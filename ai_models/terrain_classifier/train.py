import os
import torch
import torch.nn as nn
import torch.optim as optim
import pytorch_lightning as pl
from pytorch_lightning.loggers import WandbLogger
from torchvision import transforms, datasets
from efficientnet_pytorch import EfficientNet
import wandb
import onnx
import tensorflow as tf
import numpy as np
from torch.utils.data import DataLoader

# Configurations
class Config:
    data_dir = '../../datasets/terrain_images'
    batch_size = 32
    num_workers = 4
    num_classes = 5  # Update as per dataset
    lr = 1e-3
    epochs = 30
    model_name = 'efficientnet-b2'
    export_onnx = True
    export_tflite = True
    onnx_path = 'terrain_classifier.onnx'
    tflite_path = 'terrain_classifier.tflite'
    wandb_project = 'IndiMorph-Terrain-Classifier'

# Data Module
class TerrainDataModule(pl.LightningDataModule):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.RandomHorizontalFlip(),
            transforms.RandomRotation(10),
            transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ])

    def setup(self, stage=None):
        self.train_dataset = datasets.ImageFolder(os.path.join(self.cfg.data_dir, 'train'), transform=self.transform)
        self.val_dataset = datasets.ImageFolder(os.path.join(self.cfg.data_dir, 'val'), transform=self.transform)

    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.cfg.batch_size, shuffle=True, num_workers=self.cfg.num_workers)

    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.cfg.batch_size, shuffle=False, num_workers=self.cfg.num_workers)

# Model Module
class TerrainClassifier(pl.LightningModule):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.model = EfficientNet.from_pretrained(cfg.model_name, num_classes=cfg.num_classes)
        self.criterion = nn.CrossEntropyLoss()

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = self.criterion(logits, y)
        acc = (logits.argmax(dim=1) == y).float().mean()
        self.log('train_loss', loss, on_step=True, on_epoch=True, prog_bar=True)
        self.log('train_acc', acc, on_step=True, on_epoch=True, prog_bar=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = self.criterion(logits, y)
        acc = (logits.argmax(dim=1) == y).float().mean()
        self.log('val_loss', loss, on_step=False, on_epoch=True, prog_bar=True)
        self.log('val_acc', acc, on_step=False, on_epoch=True, prog_bar=True)
        return loss

    def configure_optimizers(self):
        optimizer = optim.AdamW(self.parameters(), lr=self.cfg.lr)
        scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=self.cfg.epochs)
        return [optimizer], [scheduler]

# Export to ONNX and TFLite
@torch.no_grad()
def export_to_onnx_and_tflite(model, cfg):
    dummy_input = torch.randn(1, 3, 224, 224)
    torch.onnx.export(model, dummy_input, cfg.onnx_path, input_names=['input'], output_names=['output'], opset_version=12)
    print(f"Exported to ONNX: {cfg.onnx_path}")
    # Convert ONNX to TFLite
    onnx_model = onnx.load(cfg.onnx_path)
    tf_rep = tf.experimental.onnx.export(onnx_model)
    converter = tf.lite.TFLiteConverter.from_concrete_functions([tf_rep])
    tflite_model = converter.convert()
    with open(cfg.tflite_path, 'wb') as f:
        f.write(tflite_model)
    print(f"Exported to TFLite: {cfg.tflite_path}")

if __name__ == '__main__':
    cfg = Config()
    wandb_logger = WandbLogger(project=cfg.wandb_project)
    data_module = TerrainDataModule(cfg)
    model = TerrainClassifier(cfg)
    trainer = pl.Trainer(max_epochs=cfg.epochs, logger=wandb_logger, accelerator='auto', devices='auto')
    trainer.fit(model, datamodule=data_module)
    if cfg.export_onnx or cfg.export_tflite:
        export_to_onnx_and_tflite(model.model, cfg) 
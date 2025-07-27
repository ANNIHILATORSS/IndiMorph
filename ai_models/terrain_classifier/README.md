# Advanced Terrain Classifier

This module implements a state-of-the-art terrain classification pipeline for IndiMorph using EfficientNetV2, PyTorch Lightning, and TFLite export for edge deployment. It supports experiment tracking with Weights & Biases and modular configuration for research extensibility.

## Features
- EfficientNetV2 backbone (pretrained, fine-tunable)
- PyTorch Lightning for scalable, reproducible training
- Data augmentation and normalization
- ONNX and TFLite export for Jetson/RPi
- Experiment tracking with Weights & Biases (wandb)
- Modular config for easy research

## Usage
1. Place your dataset in `../../datasets/terrain_images/` with `train/` and `val/` subfolders.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install efficientnet_pytorch pytorch-lightning wandb onnx tensorflow
   ```
3. Run training:
   ```bash
   python train.py
   ```
4. ONNX and TFLite models will be exported after training.

## Configuration
Edit the `Config` class in `train.py` to change hyperparameters, paths, or export options.

## Experiment Tracking
- Set your Weights & Biases API key as an environment variable: `WANDB_API_KEY=...`
- All metrics and checkpoints are logged to your wandb project.

## Edge Deployment
- Use the exported `.tflite` model for inference on Jetson Nano or Raspberry Pi.

---
For questions or improvements, open an issue or pull request! 
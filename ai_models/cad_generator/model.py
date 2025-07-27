import torch
import torch.nn as nn

class VQGAN3D(nn.Module):
    def __init__(self, in_channels=1, latent_dim=256):
        super().__init__()
        # Encoder
        self.encoder = nn.Sequential(
            nn.Conv3d(in_channels, 32, 4, stride=2, padding=1), nn.ReLU(),
            nn.Conv3d(32, 64, 4, stride=2, padding=1), nn.ReLU(),
            nn.Conv3d(64, 128, 4, stride=2, padding=1), nn.ReLU(),
            nn.Flatten(),
            nn.Linear(128*4*4*4, latent_dim)
        )
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 128*4*4*4), nn.ReLU(),
            nn.Unflatten(1, (128,4,4,4)),
            nn.ConvTranspose3d(128, 64, 4, stride=2, padding=1), nn.ReLU(),
            nn.ConvTranspose3d(64, 32, 4, stride=2, padding=1), nn.ReLU(),
            nn.ConvTranspose3d(32, in_channels, 4, stride=2, padding=1), nn.Sigmoid()
        )
    def forward(self, x):
        z = self.encoder(x)
        out = self.decoder(z)
        return out 
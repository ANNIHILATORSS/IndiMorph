import torch
import torch.nn as nn
import numpy as np
import pandas as pd

class HealthLSTM(nn.Module):
    def __init__(self, input_dim=8, hidden_dim=64, num_layers=2, output_dim=1):
        super().__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)
    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])
        return out

def train_lstm(data_path, epochs=20):
    df = pd.read_csv(data_path)
    X = df.iloc[:, :-1].values.astype(np.float32)
    y = df.iloc[:, -1].values.astype(np.float32)
    X = torch.tensor(X).unsqueeze(0)  # [batch, seq, feat]
    y = torch.tensor(y).unsqueeze(0)
    model = HealthLSTM(input_dim=X.shape[2])
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    for epoch in range(epochs):
        optimizer.zero_grad()
        out = model(X)
        loss = criterion(out, y)
        loss.backward()
        optimizer.step()
        print(f'Epoch {epoch}: Loss {loss.item()}')
    torch.save(model.state_dict(), 'health_lstm.pth')
    return model

def infer_lstm(model, X):
    with torch.no_grad():
        out = model(torch.tensor(X).unsqueeze(0))
        return out.numpy()

if __name__ == '__main__':
    # Example: train on sensor_traces.csv
    model = train_lstm('../datasets/sensor_traces/actuator_imu.csv')
    # Example inference
    # X_new = ...
    # anomaly_score = infer_lstm(model, X_new) 
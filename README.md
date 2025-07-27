# IndiMorph

IndiMorph is an AI-powered, shape-shifting multi-modal vehicle platform for smart transportation, defense, and disaster response. It combines advanced AI, real-time control, digital twin simulation, and edge deployment for robust, adaptive mobility in challenging environments.

## Problem Statement
Modern mobility systems struggle to adapt to rapidly changing terrains and mission requirements. IndiMorph addresses this by enabling vehicles to morph their shape and behavior in real time, guided by AI and sensor feedback, for optimal performance in diverse scenarios.

## Key Features
- **AI-Driven Morphing:** Real-time terrain classification and morphing control using deep learning.
- **Digital Twin:** Unity-based simulation and visualization of vehicle state, terrain, and sensor data.
- **Edge AI:** Lightweight inference pipelines for Jetson Nano/Raspberry Pi.
- **CFD Optimization:** Reinforcement learning-driven aerodynamic optimization with OpenFOAM.
- **Modular Hardware Control:** Arduino/PlatformIO firmware for actuators and sensors.
- **Robust Telemetry:** Real-time logging and health monitoring.
- **Open APIs:** Flask/FastAPI backend for remote control and integration.

## Tech Stack
- **AI/ML:** PyTorch, TensorFlow, TFLite, PyTorch Lightning, Stable Baselines3, EfficientNet, Diffusion Models
- **Backend:** Flask, FastAPI, Gunicorn, MQTT, InfluxDB
- **Edge:** OpenCV, TFLite, TensorRT, PySerial
- **Simulation:** Unity3D, ML-Agents, OpenFOAM
- **Frontend:** React, Bootstrap, Plotly Dash
- **DevOps:** GitHub Actions, Docker, PlatformIO

## Folder Structure
```
.
├── ai_models/           # All ML/AI modules
├── backend_ui/          # Flask/FastAPI backend and UI
├── datasets/            # Training and runtime data
├── digital_twin/        # Unity + MQTT digital twin
├── docs/                # Diagrams and documentation
├── edge_controller/     # Jetson/RPi runtime AI
├── morphing_control/    # Hardware control logic
├── scripts/             # Setup and utility scripts
├── simulations/         # CFD and Unity simulation logs
├── LICENSE
├── README.md
└── requirements.txt
```

## Cloud Deployment (AWS/GCP/Azure)

### Prerequisites
- [Terraform](https://www.terraform.io/downloads.html) installed
- Cloud CLI (aws/gcloud/az) configured with credentials
- Docker and Docker Compose installed

### AWS
1. Edit `terraform/aws/main.tf` and set `ami_id` and `s3_bucket` variables.
2. Run:
   ```bash
   cd terraform/aws
   terraform init
   terraform apply
   ```
3. Access the backend via the EC2 public IP.

### GCP
1. Edit `terraform/gcp/main.tf` and set `project_id`, `image`, and `gcs_bucket` variables.
2. Run:
   ```bash
   cd terraform/gcp
   terraform init
   terraform apply
   ```
3. Access the backend via the VM external IP.

### Azure
1. Edit `terraform/azure/main.tf` and set `storage_account_name` variable.
2. Run:
   ```bash
   cd terraform/azure
   terraform init
   terraform apply
   ```
3. Access the backend via the VM public IP.

---
For cloud uploads, set the appropriate environment variables (see `.env.example`).
For detailed module instructions, see the respective READMEs in each folder. 
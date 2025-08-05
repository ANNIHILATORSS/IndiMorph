# IndiMorph

**IndiMorph** is an indigenous, AI-powered, shape-shifting multi-modal mobility platform engineered for smart transportation, defense operations, and disaster response. By unifying advanced AI models, dynamic hardware control, real-time digital twin simulation, and edge deployment, IndiMorph achieves robust adaptability across complex terrains and mission-critical scenarios.


<img src="Image/Recording%202025-07-28%20001606.gif" alt="IndiMorph" />


## Problem Statement

Modern mobility platforms are often rigid and fail to adapt dynamically to unpredictable terrain or mission demands. **IndiMorph solves this by enabling vehicles to intelligently morph their shape and behavior in real-time**, guided by onboard sensors and AI inference pipelines. This allows for terrain-specific optimization, rapid response, and operational resilience.

[![DOI](https://zenodo.org/badge/DOI/10.36227/techrxiv.175432935.51798519.svg)](https://doi.org/10.36227/techrxiv.175432935.51798519/v1)


## Key Features

* **AI-Driven Morphing:** Terrain-aware morph logic powered by TFLite/ONNX classifiers and pattern mapping.
* **Digital Twin:** Real-time Unity-based visualization synchronized via MQTT and UDP bridges.
* **Edge AI:** Lightweight terrain classification and actuator control pipelines optimized for Jetson Nano/Raspberry Pi.
* **CFD Optimization:** Reinforcement Learning + OpenFOAM pipeline for aerodynamic and mission-specific design tuning.
* **Modular Hardware Control:** Arduino-based actuation of Nitinol wires and pneumatics via serial command APIs.
* **Telemetry & Health Monitoring:** Real-time logging with anomaly detection using LSTM models.
* **Secure Remote Operation:** Flask/FastAPI backend with JWT auth, Prometheus metrics, and React-based UI dashboards.

<img src="Image/Recording 2025-07-28 183848.gif" alt="IndiMorph" />


## Tech Stack

* **AI/ML:** PyTorch Lightning, TensorFlow/Keras, TFLite, ONNX, Stable Baselines3, EfficientNetV2, MobileNetV2
* **Edge Runtime:** OpenCV, PySerial, TensorRT, Python threading
* **Simulation & Twin:** Unity3D, ML-Agents, OpenFOAM, MQTT (Paho), UDP sockets
* **Backend:** Flask, FastAPI, Gunicorn, Prometheus, Grafana, JWT
* **Frontend:** React, Bootstrap, HTML5, Plotly Dash
* **DevOps & Cloud:** Docker Compose, GitHub Actions, Terraform (AWS/GCP/Azure), InfluxDB, S3/GCS/Azure Blob


## Folder Structure

```bash
.
├── ai_models/           # Terrain classifier, CAD generator, CFD optimizer
├── backend_ui/          # Flask/FastAPI backend + React/HTML dashboards
├── datasets/            # Terrain images, actuator logs, sensor traces
├── digital_twin/        # Unity3D project + MQTT & UDP bridge
├── docs/                # Technical documentation and diagrams
├── edge_controller/     # Jetson/RPi runtime: inference, PID, logging
├── morphing_control/    # Arduino firmware + Python serial bridge
├── scripts/             # Utilities, cloud uploaders, simulation runners
├── simulations/         # Batch runners for OpenFOAM & Unity
├── terraform/           # Infra-as-Code for AWS, GCP, Azure
├── docker-compose.yml   # Full stack deployment orchestrator
├── README.md
└── requirements.txt
```

---

## Cloud Deployment (AWS/GCP/Azure)

### Prerequisites

* Terraform installed
* Cloud CLI (AWS/GCP/Azure) configured
* Docker & Docker Compose
* Environment variables from `.env.example`

### Deployment Instructions

#### **AWS**

```bash
cd terraform/aws
terraform init
terraform apply
```

#### **GCP**

```bash
cd terraform/gcp
terraform init
terraform apply
```

#### **Azure**

```bash
cd terraform/azure
terraform init
terraform apply
```

> After provisioning, access the backend dashboard via the public VM IP of the respective cloud provider.

---

## Research & Extensibility

IndiMorph is built as a research-grade, modular platform with extensibility in mind. Researchers can:

* Integrate new AI models (e.g., Vision Transformers, diffusion-based CAD generation)
* Expand the morph logic to support new mission modes or hardware configurations
* Deploy on alternative edge devices or integrate with managed ML services
* Extend the Unity digital twin with reinforcement learning agents or multi-agent simulations
* Upgrade the security layer with OAuth2, mTLS, or zero-trust models

---

## Example Use Cases

* **Autonomous Terrain-Adaptive Vehicle** for defense logistics
* **Disaster Response Bot** with search-and-rescue morphology modes
* **Research Platform** for CFD-aided morphing and terrain-AI co-design
* **Edge-AI Deployment Benchmark** on resource-constrained devices like Jetson Nano

---

## Acknowledgments

This project integrates work across AI, robotics, and embedded systems. For detailed module-level architecture and implementation, please refer to the `/docs` directory and associated READMEs.

# Digital Twin (Unity + MQTT)

This module provides a real-time digital twin for IndiMorph using Unity3D and MQTT. It visualizes vehicle shape, terrain changes, and sensor inputs in real time.

## Features
- Unity3D visualization of morphing and terrain
- MQTT subscriber for real-time data
- UDP socket bridge to Unity
- Modular, extensible code

## Usage
1. Start the MQTT broker (e.g., Mosquitto):
   ```bash
   mosquitto
   ```
2. Run the MQTT subscriber:
   ```bash
   python mqtt_subscriber.py
   ```
3. Run the twin sync interface:
   ```bash
   python twin_sync_interface.py
   ```
4. Open the Unity project in `unity_project/` and press Play.
5. Morphing and terrain data will be visualized in real time.

## Customization
- Edit `UNITY_HOST` and `UNITY_PORT` in `twin_sync_interface.py` to match your Unity setup.
- Extend the MQTT topics as needed for more data.

---
For more details, see the Unity project README. 
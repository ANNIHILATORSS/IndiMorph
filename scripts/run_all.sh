#!/bin/bash
set -e
source env/bin/activate
# Start backend API
(cd backend_ui && python app.py &)
# Start MQTT subscriber
(cd digital_twin && python mqtt_subscriber.py &)
# Start Twin Sync Interface
(cd digital_twin && python twin_sync_interface.py &)
# Start AI models (example: terrain classifier)
(cd ai_models/terrain_classifier && python train.py &)
echo "All IndiMorph services launched."
wait 
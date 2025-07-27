import socket
import json
import threading
import paho.mqtt.client as mqtt

UNITY_HOST = '127.0.0.1'
UNITY_PORT = 5005
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883

class TwinSyncInterface:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.unity_addr = (UNITY_HOST, UNITY_PORT)
        self.mqtt = mqtt.Client()
        self.mqtt.on_message = self.on_mqtt_message
        self.mqtt.connect(MQTT_BROKER, MQTT_PORT, 60)
        self.mqtt.subscribe('telemetry')
        self.thread = threading.Thread(target=self.mqtt.loop_forever)
        self.thread.daemon = True
        self.thread.start()
    def on_mqtt_message(self, client, userdata, msg):
        data = msg.payload.decode()
        print(f'Relaying to Unity: {data}')
        self.sock.sendto(data.encode(), self.unity_addr)
    def send_to_unity(self, data):
        self.sock.sendto(json.dumps(data).encode(), self.unity_addr)

if __name__ == '__main__':
    tsi = TwinSyncInterface()
    while True:
        pass  # Keep main thread alive 
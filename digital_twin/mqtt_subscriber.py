import asyncio
import json
import paho.mqtt.client as mqtt

MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
TOPICS = [('terrain', 0), ('morphing', 0)]

class UnityMQTTSubscriber:
    def __init__(self, broker=MQTT_BROKER, port=MQTT_PORT):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker, port, 60)
    def on_connect(self, client, userdata, flags, rc):
        print('Connected to MQTT broker')
        for topic, qos in TOPICS:
            client.subscribe(topic, qos)
    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        print(f'Received on {msg.topic}: {payload}')
        # Relay to Unity (e.g., via socket or file)
        # Placeholder: print only
    def loop_forever(self):
        self.client.loop_forever()

if __name__ == '__main__':
    sub = UnityMQTTSubscriber()
    sub.loop_forever() 
import csv
import time
from influxdb_client import InfluxDBClient, Point, WriteOptions
import psutil

class TelemetryLogger:
    def __init__(self, csv_path='telemetry_log.csv', influx_url=None, token=None, org=None, bucket=None):
        self.csv_path = csv_path
        self.csv_file = open(csv_path, 'a', newline='')
        self.csv_writer = csv.writer(self.csv_file)
        self.influx = None
        if influx_url and token and org and bucket:
            self.influx = InfluxDBClient(url=influx_url, token=token, org=org)
            self.write_api = self.influx.write_api(write_options=WriteOptions(batch_size=1))
            self.bucket = bucket
    def log(self, data):
        # data: dict with keys like 'timestamp', 'sensor', 'ai_decision', 'actuator_state'
        self.csv_writer.writerow([data.get('timestamp'), data.get('sensor'), data.get('ai_decision'), data.get('actuator_state')])
        self.csv_file.flush()
        if self.influx:
            point = Point('telemetry')
            for k, v in data.items():
                point.field(k, v)
            self.write_api.write(bucket=self.bucket, record=point)
    def close(self):
        self.csv_file.close()
        if self.influx:
            self.influx.close()

if __name__ == '__main__':
    logger = TelemetryLogger()
    try:
        for i in range(10):
            data = {
                'timestamp': time.time(),
                'sensor': psutil.cpu_percent(),
                'ai_decision': 'road',
                'actuator_state': [90, 90, 90, 90]
            }
            logger.log(data)
            time.sleep(1)
    finally:
        logger.close() 
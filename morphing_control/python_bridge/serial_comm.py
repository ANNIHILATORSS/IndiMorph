import serial
import time
import threading

class MorphingSerialBridge:
    def __init__(self, port='COM3', baudrate=115200, timeout=1):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        self.lock = threading.Lock()
    def send_morph_command(self, angles):
        cmd = f"MORPH:{','.join(str(int(a)) for a in angles)}\n"
        with self.lock:
            self.ser.write(cmd.encode())
    def reset(self):
        with self.lock:
            self.ser.write(b'RESET\n')
    def close(self):
        self.ser.close()

if __name__ == '__main__':
    bridge = MorphingSerialBridge(port='COM3')
    try:
        bridge.send_morph_command([90, 120, 60, 90])
        time.sleep(2)
        bridge.reset()
    finally:
        bridge.close() 
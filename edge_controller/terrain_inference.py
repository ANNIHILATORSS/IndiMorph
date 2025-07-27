import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
import time
import serial

def load_model(model_path):
    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    return interpreter, input_details, output_details

def preprocess_image(img):
    img = cv2.resize(img, (224, 224))
    img = img.astype(np.float32) / 255.0
    img = (img - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]
    img = np.transpose(img, (2, 0, 1))
    img = np.expand_dims(img, 0)
    return img

def get_imu_data(port='/dev/ttyUSB0', baudrate=115200):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        line = ser.readline().decode().strip()
        imu = [float(x) for x in line.split(',')]
        ser.close()
        return imu
    except Exception:
        return [0.0]*6

def infer_terrain(interpreter, input_details, output_details, img, imu):
    interpreter.set_tensor(input_details[0]['index'], img.astype(np.float32))
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])
    return np.argmax(output)

if __name__ == '__main__':
    interpreter, input_details, output_details = load_model('model.tflite')
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        img = preprocess_image(frame)
        imu = get_imu_data()
        terrain_class = infer_terrain(interpreter, input_details, output_details, img, imu)
        print(f'Terrain class: {terrain_class}')
        time.sleep(0.1) 
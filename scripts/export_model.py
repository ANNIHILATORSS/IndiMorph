import torch
import tensorflow as tf
import argparse
import os

def export_pytorch_to_onnx(model, dummy_input, onnx_path):
    torch.onnx.export(model, dummy_input, onnx_path, input_names=['input'], output_names=['output'], opset_version=12)
    print(f'Exported to ONNX: {onnx_path}')

def export_onnx_to_tflite(onnx_path, tflite_path):
    import onnx
    import onnx_tf.backend as backend
    onnx_model = onnx.load(onnx_path)
    tf_rep = backend.prepare(onnx_model)
    converter = tf.lite.TFLiteConverter.from_concrete_functions([tf_rep.tf_module.__call__.get_concrete_function()])
    tflite_model = converter.convert()
    with open(tflite_path, 'wb') as f:
        f.write(tflite_model)
    print(f'Exported to TFLite: {tflite_path}')

def export_keras_to_tflite(keras_model_path, tflite_path):
    model = tf.keras.models.load_model(keras_model_path)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    with open(tflite_path, 'wb') as f:
        f.write(tflite_model)
    print(f'Exported to TFLite: {tflite_path}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--pytorch', type=str, help='Path to PyTorch model file')
    parser.add_argument('--onnx', type=str, help='Path to ONNX model file')
    parser.add_argument('--keras', type=str, help='Path to Keras model file')
    parser.add_argument('--tflite', type=str, required=True, help='Output TFLite file path')
    args = parser.parse_args()
    if args.pytorch:
        model = torch.load(args.pytorch)
        dummy_input = torch.randn(1, 3, 224, 224)
        export_pytorch_to_onnx(model, dummy_input, args.onnx)
        export_onnx_to_tflite(args.onnx, args.tflite)
    elif args.keras:
        export_keras_to_tflite(args.keras, args.tflite)
    else:
        print('Specify either --pytorch or --keras model to export.') 
import subprocess
import time

def run_openfoam_batch():
    subprocess.run(['python', 'openfoam/run_batch.py'], check=True)

def run_unity_batch():
    subprocess.run(['python', 'unity_logs/unity_batch_runner.py'], check=True)

def main():
    print('Running OpenFOAM batch simulations...')
    run_openfoam_batch()
    print('Running Unity batch simulations...')
    run_unity_batch()
    print('All simulations complete.')

if __name__ == '__main__':
    main() 
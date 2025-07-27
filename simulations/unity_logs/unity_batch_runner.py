import os
import subprocess
import glob

UNITY_PATH = '/Applications/Unity/Hub/Editor/2022.3.0f1/Unity'  # Update for your OS
PROJECT_PATH = '../../digital_twin/unity_project'
LOGS_DIR = './'
SCENARIOS = ['scenario1', 'scenario2']


def run_unity_batch(scenario):
    log_file = os.path.join(LOGS_DIR, f'{scenario}_log.txt')
    cmd = [
        UNITY_PATH,
        '-batchmode',
        '-projectPath', PROJECT_PATH,
        '-executeMethod', 'BatchRunner.Run',
        f'-scenario={scenario}',
        '-logFile', log_file,
        '-quit'
    ]
    subprocess.run(cmd, check=True)
    print(f'Unity batch for {scenario} complete. Log: {log_file}')


def main():
    for scenario in SCENARIOS:
        run_unity_batch(scenario)

if __name__ == '__main__':
    main() 
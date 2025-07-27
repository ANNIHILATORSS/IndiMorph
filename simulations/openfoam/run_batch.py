import os
import subprocess
import glob
import pandas as pd
from scripts.cloud_upload import upload_to_cloud

CASES_DIR = './cases/'
RESULTS_CSV = 'batch_results.csv'
CLOUD_UPLOAD = True


def run_case(case_path):
    print(f'Running case: {case_path}')
    subprocess.run(['bash', '../../ai_models/cfd_optimizer/openfoam_runner.sh', case_path], check=True)
    drag_file = os.path.join(case_path, 'drag.txt')
    with open(drag_file) as f:
        drag = float(f.read().strip().split()[-1])
    return {'case': os.path.basename(case_path), 'drag': drag}


def main():
    cases = glob.glob(os.path.join(CASES_DIR, '*'))
    results = []
    for case in cases:
        if os.path.isdir(case):
            res = run_case(case)
            results.append(res)
    df = pd.DataFrame(results)
    df.to_csv(RESULTS_CSV, index=False)
    print(f'Batch results saved to {RESULTS_CSV}')
    if CLOUD_UPLOAD:
        upload_to_cloud(RESULTS_CSV)

if __name__ == '__main__':
    main() 
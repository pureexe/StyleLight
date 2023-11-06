#!/bin/sh

# this is a command that to run stylelight from start to finish 

# 1. preprocess data
python data_prepare_laval.py

# 2. Inferecing the stylelight 
python test_lighting.py

# 3. evaluate the score
cd evaluation

# 4. tonemap the ground truth (is_toned=True)
python tonemap.py --test_data ../assets/IndoorHDRDataset2018_stylightdataset-128x256/test --out_dir gt_128x256

# 5. downsize the prediction to (128x256)

python downsize.py

# 6. tonemap the prediction
python tonemap.py --test_data ../assets/output/stylelight/indoor128x256 --out_dir pred_128x256

#!/bin/sh

# this is a command that to run stylelight from start to finish 

# 1. preprocess data
python data_prepare_laval.py

# 2. Inferecing the stylelight 
python test_lighting.py

# 3. evaluate the score
cd evaluation

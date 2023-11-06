# PURE
# down scale environment map to 128x256 as per mention in the paper 

import os 
from tqdm.auto import tqdm

from skylibs.envmap import EnvironmentMap
from skylibs.hdrio import imread, imsave

IN_DIR = "assets/output/stylelight/indoor"
OUT_DIR = "assets/output/stylelight/indoor128x256"

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    files = sorted(os.listdir(IN_DIR))
    # To match the code, this one will use skylibs to resize (but skylibs seem to have aliasing)
    for filename in files:
        # rename to match and output (remove _test from file name)
        outname = filename.replace("_test","")
        ori_path = os.path.join(IN_DIR, filename)
        # read environment map
        e = EnvironmentMap(ori_path, 'latlong')
        e.resize((128, 256)) # resize to 128x256
        imsave(os.path.join(OUT_DIR,outname), e.data)
    
    
    
if __name__ == "__main__":
    main()
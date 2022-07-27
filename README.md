# StyleLight: HDR Panorama Generation for Lighting Estimation and Editing  

### [Project](https://style-light.github.io/) | [YouTube](https://www.youtube.com/watch?v=sHeWK1MSPg4) | [arXiv](https://www.youtube.com/watch?v=sHeWK1MSPg4) 

<img src='imgs/Fig1.jpg' width=100%>



>**Abstract:** We present a new lighting estimation and editing framework to generate high-dynamic-range (HDR) indoor panorama lighting from a single limited field-of-view (FOV) image captured by low-dynamic-range (LDR) cameras. Existing lighting estimation methods either directly regress lighting representation parameters or decompose this problem into FOV-to-panorama and LDR-to-HDR lighting generation sub-tasks. However, due to the partial observation, the high-dynamic-range lighting, and the intrinsic ambiguity of a scene, lighting estimation remains a challenging task. To tackle this problem, we propose a coupled dual-StyleGAN panorama synthesis network (StyleLight) that integrates LDR and HDR panorama synthesis into a unified framework. The LDR and HDR panorama synthesis share a similar generator but have separate discriminators. During inference, given an LDR FOV image, we propose a focal-masked GAN inversion method to find its latent code by the LDR panorama synthesis branch and then synthesize the HDR panorama by the HDR panorama synthesis branch. StyleLight takes FOV-to-panorama and LDR-to-HDR lighting generation into a unified framework and thus greatly improves lighting estimation. Extensive experiments demonstrate that our framework achieves superior performance over state-of-the-art methods on indoor lighting estimation. Notably, StyleLight also enables intuitive lighting editing on indoor HDR panoramas, which is suitable for real-world applications. Our code will be released to facilitate future research.

[Guangcong Wang](https://wanggcong.github.io/), [Yinuo Yang](https://www.linkedin.com/in/yinuo-yang-3a55041b8/), [Chen Change Loy](https://www.mmlab-ntu.com/person/ccloy/), [Ziwei Liu](https://liuziwei7.github.io/) 
 S-Lab, Nanyang Technological University

 In **European Conference on Computer Vision (ECCV)**, 2022  

### Fast Video-to-Video Translation

<p align='center'>  
  <img src='imgs/performance.gif' width='90%'/>  
</p>

### Peformance

<p align='left'>  
  <img src='imgs/metrics.png' width='60%'/>  
</p>

## Prerequisites
- Linux or macOS
- Python 3
- NVIDIA GPU + CUDA cuDNN
- PyTorch >= 1.0
- ffmpeg toolbox >= 4.0
- OpenCV

## Getting Started

### Inference Enviroment
We recommend using the virtual environment (conda) to run the code easily.

```
conda create -n fvid python=3.7;
conda activate fvid;
conda install pytorch==1.7.1 torchvision==0.8.2 cudatoolkit=10.1;
conda install ffmpeg==4.0.2;
pip install opencv-python dominate scipy tqdm matplotlib scikit-image;
```

### Download examples
- Please first download the example ``datasets`` from [this link](https://drive.google.com/file/d/18LzfxnD0xUr4Bu-NrzrjzOoN0jUodgOW/view?usp=sharing).


### Download pretrained models 
- Face 
  - Download the pretrained model from [this link](https://drive.google.com/file/d/1rqZfQ5X1zVLvObqzJZFCG5tFMPGGHu9u/view?usp=sharing) and unzip it in ``checkpoints`` folder.
  - To test the model. 
    ```
    bash scripts/face/test.sh
    ```

- Cityscapes  
  -  Download the pretrained model from [this link](https://drive.google.com/file/d/1AOAen8rcRhcJHX7QjyWAItCN243mHpxA/view?usp=sharing) and unzip it in ``checkpoints`` folder.
  - To test the model. 
    ```
    bash scripts/street/test.sh
    ```

## Training 

### Installation

Please first install [FlowNet2](https://github.com/NVIDIA/flownet2-pytorch) into ``models/flownet2_pytorch/``.


### Dataset
- Cityscapes
  - Please download the full-size dataset (~300 GB) from the [official website](https://www.cityscapes-dataset.com/).
  - We pre-pocess the corresponding semantic maps (A) and instance maps (Inst) by well-trained models.
- Face
  - We adopt the [FaceForensics](http://niessnerlab.org/projects/roessler2018faceforensics.html) dataset. The keypoints of each frame are generated by landmark detection. We then interpolate the keypoints to get face edges.
- Pose
  - We use dancing videos on YouTube following vid2vid. We then apply DensePose and OpenPose to estimate the poses for each frame. Due to the pravicy issues, we do not release the pretrained model for Pose2Body, which is kept the same as vid2vid.



## To-Do
- [x] Inference Code
- [x] Example datasets
- [x] Example Pretrained Models 
- [ ] Update Pretrained Models
- [ ] Clean Training Code
- [ ] Training Instructions


## Citation

If you find this useful for your research, please cite the our paper.

```
@inproceedings{wang2022stylelight,
   author    = {Wang, Guangcong and Yang, Yinuo and Loy, Chen Change and Liu, Ziwei},
   title     = {StyleLight: HDR Panorama Generation for Lighting Estimation and Editing},
   booktitle = {European Conference on Computer Vision (ECCV)},   
   year      = {2022},
  }
```

or
```
Guangcong Wang, Yinuo Yang, Chen Change Loy, and Ziwei Liu. StyleLight: HDR Panorama Generation for Lighting Estimation and Editing, ECCV 2022.
```

## Acknowledgments
This code is based on the [StyleGAN2-ada-pytorch](https://github.com/NVlabs/stylegan2-ada-pytorch) codebase. 

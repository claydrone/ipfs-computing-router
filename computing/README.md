# Image Classification

image_classification.ipynb consists of transfer learning with ResNet50

tensorflow 1.13.1 is required (1.13.1 is the default package version on nbai.io as of Dec 2, 2020)

## Dataset

10 Monkey Species: https://calibration-ipfs.filswan.com/ipfs/QmQhckZqk2rPyeyekt6KMTAR4TEKAs1xi8R3DTCgFqfQgs

## Running ipynb

Open notebook after login to https://nbai.io

Create folder with name "monkey" in the same directory and unzip the dataset to have the following schema

```
.
├── image_classification.ipynb
└── monkey
    ├── monkey_labels.txt
    ├── training
    │   └── training
    │       ├── n0
    │       ├── n1
    │       ├── n2
    │       ├── n3
    │       ├── n4
    │       ├── n5
    │       ├── n6
    │       ├── n7
    │       ├── n8
    │       └── n9
    └── validation
        └── validation
            ├── n0
            ├── n1
            ├── n2
            ├── n3
            ├── n4
            ├── n5
            ├── n6
            ├── n7
            ├── n8
            └── n9
```


Install TensorFlow

```
!pip install opencv-python==4.5.5.64
pip install --upgrade TensorFlow

```


Tensorflow uses GPU by default if GPU is enabled

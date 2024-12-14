# YOLO IMPLEMENTATION AND USAGE IN RASPBERRYPI4 USING PYTHON

This project is aimed to be an installation guide for using YOLO in raspbberyPi4 (from now will be refered as raspi)

## I. Pre-Requisites.

First step before using YOLO in python are installing python itself and the library (using ultralytics)

### Step 1: Make sure raspi software are up to date

```
sudo apt update
sudo apt full-upgrade
```

### Step 2: Install python, pip, and ultralytics

```
sudo apt install python3-pip -y
pip install -U pip
pip install ultralytics
```

### Step 2.5: If there is an error

Sometime the installation of package and library will be blocked by the system. One solution is to use virtual enviroment as follow Change the virtual enviroment name as desired. Then wait for the installation to complete.

```
sudo apt install python3-venv
python3 -m venv <virtual enviroment name>
source <virtual enviroment name>/bin/activate
pip install ultralytics
```

### Step 3: Verification

Check if the installation is successfull using simple python code below

```
from ultralytics import YOLO

# Load a YOLO11n PyTorch model
model = YOLO("yolo11n.pt")

# Export the model to NCNN format
model.export(format="ncnn")  # creates 'yolo11n_ncnn_model'

# Load the exported NCNN model
ncnn_model = YOLO("yolo11n_ncnn_model")

# Run inference
results = ncnn_model("https://ultralytics.com/images/bus.jpg", save=True)
```

The result should be as follow.

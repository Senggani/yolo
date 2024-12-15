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

The result should be saved in the directory stated in the command line.

### Step 4: Other

For this implementation, needed backend service that will be recieving image and an RMQ service as a queue holder before sending image via API to backend. Configure url for backend API and RMQ parameter in the code (for both capture.py and detect.py). Make sure you are using the latest code
```
git clone https://github.com/Senggani/yolo
git pull
```

## II. Specific Implementation
On this implementation, the image source are from image buffer captured from webcam. Raspi will be accessed using PuTTy

### Step 1: Connect to Raspi using SSH
Open PuTTy, made sure to connect to the same network as raspi. hostname is admin@pmmodule in port 22.
Login to the raspi then start virtual enviroment.
```
source virt/bin/activate
cd ./yolo
python3 capture.py
python3 upload.py   # open python file in different putty session!
```

### Step 2: Run the backend
```
npm start
```


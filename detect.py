from ultralytics import YOLO
import os

# image source
img = "./20241123_173039.jpg"

model_name = "yolo11n"
model_directory = "./" + model_name + "_ncnn_model"

export_directory = "./image"

if not(os.path.isdir(model_directory)):
    face_model = YOLO(model_name + ".pt")
    face_model.export(format='ncnn')
    
if not(os.path.isdir(export_directory)):
    os.makedirs(export_directory)

ncnn_face_model = YOLO(model_directory)
results = ncnn_face_model.predict(source=img, project=export_directory)
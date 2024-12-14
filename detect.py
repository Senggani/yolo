from ultralytics import YOLO

# image source
img = "./20241123_173039.jpg"

face_model = YOLO("best.pt")
face_model.export(format='ncnn')

ncnn_face_model = YOLO("best_ncnn_model")
results = ncnn_face_model.predict(source=img, project="images")
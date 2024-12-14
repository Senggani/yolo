from datetime import datetime
import cv2 as cv
import time, pika
from ultralytics import YOLO
import os

path = "./image/"
# Inisiasi model untuk YOLO
model_name = "yolo11n"
model_directory = "./" + model_name + "_ncnn_model"

export_directory = "./image"

if not(os.path.isdir(model_directory)):
    face_model = YOLO(model_name + ".pt")
    face_model.export(format='ncnn')

ncnn_face_model = YOLO(model_directory)

# Menyalakan kamera
cap = cv.VideoCapture(0)
if not cap.isOpened():
	print("Camera not detected")
	exit()

while True:
  # Mendapatkan waktu saat ini sebagai penamaan file
  current_datetime = datetime.now()
  formatted_date = current_datetime.strftime("%Y%m%d_%H%M%S")
  fullPath = (path + formatted_date + ".jpg")

  # Mengambil gambar
  ret, image = cap.read()
  if not ret:
    print("error to capture image")

  #=============     YOLO     =============#
#   image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
  
    results = ncnn_face_model.predict(source=image, project=export_directory, name="image_name.jpg")
    print(results.boxes.cls)

  #-------------     YOLO     -------------#

  #============= RMQ Produce  =============#
#   credentials = pika.PlainCredentials(username='pm_modue', password='hl6GjO5LlRuQT1n')
#   connection = pika.BlockingConnection(pika.ConnectionParameters('rmq2.pptik.id', 5672, '/pm_module', credentials))
#   channel = connection.channel()

#   channel.queue_declare(queue='opencv_status')
  
#   message = ('{"full_path": "'+fullPath+'", "total_face": '+str(len(face))+', "total_body": '+str(len(body))+'}')

#   channel.basic_publish(exchange='',
#                         routing_key='opencv_status',
#                         body=message)
#   print(" [x] Sent: " + message)

#   connection.close()
  #------------- RMQ Produce  -------------#

  # Delay untuk pengambilan gambar selanjutnya
  time.sleep(10)

# Mematikan kamera
cap.release


from ultralytics import YOLO

model = YOLO("runs/detect/level3_pothole_finetune/weights/best.pt")

model.val(data="pothole_dataset/data.yaml")
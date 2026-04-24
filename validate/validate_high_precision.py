from ultralytics import YOLO

model = YOLO("runs/detect/level3_high_precision/weights/best.pt")

model.val(data="dataset.yaml")
from ultralytics import YOLO

model = YOLO("yolov8m.pt")

model.train(
    data="dataset.yaml",
    epochs=30,
    imgsz=640,
    batch=16,
    lr0=0.003,
    optimizer="Adam",
    weight_decay=0.0005,
    patience=10,
    hsv_h=0.015,
    hsv_s=0.7,
    hsv_v=0.4,
    fliplr=0.5,
    mosaic=1.0,
    name="level3_high_precision"
)
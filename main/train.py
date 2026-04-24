from ultralytics import YOLO

model = YOLO("runs/detect/road_damage_final/weights/best.pt")

model.train(
    data="archive (2)/data.yaml",
    epochs=10,
    imgsz=640,
    batch=8,
    lr0=0.005,
    optimizer="AdamW",
    name="road_damage_finetuned"
)
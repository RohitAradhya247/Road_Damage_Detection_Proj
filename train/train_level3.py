from ultralytics import YOLO

model = YOLO("runs/detect/road_damage_final/weights/best.pt")

model.train(
    data="pothole_dataset/data.yaml",
    epochs=10,
    imgsz=640,
    batch=8,
    lr0=0.005,
    optimizer="Adam",
    name="level3_pothole_finetune"
)
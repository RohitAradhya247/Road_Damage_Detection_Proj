from ultralytics import YOLO

model = YOLO("runs/detect/road_damage_final/weights/best.pt")

model.predict(
    source="RDD2022/India/test/images",
    save=True,
    show=True,
    conf=0.15
)
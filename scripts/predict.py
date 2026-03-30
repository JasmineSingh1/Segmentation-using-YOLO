from ultralytics import YOLO

model = YOLO("models/YOLO11s-seg_best.pt")

model.predict(
    source="data/test/images",
    save=True,
    conf=0.25
)
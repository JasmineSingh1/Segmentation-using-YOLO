from ultralytics import YOLO

model = YOLO("models/YOLO11s-seg_best.pt")

metrics = model.val(
    data="configs/data.yaml",
    split="val"
)

print(metrics)
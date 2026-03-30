from ultralytics import YOLO
import torch

device = 0 if torch.cuda.is_available() else "cpu"

model = YOLO("yolo11s-seg.pt")

model.train(
    data="configs/data.yaml",
    epochs=150,
    imgsz=640,
    batch=8,
    patience=40,
    device=0
)
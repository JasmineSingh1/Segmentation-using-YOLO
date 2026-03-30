import cv2
from ultralytics import YOLO

model = YOLO("models/YOLO11s-seg_best.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated = results[0].plot()

    cv2.imshow("YOLO Segmentation", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):   # press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
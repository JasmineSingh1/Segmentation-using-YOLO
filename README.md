# End-to-End YOLO Pipeline for Object Segmentation
This repository provides an end-to-end implementation of segmentation using YOLO-based models, supporting custom dataset training, evaluation, and real-time inference.

---

## Features

* Train YOLO segmentation models on custom datasets
* Evaluate performance using mAP, precision, and recall
* Real-time webcam segmentation using OpenCV
* GPU-accelerated training (Kaggle / Colab compatible)
* Scalable to multiple YOLO versions

---

## Structure

```
project-root/
│
├── config/
│   └── data.yaml
│
├── data/
│   └── README.md
│
├── models/
│   └── README.md
│
├── notebooks/
│   └── yolo11s-segcustomtrained.ipynb
│
├── scripts/
│   ├── train.py
│   ├── validate.py
│   ├── predict.py
│   └── webcam_inference.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Dataset Setup

The dataset is not included in this repository due to size limitations.

### Link to access the dataset

* Download the dataset from https://app.roboflow.com/jasmines-workspace-esjaa/yolov11seg/1

### Expected Structure

```
data/
 ├── train/
 │   ├── images/
 │   └── labels/
 ├── valid/
 │   ├── images/
 │   └── labels/
 └── test/
     ├── images/
     └── labels/
```

---

## Configuration

Edit:

```
configs/data.yaml
```

```yaml
path: data

train: train/images
val: valid/images
test: test/images

nc: 1
names: ['object']
```

---

## Training

```bash
python scripts/train.py
```

---

## Validation

```bash
python scripts/validate.py
```

---

## Testing / Inference on Images

```bash
python scripts/predict_images.py
```

---

## Real-Time Webcam Inference

```bash
python scripts/webcam_inference.py
```

Press **'q'** to exit.

---

## Pretrained Model

The trained model weights (`YOLO11s-seg_best.pt`) are not included in this repository.

Download from:
https://www.kaggle.com/datasets/jasminesingh01/yolo11s-segmentation-model

Place it in:
```
models/YOLO11s-seg_best.pt
```

---

## Notebook

The full training workflow is available in:

```
notebooks/yolo11s-segcustomtrained.ipynb
```

---

## Evaluation Metrics

* Precision
* Recall
* mAP@50
* mAP@50-95
* Mask accuracy

---

## Notes

* Update dataset path in `data.yaml` if needed
* Ensure GPU is enabled for faster training
* Compatible with multiple YOLO versions

---

<!-- ## 📜 License

This project is licensed under the MIT License.

--- -->
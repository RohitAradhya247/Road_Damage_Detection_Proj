# Road Damage Detection using YOLOv8

A deep learning project for detecting and classifying road damage such as cracks and potholes using YOLOv8.

---

## Team Members

- Rohit Rajashekar Aradhya
- Sonika K V

---

## Project Overview

The project is divided into three levels:

| Level | Description |
|-------|-------------|
| Level 1 | Binary classification — Pothole vs. No Pothole |
| Level 2 | Multi-class detection — Longitudinal Crack, Transverse Crack, Alligator Crack, Pothole |
| Level 3 | Improved model with better tuning and higher precision (Extra Credit) |

---

## Project Structure

```
Road_Damage_Detection_Proj/
├── configs/        # Dataset configuration files (YAML)
├── main/           # Main scripts (training, prediction)
├── preprocess/     # Data preprocessing scripts
├── train/          # Training scripts for each level
├── validate/       # Validation scripts
├── test/           # Testing scripts
├── models/         # Trained YOLO model weights (.pt files)
└── results/        # Predictions, logs, and output results
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/RohitAradhya247/Road_Damage_Detection_Proj.git
cd Road_Damage_Detection_Proj
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```

### 3. Install Dependencies

```bash
pip install ultralytics
pip install opencv-python matplotlib
```

---

## Dataset

- Dataset used: [RDD2022 — Road Damage Dataset](https://github.com/sekilab/RoadDamageDetector)
- Contains real-world road images from multiple countries
- Dataset is not included in this repo due to large file size — download it separately and update the paths in the YAML config files before running anything

---

## Preprocessing

```bash
python preprocess/convert.py
python preprocess/remove_duplicates.py
python preprocess/split_dataset.py
```

---

## Training

### Level 1 — Binary Classification

```bash
python train/train.py
```

### Level 2 — Multi-class Detection

```bash
yolo detect train model=yolov8n.pt data=configs/data_fixed.yaml epochs=10
```

### Level 3 — Improved Model (Extra Credit)

```bash
python train/train_level3.py
```

---

## Validation

### Standard

```bash
yolo val model=models/best.pt data=configs/dataset.yaml
```

### Level 3

```bash
python validate/validate_level3.py
```

---

## Prediction

```bash
python main/predict.py
```

Output is saved to `results/`.

---

## Results Summary

| Level | Description | Outcome |
|-------|-------------|---------|
| Level 1 | Binary detection | Good baseline |
| Level 2 | Multi-class detection | Moderate accuracy |
| Level 3 | Improved model | Better mAP, precision and recall |

Level 3 improvements include better hyperparameter tuning, improved class balance, and fine-tuning focused on pothole detection. This contributes +10% extra credit in the course evaluation.

---

## Notes

- Dataset is not included — download and set up paths manually
- Update dataset paths in YAML files before running training
- Training on CPU is very slow — GPU is recommended

---

## References

- [Ultralytics YOLOv8 Documentation](https://docs.ultralytics.com)
- [RDD2022 Road Damage Dataset](https://github.com/sekilab/RoadDamageDetector)
- Course lecture materials (EECE 5639 — Computer Vision, Northeastern University)

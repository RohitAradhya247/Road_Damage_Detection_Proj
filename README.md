# 🚧 Road Damage Detection using YOLOv8

This project focuses on detecting and classifying different types of road damage using deep learning (YOLOv8). The system analyzes road images and identifies defects such as cracks and potholes.

---

## 👥 Team Members
- Rohit Rajashekar Aradhya  
- Sonika K V  

---

## 📌 Project Overview

The project is divided into three levels:

- **Level 1:** Binary classification (Pothole vs No Pothole)  
- **Level 2:** Multi-class detection  
  - Longitudinal Crack  
  - Transverse Crack  
  - Alligator Crack  
  - Pothole  
- **Level 3 (Extra Credit):** Improved model with tuning and higher precision  

---

## 📂 Project Structure


configs/ → Dataset configuration files (YAML)
main/ → Main scripts (training, prediction)
preprocess/ → Data preprocessing scripts
train/ → Training scripts for different levels
validate/ → Validation scripts
test/ → Testing scripts
models/ → Trained YOLO models (.pt files)
results/ → Output results, predictions, logs


---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/RohitAradhya247/Road_Damage_Detection_Proj.git
cd Road_Damage_Detection_Proj
2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
3. Install dependencies
pip install ultralytics
pip install opencv-python matplotlib
📊 Dataset
Dataset used: RDD2022 (Road Damage Dataset)
Contains real-world road images from multiple countries
Dataset is not included in this repository due to large size

👉 Place dataset in the correct directory before running

🔄 Preprocessing

Run the following scripts:

python preprocess/convert.py
python preprocess/remove_duplicates.py
python preprocess/split_dataset.py
🧠 Training
Level 1 (Binary Model)
python train/train.py
Level 2 (Multi-class Model)
yolo detect train model=yolov8n.pt data=configs/data_fixed.yaml epochs=10
Level 3 (Improved Model)
python train/train_level3.py
📈 Validation
Standard validation
yolo val model=models/best.pt data=configs/dataset.yaml
Level 3 validation
python validate/validate_level3.py
🔍 Prediction
python main/predict.py

Results will be saved in:

results/
📊 Results Summary
Level	Description	Outcome
Level 1	Binary detection	Good baseline
Level 2	Multi-class detection	Moderate accuracy
Level 3	Improved model	Better precision and performance
Level 3 Improvements:
Better hyperparameter tuning
Improved class balance
Fine-tuning for pothole detection
Higher mAP and recall
🚀 Extra Credit (Level 3)

Level 3 focuses on improving performance over Level 2 by:

Enhancing model precision
Optimizing training parameters
Improving detection quality

This contributes to +10% extra credit in the course evaluation.

⚠️ Notes
Dataset is not included in this repository
Update dataset paths in YAML files before running
Training on CPU is slow — GPU recommended
📚 References
Ultralytics YOLOv8 Documentation
RDD2022 Dataset
Course lecture materials
✅ Final Outcome
Built an end-to-end road damage detection system
Implemented multi-level detection pipeline
Improved performance using Level 3 enhancements
Successfully structured and deployed the project

import os
import random
import shutil

img_src = "data/images/all"
lbl_src = "data/labels/all"

img_train = "data/images/train"
img_val = "data/images/val"
lbl_train = "data/labels/train"
lbl_val = "data/labels/val"

os.makedirs(img_train, exist_ok=True)
os.makedirs(img_val, exist_ok=True)
os.makedirs(lbl_train, exist_ok=True)
os.makedirs(lbl_val, exist_ok=True)

files = [f for f in os.listdir(img_src) if f.endswith(".jpg")]

random.shuffle(files)

split_ratio = 0.8
split_index = int(len(files) * split_ratio)

train_files = files[:split_index]
val_files = files[split_index:]

train_count = 0
val_count = 0

for file in train_files:
    img_path = os.path.join(img_src, file)
    lbl_path = os.path.join(lbl_src, file.replace(".jpg", ".txt"))

    if not os.path.exists(lbl_path):
        continue

    shutil.copy(img_path, os.path.join(img_train, file))
    shutil.copy(lbl_path, os.path.join(lbl_train, file.replace(".jpg", ".txt")))
    train_count += 1

for file in val_files:
    img_path = os.path.join(img_src, file)
    lbl_path = os.path.join(lbl_src, file.replace(".jpg", ".txt"))

    if not os.path.exists(lbl_path):
        continue

    shutil.copy(img_path, os.path.join(img_val, file))
    shutil.copy(lbl_path, os.path.join(lbl_val, file.replace(".jpg", ".txt")))
    val_count += 1

print(f"Train images: {train_count}")
print(f"Val images: {val_count}")
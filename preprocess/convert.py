import os
import xml.etree.ElementTree as ET
import shutil

class_map = {
    "D00": 0,
    "D10": 1,
    "D20": 2,
    "D40": 3
}

countries = ["India", "United_States", "Japan", "Czech", "China_Drone"]

img_out = "data/images/all"
lbl_out = "data/labels/all"

os.makedirs(img_out, exist_ok=True)
os.makedirs(lbl_out, exist_ok=True)

count = 0

for country in countries:
    img_dir = f"RDD2022/{country}/train/images"
    ann_dir = f"RDD2022/{country}/train/annotations/xmls"

    for file in os.listdir(ann_dir):
        if not file.endswith(".xml"):
            continue

        xml_path = os.path.join(ann_dir, file)
        tree = ET.parse(xml_path)
        root = tree.getroot()

        img_name = root.find("filename").text
        img_path = os.path.join(img_dir, img_name)

        if not os.path.exists(img_path):
            continue

        size = root.find("size")
        w = int(size.find("width").text)
        h = int(size.find("height").text)

        labels = []

        for obj in root.findall("object"):
            cls = obj.find("name").text

            if cls not in class_map:
                continue

            cls_id = class_map[cls]

            bbox = obj.find("bndbox")
            xmin = int(bbox.find("xmin").text)
            ymin = int(bbox.find("ymin").text)
            xmax = int(bbox.find("xmax").text)
            ymax = int(bbox.find("ymax").text)

            x_center = ((xmin + xmax) / 2) / w
            y_center = ((ymin + ymax) / 2) / h
            width = (xmax - xmin) / w
            height = (ymax - ymin) / h

            labels.append(f"{cls_id} {x_center} {y_center} {width} {height}")

        if len(labels) == 0:
            continue

        shutil.copy(img_path, os.path.join(img_out, img_name))

        label_path = os.path.join(lbl_out, img_name.replace(".jpg", ".txt"))
        with open(label_path, "w") as f:
            f.write("\n".join(labels))

        count += 1

print(f"Total images: {count}")
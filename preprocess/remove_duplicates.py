import os
from PIL import Image
import imagehash

folder = "images"
hashes = {}
duplicates = []

for filename in os.listdir(folder):
    path = os.path.join(folder, filename)

    try:
        img = Image.open(path)
        h = imagehash.average_hash(img)

        if h in hashes:
            duplicates.append(path)
        else:
            hashes[h] = path

    except:
        continue

for dup in duplicates:
    os.remove(dup)

print(f"Removed {len(duplicates)} duplicates")
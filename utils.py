import json
import config
import os

from collections import defaultdict

def pre_index(annotation_path):
    with open(annotation_path, 'r') as file:
        annotations = json.load(file)
    data = defaultdict(list)

    for item in annotations["annotations"]:
        img_id = item['image_id']
        data[img_id].append([item['category_id']] + item['bbox'])

    return data



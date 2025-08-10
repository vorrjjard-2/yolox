import json
import config
import os

from collections import defaultdict

def pre_index(annotation_path):
    with open(annotation_path, 'r') as file:
        annotations = json.load(file)

    id_annotations = defaultdict(list)
    id_images = {}
    id_categories = {} 

    #ID TO ANNOTATIONS

    for item in annotations["annotations"]:
        img_id = item['image_id']
        id_annotations[img_id].append([item['category_id']] + item['bbox'])

    # ID TO IMAGE
    for item in annotations["images"]:
        id = item['id']
        id_images[id] = [item['file_name'], item['width'], item['height']]
    
    for item in annotations['categories']:
        category_id = item['id']
        id_categories[category_id] = item['name']
        
    return id_annotations, id_images, id_categories

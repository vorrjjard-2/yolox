import json
import config
import os

from collections import defaultdict

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

from PIL import Image, ImageFile

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
        id_images[id] = (item['file_name'], item['width'], item['height'])
    
    for item in annotations['categories']:
        category_id = item['id']
        id_categories[category_id] = item['name']
        
    return (id_annotations, id_images, id_categories)


def plot_image(img_path, bboxes):
    img = np.array(Image.open(img_path).convert("RGB"))
    fig, ax = plt.subplots(1)

    ax.imshow(img)
    for bbox_coords in bboxes:
        rect = patches.Rectangle((bbox_coords[0], bbox_coords[1]),
                                bbox_coords[2], bbox_coords[3],
                                linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    plt.show()

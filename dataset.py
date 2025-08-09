import config
import numpy as np
import torch
from PIL import Image, ImageFile
from torch.utils.data import Dataset, DataLoader

from PIL import Image, ImageFile

from utils import (
    pre_index
)

import json
import os

ImageFile.LOAD_TRUNCATED_IMAGES = True

class YOLODataset(Dataset):
    def __init__(self, 
                 split, 
                 S=[13, 26, 52],
                 transform=None
                   ):
        super().__init__()
        self.split = split
        self.S = S
        self.transform = transform
        self.annotations = pre_index(os.path.join('datasets', config.DATASET, self.split, '_annotations.coco.json'))

    def __len__(self):
        return len(self.annotations)
    
    def __getitem__(self, index):
        image = np.array(Image.open(img_path).convert("RGB"))
            


        return super().__getitem__(index)

import config
import numpy as np
import torch
from PIL import Image, ImageFile
from torch.utils.data import Dataset, DataLoader

ImageFile.LOAD_TRUNCATED_IMAGES = True

class YOLODataset(Dataset):
    def __init__(self, 
                 split, 
                 annotations,
                 S=[13, 26, 52],
                 transform=None
                   ):
        super().__init__()
        self.split = split
        self.annotations = annotations
        self.S = S
        self.transform = transform


    def __len__(self):
        return len(self.annotations)

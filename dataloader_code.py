import h5py

# Path to your H5 file
file_path = 'SSL.keypoints.train.0.h5'

import h5py

def h5_to_dict(group):
    result = {}
    for key, item in group.items():
        if isinstance(item, h5py.Group):  # if the item is a group, recursively convert it
            result[key] = h5_to_dict(item)  # only the value (item) is converted
        else:  # if the item is a dataset, get the data
            result[key] = item[()]
    return result


# Open the H5 file in read mode and convert it to a dictionary
with h5py.File(file_path, 'r') as f:
    data = h5_to_dict(f)


dataset_ = list(data.values())


import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np


# Open the file and read its content
with open('GTEnglish.txt', 'r') as file:
    # Read all lines into a list, with each line including its newline character
    lines = file.readlines()

# Remove the newline character from each line
labels = [line.rstrip('\n') for line in lines]


# Step 1: Define a custom Dataset class
class MyDataset(Dataset):
    def __init__(self, dataset,labels):
        """
        Args:
            data (tensor or ndarray): The data points (features).
            labels (tensor or ndarray): The corresponding labels.
        """
        self.dataset = dataset
        self.labels = labels
        
    def __len__(self):
        """Return the number of samples in the dataset."""
        return len(self.dataset)

    def __getitem__(self, idx):
        """Return a sample (data point and label) by index."""
        sample = (list(self.dataset[idx].values())[0])
        sample = np.expand_dims(sample, axis=0)
        label =  self.labels[int(list(self.dataset[idx].keys())[0].split("_")[-1])]
        return sample, label

Dataset = MyDataset(dataset_,labels)

# Step 3: Define DataLoader
dataloader = DataLoader(Dataset, batch_size=1, shuffle=True, num_workers=2)

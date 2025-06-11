import time
import numpy as np
import os, re
import threading, logging, copy
from random import shuffle
import torch

def get_dataset(path, f_format, nfeat):
    if f_format.endswith('trainset_with_scaled_normalized.txt'):
        dump_file = '/train.npy'
    elif f_format.endswith('predictset_with_scaled_normalized.txt'):
        dump_file = '/predict.npy'
    dump_file = './train/train.npy'
    st_time = time.time()
    data = np.load(dump_file,allow_pickle=True)
    return data
def get_format(file): 
    data = []
    with open(file, 'r') as f:
        data = list(f.readlines())
        data = list(map(lambda x: re.sub(r"([ ]+)",",",x),data))
    f_format = ''
    if file == 'data/trainset_with_scaled_normalized.txt':
        f_format = './data/trainset_with_scaled_format.txt'
    elif file == 'data/predictset_with_scaled_normalized.txt':
        f_format = './data/predictset_with_scaled_format.txt'
    with open(f_format, "w") as f:
        f.writelines(data)
        return f_format
if __name__ == "__main__":
    import os, logging
    log_path = "./logs/"
    if not os.path.exists(log_path): os.mkdir(log_path)
    logging.basicConfig(
        filename=os.path.join(log_path, "out.log"),
        format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',
        level=logging.INFO
    )


class TrainDataset(object):
    def __init__(self, data, device):
        self.data = list(data)
        self.offset = 0
        self.device = device
    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx):
        X = np.array(self.data[idx][0]).astype(np.float16)
        X = torch.FloatTensor(X)
        y = np.array([self.data[idx][3]])
        y = torch.FloatTensor(y)
        flag_list = self.data[idx][1]
        struct_name = self.data[idx][2]
        X = X.to(self.device)
        y = y.to(self.device)
        return X, flag_list, y, struct_name
class PredictDataset(object):
    def __init__(self, data, device):
        self.data = list(data)
        self.offset = 0
        self.device = device
    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx):
        X = np.array(self.data[idx][0]).astype(np.float16)
        X = torch.FloatTensor(X)
        flag_list = self.data[idx][1]
        struct_name = self.data[idx][2]
        X = X.to(self.device)
        return X, flag_list, struct_name



import os
import shutil
import numpy as np
import sklearn.model_selection as model_selection
import random

def train_test_split(dir_path):
  cc_list=[]
  bz_list=[]
  for root,dirs,files in os.walk(dir_path):
    for dir in dirs:
      if "cc" in dir:
        cc_list.append(dir)
      if "bz" in dir:
        bz_list.append(dir)
        
  # create temporary fake labels     
  cc_labels = np.ones(len(cc_list))
  bz_labels = np.ones(len(bz_list))
  
  # create train/val/test subsets in [0.6:0.2:0.2] ratio using scikit
  cc_train, cc_test, cc_train_labels, cc_test_labels = model_selection.train_test_split(cc_list, cc_labels, train_size=0.8,test_size=0.2, random_state=10)
  cc_train, cc_val, cc_train_labels, cc_val_labels = model_selection.train_test_split(cc_train, cc_train_labels, train_size=0.75,test_size=0.25, random_state=10)
  
  bz_train, bz_test, bz_train_labels, bz_test_labels = model_selection.train_test_split(bz_list, bz_labels, train_size=0.8,test_size=0.2, random_state=10)
  bz_train, bz_val, bz_train_labels, bz_val_labels = model_selection.train_test_split(bz_train, bz_train_labels, train_size=0.75,test_size=0.25, random_state=10)
  #random.shuffle(cc_list)
  #random.shuffle(bz_list)
  #cc_train = cc_list[:int(len(cc) * 0.6)]
  #cc_val = cc_list[int(len(cc) * 0.6):int(len(cc) * 0.8)]
  #cc_test = cc_list[int(len(cc) * 0.8):]
  print("bz train: ", bz_train)
  print("bz val: ", bz_val)
  print("bz test: ", bz_test)
  
def main():
  train_test_split("/home/lab/dillery/images/")

if __name__ == '__main__':
    main()

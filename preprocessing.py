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
  #cc_labels = np.ones(len(cc_list))
  #bz_labels = np.ones(len(bz_list))
  
  # create train/val/test subsets in [0.6:0.2:0.2] ratio using scikit
  #cc_train, cc_test, cc_train_labels, cc_test_labels = model_selection.train_test_split(cc_list, cc_labels, train_size=0.8,test_size=0.2, random_state=10)
  #cc_train, cc_val, cc_train_labels, cc_val_labels = model_selection.train_test_split(cc_train, cc_train_labels, train_size=0.75,test_size=0.25, random_state=10)
  cc_train, cc_test= model_selection.train_test_split(cc_list, train_size=0.8,test_size=0.2, random_state=10)
  cc_train, cc_val = model_selection.train_test_split(cc_train, train_size=0.75,test_size=0.25, random_state=10)
  
  bz_train, bz_test = model_selection.train_test_split(bz_list, train_size=0.8,test_size=0.2, random_state=10)
  bz_train, bz_val = model_selection.train_test_split(bz_train, train_size=0.75,test_size=0.25, random_state=10)
  
  #print("bz train: ", bz_train)
  #print("bz val: ", bz_val)
  #print("bz test: ", bz_test)
  
  return cc_train, cc_val , cc_test , bz_train, bz_val, bz_test
  
def copytree(src, dst, symlinks=False, ignore=None):
  for item in os.listdir(src):
      s = os.path.join(src, item)
      d = os.path.join(dst, item)
      if os.path.isdir(s):
          shutil.copytree(s, d, symlinks, ignore)
      else:
          shutil.copy2(s, d)
          
def main():
  #train_test_split("/home/lab/dillery/images/")
  cc_train, cc_val , cc_test , bz_train, bz_val, bz_test = train_test_split("/images")
  os.makedirs("/images/cc/train")
  os.mkdir("/images/cc/test")
  os.mkdir("/images/cc/val")
  for file in cc_train:
      copytree("/images/" + file, "/images/cc/train/")
  for file in cc_val:
      copytree("/images/" + file, "/images/cc/val/")
  for file in cc_test:
      copytree("/images/" + file, "/images/cc/test/")
  for file in bz_train:
      copytree("/images/" + file, "/images/bz/train/")
  for file in bz_val:
      copytree("/images/" + file, "/images/bz/val/")
  for file in bz_test:
      copytree("/images/" + file, "/images/bz/test/")

if __name__ == '__main__':
    main()

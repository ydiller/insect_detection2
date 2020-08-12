import os
import shutil
import numpy as np
import sklearn.model_selection as model_selection
import random

# A method creates lists of the data splitted to train/val/test in [0.8:0.2:0.2] ratio
def train_test_split(dir_path):
  cc_list=[]
  bz_list=[]
  for root,dirs,files in os.walk(dir_path):
    for dir in dirs:
      if "cc" in dir:
        cc_list.append(dir)
      if "bz" in dir:
        bz_list.append(dir)

  cc_train, cc_test= model_selection.train_test_split(cc_list, train_size=0.8,test_size=0.2, random_state=10)
  cc_train, cc_val = model_selection.train_test_split(cc_train, train_size=0.75,test_size=0.25, random_state=10)
  
  bz_train, bz_test = model_selection.train_test_split(bz_list, train_size=0.8,test_size=0.2, random_state=10)
  bz_train, bz_val = model_selection.train_test_split(bz_train, train_size=0.75,test_size=0.25, random_state=10)
 
  return cc_train, cc_val , cc_test , bz_train, bz_val, bz_test

# An implementation of the shutil.copytree function that works with multiple copies to the same directory
def copytree(src, dst, symlinks=False, ignore=None):
  for item in os.listdir(src):
      s = os.path.join(src, item)
      d = os.path.join(dst, item)
      if os.path.isdir(s):
          shutil.copytree(s, d, symlinks, ignore)
      else:
          shutil.copy2(s, d)

def main():
  cc_train, cc_val , cc_test , bz_train, bz_val, bz_test = train_test_split("/images")
  os.makedirs("/images/cc/train")
  os.mkdir("/images/cc/test")
  os.mkdir("/images/cc/val")
  os.makedirs("/images/bz/train")
  os.mkdir("/images/bz/test")
  os.mkdir("/images/bz/val")
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

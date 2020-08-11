import os
import shutil
import numpy as np

def train_test_split(dir_path):
  cc_list=[]
  bz_list=[]
  for dir in os.walk(dir_path):
    if "cc" in dir:
      cc_list.append(dir)
    if "bz" in dir:
      bz_list.append(dir)
  
  print(cc_list)
  
def main():
  train_test_split("images")

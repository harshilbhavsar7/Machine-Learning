import os
from pathlib import Path
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--src', type=str, help='Source')
parser.add_argument('-d', '--des', type=str, help='Destination')

   

args = parser.parse_args()

# srcdir=r"D:\Infomize\AI\Annotations\table\Combined_new_table\JPEGImages"
# desdir=r"D:\Infomize\AI\Annotations\table\Combined_new_table\Main"
srcdir=args.src
desdir=args.des
print(srcdir)
print(desdir)
files = os.listdir(srcdir)
# print(len(files))
# print(type(files))
# print(files[0])
files_shuffled=random.sample(files,len(files))
print(len(files_shuffled))
print(type(files_shuffled))

train,test,val = 0.8,0.1,0.1
with open(desdir+'/train.txt','a') as f:
    train_num = int(train*len(files))
    for i in files[:train_num]:
        f.write(os.path.splitext(i)[0]+'\n')

with open(desdir+'/test.txt','a') as f:
    test_num = int(test*len(files))
    for i in files[train_num:train_num+test_num]:
        f.write(os.path.splitext(i)[0]+'\n')
        
with open(desdir+'/val.txt','a') as f:
    val_num = int(val*len(files))
    for i in files[train_num+test_num:train_num+test_num+val_num]:
        f.write(os.path.splitext(i)[0]+'\n')


print('Train Files :::: {}'.format(train_num))
print('Test Files :::: {}'.format(test_num))
print('Validation Files :::: {}'.format(val_num))
print('Total :::: {}'.format(len(files)))

srcdir = 'C:/Users/rajes/Desktop/dhruv/combined_template_table/data'



import os
import shutil
'''
def rename(file,newfile):
    shutil.copy(os.path.join(srcdir,file),desdir)
    os.rename(os.path.join(desdir,file),os.path.join(desdir,newfile))
'''
'''
des=''    
os.makedirs('C:/Users/rajes/Desktop/dhruv/table_data')
for i, file in enumerate(sorted(os.listdir(srcdir))):
    if file.endswith('.jpg'):
        desdir = 'C:/Users/rajes/Desktop/dhruv/table_data/JPEGImages/'
        for j in range(num):
            rename(file,'dataset_{}_{}.jpg'.format(i,j))
    elif file.endswith('.xml'):
        desdir = 'C:/Users/rajes/Desktop/dhruv/table_data/Annotations/'
        for j in range(num):
            rename(file,'dataset_{}_{}.xml'.format(i-1,j))
'''
'''
maindir = 'C:/Users/rajes/Desktop/dhruv/table_data/Main/'            
with open(os.path.join(maindir,'tableval.txt'),'a') as f:            
    for i in sorted(os.listdir(desdir))[80:]:
        f.write(i)
        f.write('/n')
with open(os.path.join(maindir,'test.txt'),'a') as f:
    for i in sorted(os.listdir(desdir))[:80]:
        f.write(i)
        f.write('/n')
'''    
des='C:/Users/rajes/Desktop/dhruv/combined_template_table/combined_data'  
if not os.path.exists(des):  
    os.makedirs(des)
for file in os.listdir(srcdir):
    if file.endswith('.xml'):
        desdir = 'C:/Users/rajes/Desktop/dhruv/combined_template_table/combined_data/Annotations'
        if not os.path.exists(desdir):
            os.makedirs(desdir)
        shutil.copy(os.path.join(srcdir,file),desdir)
    elif file.endswith('.jpg'):
        desdir = 'C:/Users/rajes/Desktop/dhruv/combined_template_table/combined_data/JPEGImages'
        if not os.path.exists(desdir):
            os.makedirs(desdir)
        shutil.copy(os.path.join(srcdir,file),desdir)
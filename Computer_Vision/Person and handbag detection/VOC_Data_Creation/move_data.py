import os
import shutil
src = r'D:\Harshil\My_work\ML\Projects\P_H_Object_detection\test_data'
des=r'D:\Harshil\My_work\ML\Projects\P_H_Object_detection\VOC\annot_data'
# src2=r'D:\Harshil\My_work\ML\Projects\P_H_Object_detection\test_data'

for i in os.listdir(des):
    try:
        shutil.copy(src+'/'+i.replace('.xml','.jpg'),des)
    except:
        print(i)
    #/105_unsere Bestellung Nr.jpg
    #114_Nyrstar PO 4501847538_09.01.2020_HS172529616_1HE_2
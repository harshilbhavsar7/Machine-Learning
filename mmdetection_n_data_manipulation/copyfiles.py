import os
import shutil
src = r'D:\Infomize\AI\Annotations\For_training\17-Nov\data\VOCdevkit\VOC2007\\JPEGImages'
des=r'D:\Infomize\AI\Annotations\For_training\17-Nov\data\VOCdevkit\VOC2007\\def_des'
src2=r'D:\Infomize\AI\Annotations\For_training\17-Nov\data\VOCdevkit\VOC2007\\New_image'

for i in os.listdir(des):
    try:
        shutil.move(src+'/'+i.replace('.xml','.jpg'),src2)
    except:
        print(i)
    #/105_unsere Bestellung Nr.jpg
    #114_Nyrstar PO 4501847538_09.01.2020_HS172529616_1HE_2
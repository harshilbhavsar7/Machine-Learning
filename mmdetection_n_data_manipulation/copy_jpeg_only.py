import os,shutil

srcdir=r"D:\Infomize\AI\Annotations\30-Oct-2020\table\useless\21_tnh_data\VOCdevkit\VOC2007\Annotations"
for element in os.listdir(srcdir):
		# src2=os.listdir(os.path.join(srcdir,file))
		# for element in src2:
			if element.endswith('.xml'):
					#print('dssnbhdlv')
					# desdir = r'D:\Infomize\AI\Annotations\table\test_anjali\Annotations'
					# if not os.path.exists(desdir):
					# 	os.makedirs(desdir)
					# shutil.copy(os.path.join(os.path.join(srcdir,file+"/images"),element),desdir)
					desdir = r'D:\Infomize\AI\Annotations\30-Oct-2020\table\useless\21_tnh_data\VOCdevkit\VOC2007\JPEGImages'
					# if not os.path.exists(desdir):
					# 	os.makedirs(desdir)
					try:
						#print('bhkjfskj')
						shutil.copy(os.path.join(srcdir,os.path.splitext(element)[0]+'.jpg'),desdir)
						shutil.copy(os.path.join(srcdir,element),desdir)
						print(element)
					except:
						print('exception',element)
				


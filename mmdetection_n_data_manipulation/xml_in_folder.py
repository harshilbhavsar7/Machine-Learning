import os,shutil

srcdir=r"D:\Infomize\AI\Annotations\entities\test"
for file in os.listdir(srcdir):
	try:
		src2=os.listdir(os.path.join(srcdir,file))
		for element in src2:
			if element.endswith('.xml'):
				desdir = r'D:\Infomize\AI\Annotations\entities\test2\Annotations'
				if not os.path.exists(desdir):
					os.makedirs(desdir)
				shutil.copy(os.path.join(os.path.join(srcdir,file),element),desdir)
				desdir = r'D:\Infomize\AI\Annotations\entities\test2\JPEGImages'
				if not os.path.exists(desdir):
					os.makedirs(desdir)
				shutil.copy(os.path.join(os.path.join(srcdir,file),os.path.splitext(element)[0]+'.jpg'),desdir)
			'''
			if element.endswith('.jpg'):
				desdir = r'D:\Infomize\AI\Annotations\table\test\JPEGImages'
				if not os.path.exists(desdir):
					os.makedirs(desdir)
				shutil.copy(os.path.join(os.path.join(srcdir,file+"/images"),element),desdir)		
			'''
	except:
		print(file)
				
				


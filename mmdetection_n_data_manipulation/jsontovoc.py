import os
import json


srcfolder = r'D:\Infomize\AI\Annotations\entities\test'

for pos in os.listdir(srcfolder):
	srcfile = os.path.join(srcfolder+'/'+pos,'annotations.json')
	with open(srcfile,'r') as f:
		data = json.load(f)
	# print(data)
	classfile = os.path.join(srcfolder+'/'+pos,'classes.json')
	with open(classfile,'r') as f:
		_classes = json.load(f)
	# print(len(_classes))

	classes = {}s
	for c in _classes:
		classes[c['id']]=c['name']

	print(classes)
	
	for element in data:
		desfile= os.path.splitext(element)[0]+'.xml'
		desdir = os.path.join(srcfolder+'/'+pos+'/images',desfile)
		with open(desdir,'w') as f:
			content = '''<annotation>
				<folder>images</folder>
				<filename>{}</filename>
				<path>{}</path>
				<source>
					<database>Unknown</database>
				</source>
				<size>
					<width>{}</width>
					<height>{}</height>
					<depth>3</depth>
				</size>
				<segmented>0</segmented>
			'''

			f.write(content.format(element,element,2000,2000))
			for j in data[element]:
				try:
					content = '''
					<object>
						<name>{}</name>
						<pose>Unspecified</pose>
						<truncated>0</truncated>
						<difficult>0</difficult>
						<bndbox>
							<xmin>{}</xmin>
							<ymin>{}</ymin>
							<xmax>{}</xmax>
							<ymax>{}</ymax>
						</bndbox>
					</object>
					'''

					x1 = j['points']['x1']
					x2 = j['points']['x2']
					y1 = j['points']['y1']
					y2 = j['points']['y2']
					label = classes[j['classId']]
					f.write(content.format(label,int(x1),int(y1),int(x2),int(y2)))
				except:
					print(element)
			f.write('\n\n</annotation>')


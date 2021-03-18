import os
import json


srcfolder = r'D:\Infomize\AI\test'
classes = {'table':[],'cell':[],'description':[],'CustomerName':[],'SupplierName':[],'DeliveryAddressName':[],'DeliveryAddressDivision':[],'DeliveryAddressStreet':[],'DeliveryAddressCity':[],'DeliveryAddressPostalCode':[],'DeliveryAddressCountry':[],'CustomerVATNumber':[],'OrderReference':[],'OrderDate':[],'Currency':[],'CustomerStreet':[],'CustomerCity':[],'CustomerPostalCode':[],'CustomerCountry':[],'SupplierStreet':[],'SupplierCity':[],'SupplierPostalCode':[],'SupplierCountry':[],'PurchaserContactName':[],'PurchaserContactEmail':[],'PurchaserContactPhone':[],'Class 1':[],'HeaderRemarks2':[],'HeaderRemarks 1':[],'HeaderRequestedDeliveryDate':[],'TotalOrderValue':[]}

for pos in os.listdir(srcfolder):
	# srcfile = os.path.join(srcfolder+'/'+pos,'annotations.json')
	# with open(srcfile,'r') as f:
	# 	data = json.load(f)
	# # print(data)
	print(pos)
	classfile = os.path.join(srcfolder+'/'+pos,'classes.json')
	with open(classfile,'r') as f:
		_classes = json.load(f)
	# print(len(_classes))

	classes2 = dict.fromkeys([])
	for c in _classes:
		# print(c['id'])
		# print(c['name'])
		name = c['name']
		name_id = c['id']
		value = classes[name]
		value.append(name_id)
		classes[name] = list(set(value))
		# classes[c['name']]=c['id']

for key,value in classes.items():
	print(key,value)
# print(classes)
from pycocotools.coco import COCO
import requests

# instantiate COCO specifying the annotations json path
coco = COCO(r'D:\Harshil\My_work\ML\Data\COCO Json\annotations_trainval\instances_val2017.json')
# coco = COCO(r'D:\Harshil\My_work\ML\Data\COCO Json\annotations\image_info_test-dev2017.json'))

# Specify a list of category names of interest
catIds = coco.getCatIds(catNms=['person','handbag'])
print(catIds)
# Get the corresponding image ids and images using loadImgs
imgIds = coco.getImgIds(catIds=catIds)
# print(len(imgIds))
images = coco.loadImgs(imgIds)
# print(len(images))
# print("all ok")
coco.download('test_data',imgIds)
# Save the images into a local folder
# for im in images:
#     img_data = requests.get(im['coco_url']).content
#     with open('test_data' + im['file_name'], 'wb') as handler:
#         handler.write(img_data)


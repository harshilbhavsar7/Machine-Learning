from pycocotools.coco import COCO
import requests
import os
import json

def modify_ids(self, images, annotations):
      """
      creates new ids for the images. I.e., reorganizes the ids and returns the dictionaries back
      images: list of images dictionaries
      imId_counter: image id starting from one (each dicto will start with id of last json +1)
      """
      print("Reinitialicing images and annotation IDs ...")
      ### Images
      old_new_imgs_ids = {}  # necessary for the annotations!
      for n,im in enumerate(images)[:1]:
          old_new_imgs_ids[images[n]['id']] = n+1  # dicto with old im_ids and new im_ids
          print(old_new_imgs_ids[images[n]['id']])
          images[n]['id'] = n+1 # reorganize the ids
          print(images[n]['id'])
          break
      ### Annotations
      for n,ann in enumerate(annotations):
          annotations[n]['id'] = n+1
          old_image_id = annotations[n]['image_id']
          annotations[n]['image_id'] = old_new_imgs_ids[old_image_id]  # replace im_ids in the annotations as well
          break
      return images, annotations


coco = COCO(r'D:\Harshil\My_work\ML\Data\COCO Json\annotations_trainval\instances_val2017.json')
# coco = COCO(r'D:\Harshil\My_work\ML\Data\COCO Json\annotations\image_info_test-dev2017.json'))

catIds = coco.getCatIds(catNms=['person','handbag'])
imgIds = coco.getImgIds(catIds=catIds)
images = coco.loadImgs(imgIds)
print(images[0])

json_parent = r"D:\Harshil\My_work\ML\Projects\P_H_Object_detection\train_annotations.json"
imgs_ids = [x['id'] for x in images] # get img_ids of imgs with the category
# print(imgs_ids[0])
new_imgs = [x for x in coco.dataset['images'] if x['id'] in imgs_ids]
print("new_image_id",new_imgs[0])
### Filter annotations
new_annots = [x for x in coco.dataset['annotations'] if x['category_id'] in catIds]
print(new_annots[0])
## Reorganize the ids
# new_imgs, annotations = modify_ids(new_imgs, new_annots)
### Filter categories
new_categories = [x for x in coco.dataset['categories'] if x['id'] in catIds]
# print("new_categories: ", new_categories)
# data = {
#     "info": coco.dataset['info'],
#     "licenses": coco.dataset['licenses'],
#     "images": new_imgs, 
#     "annotations": new_annots,
#     "categories": new_categories 
#     }
# print("saving json: ")
# with open(json_parent, 'w') as f:
#     json.dump(data, f)

# Create a scoring file that loads and inferes from the model

import json
import numpy as np
import pickle
# import joblib
import base64
import logging
# logging.basicConfig(level=logging.DEBUG)
import logging.config

import os
from os import listdir
from os.path import isfile, join

from azureml.core.model import Model

import cv2
import base64
from imageio import imread
import io
import yaml

print("\n\n\nInstalling tesseract dependencies\n\n\n")
import sys
# os.system('pip install -U git+https://github.com/madmaze/pytesseract.git')
os.system('sudo apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config')
os.system('git clone https://github.com/tesseract-ocr/tesseract tesseract')
os.system('sudo apt install cmake -y')

print("\n\nRunning cmake...")
os.system("cd tesseract && mkdir build && cd build && cmake ..")
# os.system('! conda install -c conda-forge pytesseract -y')

print("\n\napt install tessaract-ocr ...")
os.system('apt install tesseract-ocr -y')
os.system('apt install libtesseract-dev -y')
os.system('pip install Pillow')
os.system('pip install pytesseract')
os.system('pip install pdf2image==1.7.1')
os.system('apt-get install poppler-utils')
os.system('pip install PyPDF2')
print("\n\n\nTesseract installation completed\n\n\n")

print("\n\n\n*************************************************00000******************")
print("**                        ********************00000*********************")
print("** COMPLETED SUCCESSFULLY *****************00000************************")
print("**                        **************00000***************************")
print("*************************************00000******************************")
print("***************00000**************00000*********************************")
print("******************00000********00000************************************")
print("*********************00000**00000***************************************")
print("************************000000******************************************\n\n\n")


import mmdet
from mmdet.apis import inference_detector, init_detector, show_result_pyplot

import mmdetection
from mmdetection.mmdet.apis import show_result

import urllib.request
from os import path

import torch, torchvision
print(torch.__version__, torch.cuda.is_available())

# Check MMDetection installation
import mmdet
print(mmdet.__version__)

# Check mmcv installation
from mmcv.ops import get_compiling_cuda_version, get_compiler_version
print(get_compiling_cuda_version())
print(get_compiler_version())

import custom_api
from custom_api.image_processing import rgbToString, stringToRGB
from custom_api.post_processing import post_processing, multi_post_processing
from custom_api.generate_ocr_roi import runOCR, runMultipleOCR
from custom_api.run_extraction import getData

from custom_api.changeResolution import getScale, changeResolution

import time

def init():
    global logger
    global model
    print("...............initializing.............")

    init_logger()
     # Get the path where the deployed model can be found.
    model_path = Model.get_model_path(model_name='epoch_36_default')
    # model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'sklearn_mnist_model.pkl')

    # urllib.request.urlretrieve("https://github.com/open-mmlab/mmdetection/blob/master/configs/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco.py", "mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco.py")
    # urllib.request.urlretrieve("https://open-mmlab.s3.ap-northeast-2.amazonaws.com/mmdetection/v2.0/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth", "mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth")


    # config_path = './mmdetection/configs/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco.py'
    config_path = './mmdetection/configs/hrnet/cascade_mask_rcnn_hrnetv2p_w32_20e_coco.py'
    # model_path = './mmdetection/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'
    # build the model from a config file and a checkpoint file
    # try:
    model = init_detector(config_path, model_path, device='cpu')
    model.CLASSES = ['table', 'cell', 'borderless']

    # except Exception as e:
        # print("**********Exception occured during init")
    print(".....initiate completed........")

def init_logger():
    global logger
    logconf = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.yml')
    print('logconf {}'.format(logconf))
    if os.path.exists(logconf):
        with open(logconf, 'rt') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        print('logconf loaded')
    else:
        logging.basicConfig(level=logging.DEBUG)
        print('logconf fall back to default')
    logger = logging.getLogger('score')

def run(data):
    logger.debug('***run method')
    logger.debug('raw_data: {}'.format(data))
    try:
        response = inference(data)
    except Exception as e:
        logger.debug('***run method EXCEPTION: {}'.format(e))
        response = str(e)
    return response

    # data = np.array(json.loads(json_data)['data']).astype('float32')
    # predictions = run_inference(data)
    # return json.dumps(predictions)
    # result = str(e)
    # return json.dumps({"Success": result})

def inference(raw_data):
    # logger.info('parse input json raw_data to get image')
    time_log = []

    start = time.process_time()
    try:
        parsed_json = json.loads(raw_data)
        raw_data = parsed_json['file']
        img_list = getData(raw_data)
        # in_img = stringToRGB(image_raw)
        in_imgs = img_list
    except Exception as e:
        err = json.dumps({"Status":"failed", "Message":"error at Input parsing, i.e. stringToRGB()", "Exception":str(e)})
        return err
    time_log.append({"Process":"stringToRGB", "Time":str(time.process_time() - start)})



    start = time.process_time()
    # run inference on input image
    pages = []
    try:
        for image in in_imgs:
            result = inference_detector(model, image)
            pages.append(Scan(result, image))
    except Exception as e:
        err = json.dumps({"Status":"failed", "Message":"error at inference_detector()", "Exception":str(e)})
        return err
    time_log.append({"Process":"inference_detector", "Time":str(time.process_time() - start)})



    start = time.process_time()
    # Post processing - 'Extract tabular structure'
    try:
        # output = post_processing(result, in_img)
        tables = multi_post_processing(pages)
    except Exception as e:
        err = json.dumps({"Status":"failed", "Message":"error at post_processing()", "Exception":str(e)})
        return err
    time_log.append({"Process":"post_processing", "Time":str(time.process_time() - start)})



    start = time.process_time()
    # Post processing - 'Run OCR on RoI regions'
    try:
        # ocr_roi = runOCR(output, in_img)
        ocr_roi = runMultipleOCR(tables)
    except Exception as e:
        err = json.dumps({"Status":"failed", "Message":"error at runOCR()", "Exception":str(e)})
        return err
    time_log.append({"Process":"runOCR", "Time":str(time.process_time() - start)})


    start = time.process_time()
    #changeResolution
    try:
        with open("pdf_file.pdf", "wb") as f:
            pdf = base64.b64decode(raw_data)
            f.write(pdf)

        pdf = open("pdf_file.pdf", 'rb')
        scale = getScale(in_imgs[0], pdf)
        final_data = changeResolution(scale, ocr_roi)
    except Exception as e:
        err = json.dumps({"Status":"failed", "Message":"error at changeResolution()", "Exception":str(e)})
        return err
    time_log.append({"Process":"changeResolution", "Time":str(time.process_time() - start)})
    

    # start = time.process_time()
#     '''Get Segmented image in return'''
#     # if hasattr(model, 'module'):
#     #  model = model.module
#     try:
#         out_image = model.show_result(in_img, result, score_thr=0.5)
#         time_log.append({'Process':'show_result', 'Time':str(time.process_time() - start)})
#         start = time.process_time()
#         '''Convert segmented image into byte64 string'''
#         # output_json = img2json(out_image)
#         base64_string = rgbToString(out_image)
#         time_log.append({'Process':'img2json', 'Time':str(time.process_time() - start)})
#     except Exception as e:
#         err = json.dumps({'Status':'failed', 'Message':'error at show_result() & img2json()', 'Exception':str(e)})
#         return err



    # resp = json.dumps({'message' : 'Success', 'result': ocr_roi, 'inference_image':base64_string})
    # json_resp = {'message' : 'Success', 'result': ocr_roi, 'inference_image':base64_string, 'time_logs':time_log}
    json_resp = {"Message" : "Success", "Result": final_data, "Time_logs":time_log}
    resp = json.dumps(json_resp)

    # return a JSON response.
    return resp

# Converts image into base64 encodings
def img2json(img):
    base64_string = rgbToString(img)
    data = {"result": base64_string}
    # output_data = json.dumps(data)
    # return output_data
    return data

# Document preprocessing and conversion script here.

class Scan:
    def __init__(self, result, image):
        self.result = result 	# inference result
        self.image = image 		# segmented image

# def segmentIt(model, result, img, score_thr):
# 	if hasattr(model, 'module'):
# 		model = model.module
# 	seg_img = model.show_result(img, result, score_thr=score_thr, show=False)
# 	cv2.imwrite("./test_output/infer_img_"+str(randint(111, 999))+".jpg", seg_img)
#         try:
#         out_image = model.show_result(in_img, result, score_thr=0.5)
#         time_log.append({'Process':'show_result', 'Time':str(time.process_time() - start)})
#         start = time.process_time()
#         '''Convert segmented image into byte64 string'''
#         # output_json = img2json(out_image)
#         base64_string = rgbToString(out_image)
#         time_log.append({'Process':'img2json', 'Time':str(time.process_time() - start)})
#     except Exception as e:
#         err = json.dumps({'Status':'failed', 'Message':'error at show_result() & img2json()', 'Exception':str(e)})
#         return err

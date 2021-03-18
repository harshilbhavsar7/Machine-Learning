from argparse import ArgumentParser
import requests
import base64
import json
import os
import time
# from custom.image_processing import stringToRGB
import cv2
# import deploy_api as ai     # To test the application without Flask server, i.e. for debugging purpose.

from PIL import Image
import base64
from imageio import imread
import io
import numpy as np


# parser = ArgumentParser()
# # parser.add_argument("-ip", "--ipaddress", help="ipaddress of the host system", type=str, required=False)

# # parser.add_argument("-fn", "--function", help="Which function to run (e.g.: local, api, file", type=str, required=False)
# parser.add_argument("-s", "--source", help="Enter PDF path in source argument.", type=str, required=False)
# args = parser.parse_args()
# # fn_id = args.function

ipaddress = '122.170.12.154'
port = '5000'
scoring_uri = 'http://'+ipaddress+":"+port+'/scan_pdf'
print(scoring_uri)
# filepath = "./test_output/Table_Testing/file4.pdf"
# filepath = args.source
filepath=r'C:\Users\Dell\Downloads\test\samples\Purchase Order_6148026_HS183821154_1HE.pdf'   
json_path = './api_output.json'

'''
This returns base64 string of the input file.
'''
def getPDFString(filepath):
    with open(filepath, "rb") as f:
        base64_bytes = base64.b64encode(f.read())
    base64_string = base64_bytes.decode('utf-8')
    # print(base64_string)
    return base64_string


def stringToRGB(base64_string):
    im = imread(io.BytesIO(base64.b64decode(base64_string)))
    cv2_img = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    return cv2_img


'''For deugging without Flask server'''
def runLocal(base64_string, flags):
    print('Running Local.....')
    ai.init()
    json_data = ai.run(base64_string, flags)
    writeResult(json_data, json_path)
    return json_data


def runAPI(base64_string, flags, parameters,scoring_uri ):
    print('Running API.....')
    data = {"file": base64_string, "flags":flags, "parameters" : parameters}
    # writeResult(data, './api_input.json')
    # exit()
    input_data = json.dumps(data)
    headers = { 'Content-Type':'application/json;charset=utf-8' }
    resp = requests.post(scoring_uri, input_data, headers = headers)
    results = resp.text
    obj = json.loads(results.encode('utf-8'))
    writeResult(obj, json_path)
    return obj

# Save output result
def writeResult(obj, file_path):
    with open(file_path, "w") as fp:
        json.dump(obj, fp, indent=4)


def readResult(json_path):
    f = open(json_path)
    obj = json.load(f)
    return obj


'''
debug-flag -> Enables debuggin, returns all log files(logs.txt)
test-flag -> Enables system testing. That is it returns all the processing data and its informations.
'''
flags = {
    "debug_logs":False,
    "test_data":True,
    "time_logs":True
}

parameters = {
    "threshold": 0.5,
    "origin": True
}

base64_string = getPDFString(filepath)

start = time.process_time()
# if fn_id=='local':
#     obj = runLocal(base64_string, flags)
# elif fn_id=='api':
#     obj = runAPI(base64_string, flags, scoring_uri)
# elif fn_id=='file':
#     obj = readResult(json_path)
# else:
#     print('Improper input. Please select from these: local/api/file')
#     exit()

obj = runAPI(base64_string, flags,parameters, scoring_uri )

print("Total API time: ", str(round((time.process_time() - start), 3))+"s")

# print(obj)
if obj['Status'] == 'Success':
    for n, data in enumerate(obj['Data']['Model_inference']):
        title = data['Class']
        pg_no = data['Page_no']
        seg_img = stringToRGB(data['Image'])
        new_img = cv2.resize(seg_img, (700, 1000))
        # cv2.imshow(title+'_'+str(pg_no), new_img)
        # cv2.waitKey(0)
        cv2.imwrite(title+'_'+str(n)+".jpg", seg_img)

    for n, img in enumerate(obj['Data']['Plot_data']):
        # cv2.imshow('Plot_img_'+str(n), stringToRGB(img))
        # cv2.waitKey(0)
        cv2.imwrite(str(n)+".jpg", stringToRGB(img))

    for n, img in enumerate(obj['Data']['Sort_data']):
        new_img = cv2.resize(stringToRGB(img), (700, 1000))
        # cv2.imshow('Sort_img'+str(n), new_img)
        # cv2.waitKey(0)
        cv2.imwrite(str(n)+".jpg", stringToRGB(img))

    # for tlog in obj['Time_log']:
    #     print(tlog['Process']+': '+str(tlog['Time'])+'s')


    print("\n")
    print("****************************************************00000***************")
    print("*************************************************00000******************")
    print("**                        ********************00000*********************")
    print("** COMPLETED SUCCESSFULLY *****************00000************************")
    print("**                        **************00000***************************")
    print("*************************************00000******************************")
    print("***************00000**************00000*********************************")
    print("******************00000********00000************************************")
    print("*********************00000**00000***************************************")
    print("************************000000******************************************")
    print("\n")
else:

    print('Message', obj['Message'])
    print('Exception', obj['Exception']) 

    print("\n")  
    print("                                                                      ")
    print("         OOO           PPPPPP        PPPPPP           SSSSS       !!  ")
    print("      OO     OO        PP    PP      PP    PP       SSS   SSS     !!  ")
    print("    OO         OO      PP     PP     PP     PP     SS             !!  ")
    print("   OO           OO     PP   PPP      PP   PPP       SSS           !!  ")
    print("   OO           OO     PPPPP         PPPPP            SSSS        !!  ")
    print("    OO         OO      PP            PP                  SSS      !!  ")
    print("      OO     OO        PP            PP                    SS     !!  ")
    print("         OOO           PP            PP            SSS   SSS          ")
    print("                                                     SSSSS        !!  ")
    print("                                                                      ")
    print("      Operation Failed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!              ")
    print("\n")


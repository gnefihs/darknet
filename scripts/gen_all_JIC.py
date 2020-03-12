#!/usr/bin/env python

'''
generates jsons all the sets and all txt files in image_detections dir
!!! image_list.py should be ran for the relevant sets first !!!
'''

# builtin 
from __future__ import absolute_import, division, print_function # for python2 and python3 compatibility
import os
import subprocess
import glob
import pdb

# third-party

# own mods

__author__ = "Linn of the Ded"
__status__ = "Production"

if __name__ == '__main__':
    parent_dir = "/media/yl/demo_ssd/raw_data/"

    # get the sets with the image_detections dir 
    det_dirs = glob.glob(parent_dir+'/*/*/log_high/*/image_detections')
    for det_dir in det_dirs:
        img_txts = glob.glob(det_dir+'/*.txt')
        for img_txt in img_txts:
            cam = os.path.basename(img_txt)[11:13] #FIXME: Must be of the name image_list_xx.txt
            print(img_txt)
            json_name = "results_"+cam+"_yolov3-tiny-prn-slim_best.weights.json"
            print(json_name)
            subprocess.call("../darknet detector test ../cfg/coco6.data ../cfg/yolov3-tiny-prn-slim.cfg ../yolov3-tiny-prn-slim_best.weights -ext_output -dont_show -out %s < %s.txt" % (json_name, img_txt))
            #print(img_txt) # DEBUG

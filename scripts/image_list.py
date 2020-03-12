#!/usr/bin/env python
# coding: utf-8

'''
 script for generating yolo results for the whole datasets' log high cameras
'''

from __future__ import absolute_import, division, print_function # for python2 and python3 compatibility
import os
from os import listdir, pardir


def get_dirs(parent_dir, label_dir_name, label_name='annotations.json'):
  labels_paths_v = []
  high_set_v = []
  labels_jsons_v=[]
  
  for root, dirs, files in os.walk(parent_dir):
    for i, dire in enumerate(dirs): # identify where sets are using the "pixor_test" directories
      if dire == label_dir_name:
        labels_dir=os.path.join(root,dire)
        low_set_dir= os.path.join(labels_dir, pardir) # location of the log_low set

        set_name =  root.split('/')[-1] # set name

        # loc of log_high set
        high_set_dir=os.path.join(low_set_dir, pardir) 
        high_set_dir=os.path.join(high_set_dir, pardir) 
        high_set_dir=os.path.join(high_set_dir, "log_high") 
        high_set_dir=os.path.join(high_set_dir, set_name) 
        
        # check if set dir has pcds and fused_poses

        set_contents = listdir(high_set_dir)
        if "fused_pose" in set_contents and "pcds" in set_contents:
#             print "found set", high_set_dir
          high_set_v.append(high_set_dir)
          labels_paths_v.append(labels_dir)
          is_found = False
          for file in listdir(labels_dir):
            if file.find(label_name) >= 0:
              labels_jsons_v.append(labels_dir+'/'+file)
              is_found = True
          if not is_found:
            raise ValueError("labels not found in label dir", labels_dir)

#   print "high hz sets paths: ", high_set_v
#   print "low hz labels paths:", labels_paths_v
#   print "low hz labels jsons:", labels_jsons_v

  return high_set_v, labels_jsons_v
 
def sf_create_list(img_dir, output_txt):
    img_list = os.listdir(img_dir)
    img_list = sorted(img_list)

    with open(output_txt,'w') as file:
        for img_file in img_list:
            file.write(img_dir+'/'+img_file+'\n')

if __name__ == '__main__':

    parent_dir = "/media/yl/demo_ssd/"
    cam_names=["a0","a1","a2","a3"]
    model_name="yolov3-tiny-prn-slim_best.weights"
    det_dir="image_detections"

    # obtain list of dirs
    set_v, labels_paths_v = get_dirs(parent_dir,"no_qc_tracking")
    t_set_v, t_labels_paths_v = get_dirs(parent_dir,"qced_eval")
    set_v += t_set_v
    labels_paths_v += t_labels_paths_v

    #print(set_v) # DEBUG
    #print("len of set_v: ", len(set_v)) # DEBUG

    for set_dir in set_v:
        # create directory
        det_path=os.path.join(set_dir,det_dir)
        if not os.path.exists(det_path): os.mkdir(det_path)

        # create txt file
        for cam in cam_names:
            imgs_txt = os.path.join(det_path,"image_list_"+cam+".txt")
            imgs_path=os.path.join(set_dir,cam+"_decoded")
            sf_create_list(imgs_path,imgs_txt)

    print("completed generation of list of images for log high sets wt labels under no_qc_tracking and qced_eval")

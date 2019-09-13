import os

IMG_DATA_DIR = "/home/sf/CETRAN_test_data/data800ms/image_416"
OUTPUT_FILENAME = "image_list.txt"
OUTPUT_DIR = os.getcwd() + "/" # default: current directory

img_list = os.listdir(IMG_DATA_DIR)

num_added = 0
with open(OUTPUT_DIR + OUTPUT_FILENAME,'w') as file:
    for img_file in img_list:
        file.write(IMG_DATA_DIR+'/'+img_file+'\n')
        num_added+=1
print("No. of image added to list: ", num_added)

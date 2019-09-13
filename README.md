### Requirements:
- CUDA 10.0
- openCV >= 2.4
- cuDNN >= 7.0

### Installation:
- Run `make`
- Download weights file:
    * [weights_file] (https://drive.google.com/open?id=1fcW2C9mqby9rmq2MsvdAtec8e32D41mZ)
    * put weights into darknet folder
- Generate a txt file of image paths:
    * open image_list.py
    * change the variables to where your data is located
    * change where you want to output your list of data
    * run it `python image_list.py`
- Detect and output json labels:
    * _Note: Specify your own path to your imagelist.txt file below:_
    * Run: `./darknet detector test cfg/coco6.data cfg/yolov3-tiny-prn-slim.cfg ./yolov3-tiny-prn-slim_best.weights -ext_output -dont_show -out result.json < path/to/imagelist.txt`
    * detection results stored in `result.json` (there's a sample `result.json` included)

### JSON Sample

```
[
{
 "frame_id":1, 
 "filename":"/home/sf/CETRAN_test_data/data800ms/image_416/416_image000396.png", 
 "objects": [ 
  {"class_id":2, "name":"car", "relative_coordinates":{"center_x":0.378704, "center_y":0.535480, "width":0.102729, "height":0.137796}, "confidence":0.814241}
 ] 
}, 
{
 "frame_id":2, 
 "filename":"/home/sf/CETRAN_test_data/data800ms/image_416/416_image000587.png", 
 "objects": [ 
  {"class_id":2, "name":"car", "relative_coordinates":{"center_x":0.283575, "center_y":0.491543, "width":0.057166, "height":0.074683}, "confidence":0.906936}, 
  {"class_id":5, "name":"truck", "relative_coordinates":{"center_x":0.283575, "center_y":0.491543, "width":0.057166, "height":0.074683}, "confidence":0.307862}, 
  {"class_id":2, "name":"car", "relative_coordinates":{"center_x":0.973572, "center_y":0.515436, "width":0.047881, "height":0.070896}, "confidence":0.895838}, 
  {"class_id":2, "name":"car", "relative_coordinates":{"center_x":0.511256, "center_y":0.468355, "width":0.047102, "height":0.045618}, "confidence":0.830094}, 
  {"class_id":2, "name":"car", "relative_coordinates":{"center_x":0.444033, "center_y":0.481993, "width":0.057871, "height":0.044429}, "confidence":0.823673}, 
  {"class_id":2, "name":"car", "relative_coordinates":{"center_x":0.165386, "center_y":0.542127, "width":0.129697, "height":0.122631}, "confidence":0.503820}, 
  {"class_id":2, "name":"car", "relative_coordinates":{"center_x":0.606268, "center_y":0.473540, "width":0.062646, "height":0.038024}, "confidence":0.306950}
 ] 
}]
```






import cv2
import imutils
import numpy as np 
import os 
# file path for input images 
input_dir_path = "./lol"

# file path for output images
output_dir_path = "./loop"

# listdown all input images in input images path 
input_dir_list = os.listdir(input_dir_path)

# 
for img_name in input_dir_list:
    
    image_name = input_dir_path+"/"+img_name
    image = cv2.imread(image_name)
    # rotate at angle 315
    rotated = imutils.rotate_bound(image, 315)
    # write all images at output directory
    cv2.imwrite(os.path.join(output_dir_path , img_name), rotated)
    #cv2.imshow("Rotated (Problematic)", rotated)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
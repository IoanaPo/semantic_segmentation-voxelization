
# coding: utf-8

# In[10]:


import cv2
import matplotlib.pyplot as plt
import os
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import numpy as np


# In[42]:


def make_video(images, outimg=None, fps=5, size=None,
               is_color=True, format="XVID"):
    """
    Create a video from a list of images.
 
    @param      outvid      output video
    @param      images      list of images to use in the video
    @param      fps         frame per second
    @param      size        size of each frame
    @param      is_color    color
    @param      format      see http://www.fourcc.org/codecs.php
    @return                 see http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
 
    The function relies on http://opencv-python-tutroals.readthedocs.org/en/latest/.
    By default, the video will have the size of the first image.
    It will resize every image to this size before adding them to the video.
    """
    
    fourcc = VideoWriter_fourcc(*format)
    vid = None
    for image in images:
        if not os.path.exists(image):
            raise FileNotFoundError(image)
        img = cv2.flip(cv2.imread(image),1)
        #img = imread(image)
        if vid is None:
            if size is None:
                size = img.shape[1], img.shape[0]
            vid = VideoWriter('final_horsejump.avi', fourcc, float(fps), size, is_color)
        if size[0] != img.shape[1] and size[1] != img.shape[0]:
            img = resize(img, size)
        vid.write(img)
    vid.release()
    return vid


# In[43]:


directory = r'C:\Users\ipoliceanu\Desktop\horsejump-high'
#for .jpg files
#number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item)) and item.endswith('.jpg')])

#for .png files
number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item)) and item.endswith('.png')])

my_list = []
for each_file in range(number_of_files):
    my_list.append(os.path.join(directory, os.listdir(directory)[each_file]))
#print lista

myvid = make_video(my_list)


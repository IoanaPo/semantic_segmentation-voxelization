
# coding: utf-8

# In[39]:


get_ipython().run_line_magic('matplotlib', 'inline')
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import glob
import errno
import shutil


# In[62]:


# import the image and the mask
img = cv2.imread('C:/Users/ipoliceanu/Documents/MATLAB/DAVIS/JPEGImages/1080p/horsejump-high/00000.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#replace white with purple in the mask
mask = cv2.imread('C:/Users/ipoliceanu/Documents/MATLAB/DAVIS/Results/Segmentations/480p/bvs/horsejump-high/00000.png')
new_mask = mask;
new_mask[:,:,1] -= 255


# In[63]:


# plot them
plt.figure(figsize=(11,5))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)

plt.subplot(1, 2, 2)
plt.imshow(new_mask)

plt.tight_layout()
plt.show()


# In[60]:


#create a directory in which to save the overimposed images
dirr = 'C:/Users/ipoliceanu/Pictures/'
ss_path = dirr + str('Sem_seg_horsejump-high/')
#start with a clean slate        
if os.path.exists(ss_path):
    shutil.rmtree(ss_path)   
    os.makedirs(ss_path)
else:
    try: 
        os.makedirs(ss_path)
    except OSError:
        if not os.path.isdir(ss_path):
            raise


# In[64]:


directory ='C:/Users/ipoliceanu/Documents/MATLAB/DAVIS/JPEGImages/1080p/horsejump-high/'
mask_directory = 'C:/Users/ipoliceanu/Documents/MATLAB/DAVIS/Results/Segmentations/480p/bvs/horsejump-high/'

for file in range(len(os.listdir(directory))):
    orig_img = cv2.resize(cv2.imread(os.path.join(directory, os.listdir(directory)[file])),(854,480))
    orig_img_rgb = cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB)
    foreground = orig_img_rgb.astype(float)
    
    #normalize the alpha mask to keep intensity between 0 and 1
    alpha = foreground.astype(float)/255
    
    #replace white with purple in the mask
    mask = cv2.imread(os.path.join(mask_directory, os.listdir(mask_directory)[file]))
    new_mask = mask;
    new_mask[:,:,1] -= 255
    background = new_mask.astype(float)
    
    # multiply the foreground with the alpha matte
    foreground = cv2.multiply(alpha, foreground)
    
    # multiply the background with ( 1 - alpha )
    background = cv2.multiply(1.0 - alpha, background)
    
    # add the masked foreground and background.
    outImage = cv2.add(foreground, background)/255
    
    ssfile = os.path.join(ss_path, os.listdir(directory)[file])
    plt.imsave(ssfile, outImage)


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def nib_read_img(path):
	import nibabel as nib # read and save medical images
	image_data = nib.load(path).get_data()
	return image_data
    

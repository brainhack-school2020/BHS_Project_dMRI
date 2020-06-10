#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Extract_b0_Image(input_Image, output_Image):
    "To run this, please first make sure you install fsl and can run it"
    "One method is that run fsl and thi pre-processing code in the same terminal"
    import nipype.interfaces.fsl as fsl
    fslroi = fsl.ExtractROI(in_file=input_Image,roi_file=output_Image,t_min=0, t_size=1)
    fslroi.run()


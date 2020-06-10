#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def interact_vol_plot(x,IntenseScale):
    "to create 3D  MRI figure with slider"
    import os #TO control directories
    import nibabel as nib # read and save medical images
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    #%matplotlib inline
    import plotly
    import plotly.express as px
    from ipywidgets import interact, interactive, fixed, interact_manual
    import ipywidgets as widgets
    from skimage import io #用于读取保存或显示图片或者视频
    
    import timeit #compute time, useage: timeit.timeit()
    import math
    import time
    import warnings
    import numpy as np
    
    import nipype.interfaces.fsl as fsl #topup
    from nipype.interfaces.fsl import TOPUP
    from nipype.interfaces.fsl import ApplyTOPUP
    from nipype.interfaces.fsl import Eddy
    from nipype.testing import anatfile
    
    from dipy.denoise.localpca import mppca #denoising
    from dipy.io import read_bvals_bvecs
    from dipy.core.gradients import gradient_table
    from dipy.reconst.dti import TensorModel
    from dipy.reconst.dti import fractional_anisotropy
    from dipy.reconst.dti import color_fa
    import dipy.reconst.dki as dki
    vol = x
    colormax = IntenseScale*vol.max()#获取最大array中的最大值，最后代表cmax
    volume = vol.T
    len(volume)
    r, c = volume[math.floor(len(volume)/2)].shape
    # Define frames
    import plotly.graph_objects as go
    nb_frames = len(volume)-1
    fig = go.Figure(frames=[go.Frame(
        data=go.Surface(
        z=(len(volume)-1 - k ) * np.ones((r, c)),
        surfacecolor=volume[len(volume)-1 - k],
        cmin=0, cmax=colormax
        ),
        name=str(k) # name the frame for the animation to behave properly
        )
        for k in range(nb_frames)])

    # Add data to be displayed before animation starts
    fig.add_trace(go.Surface(
        z=(len(volume)-1) * np.ones((r, c)),
        surfacecolor=volume[len(volume)-1],#np.flipud(volume[30]),
        colorscale='gray',
        cmin=0, cmax=colormax,
        colorbar=dict(thickness=20, ticklen=4)
        ))
    def frame_args(duration):
        return {
                "frame": {"duration": 500},# Duration can be used to change animate speed
                "mode": "immediate",
                "fromcurrent": True,
                "transition": {"duration": 500, "easing": "linear"},
            }

    sliders = [
                {
                    "pad": {"b": 10, "t": 60},
                    "len": 0.9,
                    "x": 0.1,
                    "y": 0,
                    "steps": [
                        {
                            "args": [[f.name], frame_args(0)],
                            "label": str(k),
                            "method": "animate",
                        }
                        for k, f in enumerate(fig.frames)
                    ],
                }
            ]

    # Layout
    fig.update_layout(
             title='Volume Slices Image',
             width=600,
             height=600,
             scene=dict(
                        zaxis=dict(range=[-1, len(volume)-1], autorange=False),
                        aspectratio=dict(x=1, y=1, z=1),
                        ),
             updatemenus = [
                {
                    "buttons": [
                        {
                            "args": [None, frame_args(50)],
                            "label": "&#9654;", # play symbol
                            "method": "animate",
                        },
                        {
                            "args": [[None], frame_args(0)],
                            "label": "&#9724;", # pause symbol
                            "method": "animate",
                        },
                    ],
                    "direction": "left",
                    "pad": {"r": 10, "t": 70},
                    "type": "buttons",
                    "x": 0.1,
                    "y": 0,
                }
             ],
             sliders=sliders
    )
    fig.show()


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def volume_plot(MD):
	# Import data
	import time
	import numpy as np

	from skimage import io #用于读取保存或显示图片或者视频
    import math
	vol = MD
	colormax = vol.max()#获取最大array中的最大值，最后代表cmax
	volume = vol.T
	len(volume)
	r, c = volume[math.floor(len(volume)/2)].shape
	# Define frames
	import plotly.graph_objects as go
	nb_frames = len(volume)-1

	fig = go.Figure(frames=[go.Frame(data=go.Surface(
	    z=(len(volume)-1 - k ) * np.ones((r, c)),
	    surfacecolor=volume[len(volume)-1 - k],
	    cmin=0, cmax=colormax
	    ),
	    name=str(k) # you need to name the frame for the animation to behave properly
	    )
	    for k in range(nb_frames)])

	# Add data to be displayed before animation starts
	fig.add_trace(go.Surface(
	    z=(len(volume)-1) * np.ones((r, c)),
	    surfacecolor=volume[len(volume)-1],#np.flipud(volume[30]),
	    #colorscale='Gray',
	    cmin=0, cmax=colormax,
	    colorbar=dict(thickness=20, ticklen=4)
	    ))


	def frame_args(duration):
	    return {
		    "frame": {"duration": duration},
		    "mode": "immediate",
		    "fromcurrent": True,
		    "transition": {"duration": duration, "easing": "linear"},
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
		 title='Slices in volumetric data',
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


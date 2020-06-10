#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def nib_show_img(img0,slices,intenseScale):
	import plotly
	import plotly.express as px
	img00=img0[:,:,slices]
	zmax0=img00.max()
	fig=px.imshow(img0[:,:,slices],color_continuous_scale="Viridis",zmin=0,zmax=zmax0*intenseScale/100,x=None, y=None,labels={},template="plotly_white")
	fig.update_xaxes(showticklabels=False)
	fig.update_yaxes(showticklabels=False)
	fig.update_layout(coloraxis_showscale=False)
	fig.show()


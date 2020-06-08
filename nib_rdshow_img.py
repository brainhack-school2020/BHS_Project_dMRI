#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def nib_rdshow_img(path,xslice,intenseScale):
    warnings.filterwarnings('ignore')
    image_data = nib.load(path).get_data()
    img00=image_data[:,:,xslice]
    zmax0=img00.max()
    fig=px.imshow(image_data[:,:,xslice],color_continuous_scale="Viridis",                  zmin=0,zmax=zmax0*intenseScale/100,                  labels={},template="plotly_white")
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    fig.update_layout(coloraxis_showscale=False)
    fig.show()


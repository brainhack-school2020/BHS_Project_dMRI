#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def nib_rdshow_img(Images,Slices,IntenseScale,TitleImg):
    'Images: data path; Slices: which slice you want to see; IntenseScale: to percentage of the highest color strength'
    "TitleImg:image title, for example:'a test title'"
    import nibabel as nib # read and save medical images
    import warnings
    import plotly
    import plotly.express as px
    warnings.filterwarnings('ignore')
    image_data = nib.load(Images).get_data()
    img00=image_data[:,:,Slices]
    zmax0=img00.max()
    fig=px.imshow(image_data[:,:,Slices],color_continuous_scale="Viridis",              zmin=0,zmax=zmax0*IntenseScale/100,\
                  labels={},template="plotly_white")
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    fig.update_layout(coloraxis_showscale=False)
    fig.update_layout(title=TitleImg)
    fig.show()

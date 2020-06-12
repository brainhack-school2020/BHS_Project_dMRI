[![](https://img.shields.io/badge/Visit-our%20project%20page-ff69b4)](https://school.brainhackmtl.org/project/template)

# Diffusion MRI reconstruction project

Team contributors: Erjun Zhang, Brainhack Shool 2020

<div align="left">
<img src="https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/bhs2020.png" title="Brainhack School" width=500>
</div>

## Summary 

This project is about diffusion magnetic resonance (MR) data processing and analyzation. It maily consists of three part: brain diffusion MR data preprocessing, diffusion MR images reconstrution, data visualization and left and right hemispherical preprocessed MR images classification. The whole processures can be found in [this Jupyter Notebook file](https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/dMRI%20Reconstruction%20Project.ipynb). Explainations about processures results and other details are given in it.

With reproducibility being a primary concern, this project was completed by using open-source softwares/tools (Python, FSL, DIPYPE...) and dataset (dHCP and PRIME). It can be as a simple tutorial/example for new students in neuroscience (diffusion MR brain imaging) to familar/start with their further neuroscience study. 

## Project definition 

### Background

Low blood sugar is a common problem in both children and adults. Existing research showed that it may lead to serious both transient and permanent structural abnormalities on brains. Magnetic resonance imaging (MRI), specially diffusion MRI, has a higher in vivo sensitivity to lesions in soft tissues compared to other imaging modalities, and has potential to identify and quantify brain structure changes. Some of this changes are not appraient enough,even for expericed experts. Machine learning is an useful mehtod to discover potencial features. 

Currently, there are some open-source softwares to reconstruct and analysis diffusion MRI data. However, only use these tools, one, like me as a new student in this field, may get confused about operations and principle behind them. This seriously stops people to reach their long-term goals in their diffusion MRI project. 

Thus, I began this project to preprocess  dMRI data, reconstruct diffusion MR images and do some analysis by using machine learning. The goals are as following:

* Get preprocessed diffusion MR images from raw data;
* Reconstruct diffusion tensor images from the preprocessed data;
* By using machine learning, try to classify two hemispherical brain from preprocessed diffusion images.

### Tools 

The "Diffusion MRI reconstruction project" will rely on the following tools: 
 * Python3: coding language used to complete this project (Python2 also needed for some special packages).
 * Github and git: to organize this project and make version control
 * Jupyter Notebook: to file code, visualizations and results 
 * [Markdown](https://guides.github.com/features/mastering-markdown/), to structure the text in README and Jupyter Notebook
 * Visual Studio Code: to be code editor
 * Nipype: to use FSL command preprocessing  image data
 * DIPY: to be used as diffuison tensor imaging (DTI) fitting and denoising
 * matplotlib, plotly and ipython widgets: data visualization
 * Linux (Ubuntu 20.04)



### Data 

This project used data from online dataset offered by:
1. [The Developing Human Connectome Project](http://www.developingconnectome.org/second-data-release/). It consists of over 800 neonatal scans and over 250 fetal scans and can be used to data analysis after image reconstruction. 
2. [PRIME](http://fcon_1000.projects.nitrc.org/indi/PRIMEdownloads.html): used this dataset to reconstruct diffusion Images. 
3. Since during preprocessing, we used epi data with two oposite phase-encoding directions to correct distortions, other data can also be used as the source data if meet this requiement.

### Deliverables

At the end of this project, we will have: Jupyter notebook will be developted, allowing diffusion MR reconstrution and data analyzation. Weekly Deliverables are as following:
 
 - Week 1: [Assiginment 2](https://github.com/zhangerjun/Zhang-EJ-QLS612)
 - Week 2: [README file](https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/README.md)
 - Week 3: [Data visualization](https://github.com/brainhack-school2020/BHS_Project_dMRI/tree/master/Visualization)
 - Week 4: [Project report]()
 
## Method
1. Preprocessing: TOPUP flow chart
<div align="center">
	<img src="https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/Fig/TOPUP_FlowChart.png" width="600" alt="1" title="Preprocessing: TOPUP flow chart">
</div>

## Results 

1. Data Visulization (see [gif figure](https://github.com/brainhack-school2020/BHS_Project_dMRI/tree/master/Visualization) below):
  - 3D volume slices image 
  - Interactive widgets use to show preprocess results 
  - Interactive widgets use to shwo reconstruction results 
<div align="center">
	<img src="https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/Visualization/VolumeSlicesImg.gif" width="300" alt="1" title="3D volume slices image">
	<img src="https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/Visualization/Preprocessing.gif" width="300" title="Interactive widgets use to show preprocess results">	
	<img src="https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/Visualization/ReconstructedImg.gif" width="300" title="Interactive widgets use to show reconstruction results">
</div>
2. Preprocessing results

<div align="center">
	<img src="https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/Fig/PreproResults.png" width="650" alt="1" title="DTI Results">
</div>

3. DTI results

<div align="center">
	<img src="https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/Fig/DTI_Results.png" width="800" alt="1" title="DTI Results">
</div>


### Progress overview

Formating final project file...
## What I have leraned
1. Python
	* FSL, Nipype.interfaces, DIPY
	* matplotlib, plotly, ipywidgets
	* Function definition and calling
2. Markdown
	* Format this README file
	* Insert figures and animation
	* LaTex to edit mathsmatical equations
3. Github
	* Version control
	* Project ogernization
4. Jupter notebook
5. Found and learnt to use some small but useful tools
	* [Peek](https://github.com/phw/peek) for GIF making
	* [Gedit](https://wiki.gnome.org/Apps/Gedit) to edit code or markdown
6. Medical file format (NII) and data structure (BIDS)
7. Statistical method and machine learning

## Dependencies

* Operation system: I use Linux (Ubuntu 20.04) to complete this project.
* Python: both Python2 and Python3 were used in this project.
* Jupter and jupyterlab are needed to run jupyter notebooks in this project.
* Dipy (https://dipy.org/)
* Nipype (http://miykael.github.io/nipype-beginner-s-guide/installation.html)
* FSL (https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSL). I installed FSL6.0 based on python2 following FslInstallation/Linux (https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation/Linux) and FslInstallation/ShellSetup. In addtion, update Fsl-core is recommended.
* NeuroDebian: To facilitate FSL and Nipype, NeuroDebian is need to be installed. I installed it following http://neuro.debian.net/.
* AMICO (https://github.com/daducci/AMICO)



## Conclusion and acknowledgement

TBD

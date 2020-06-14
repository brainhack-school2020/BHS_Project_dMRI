[![](https://img.shields.io/badge/Visit-our%20project%20page-ff69b4)](https://school.brainhackmtl.org/project/template)

# Diffusion MRI reconstruction project

Team contributors: Erjun Zhang, Brainhack School 2020

<div align="left">
<img src="https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/bhs2020.png" title="Brainhack School" width=500>
</div>

## Summary 

This project is about diffusion magnetic resonance (MR) data processing and analysis. It mainly consists of three parts: brain diffusion MR data preprocessing, diffusion MRI images reconstruction, data visualization and left and right hemispherical preprocessed MR images classification. The whole procedures can be found in [this Jupyter Notebook file](https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/dMRI%20Reconstruction%20Project.ipynb). Explanations about procedures results and other details are given in it.

With reproducibility being a primary concern, this project was completed by using open-source softwares/tools (Python, FSL, DIPYPE...) and dataset (dHCP and PRIME). It can be as a simple tutorial/example for new students in neuroscience (diffusion MR brain imaging) to familiar/start with their further neuroscience study. 

## Project definition 

### Background

Low blood sugar is a common problem in both children and adults. Existing research showed that it may lead to serious both transient and permanent structural abnormalities on brains. Magnetic resonance imaging (MRI), specially diffusion MRI, has a higher in vivo sensitivity to lesions in soft tissues compared to other imaging modalities, and has potential to identify and quantify brain structure changes. Some of these changes are not appraient enough,even for experienced experts. Machine learning is a useful method to discover potential features. 

Currently, there are some open-source softwares to reconstruct and analyze diffusion MRI data. However, only using these tools, one, like me as a new student in this field, may get confused about operations and principle behind them. This seriously stops people to reach their long-term goals in their diffusion MRI project. 

Thus, I began this project to preprocess  dMRI data, reconstruct diffusion MR images and do some analysis by using machine learning. The goals are as following:

* **Data Preprocesssing** Get preprocessed diffusion MR images from raw MRI data;
* **Image Reconstruction** Reconstruct diffusion tensor images from the preprocessed data;
* **Machine Learning Classsification** By using machine learning, randomly choose left or right hemispheres on each slice of MRI images preprocessed above and find method to give results that which part it is belonging to (right or left?). 

### Tools 

The "Diffusion MRI reconstruction project" will rely on the following tools: 
 * Python3: coding language used to complete this project (Python2 also needed for some special packages).
 * Github and git: to organize this project and make version control
 * Jupyter Notebook: to file code, visualizations and results 
 * [Markdown](https://guides.github.com/features/mastering-markdown/), to structure the text in README and Jupyter Notebook
 * Visual Studio Code: to be code editor
 * Nipype: to use FSL command preprocessing  image data
 * DIPY: to be used as diffusion tensor imaging (DTI) fitting and denoising
 * matplotlib, plotly and ipython widgets: data visualization
 * Linux (Ubuntu 20.04)



### Data 

This project used data from online dataset offered by:
1. [The Developing Human Connectome Project](http://www.developingconnectome.org/second-data-release/). It consists of over 800 neonatal scans and over 250 fetal scans and can be used for data analysis after image reconstruction. 
2. [PRIME](http://fcon_1000.projects.nitrc.org/indi/PRIMEdownloads.html): used this dataset to reconstruct diffusion Images. This also can be downloaded [here](https://drive.google.com/file/d/1zgxynxjUCETBC6MAl4rfh0sL0WhFtKA9/view?usp=sharing) directly. 
3. Since during preprocessing, we used epi data with two opposite phase-encoding directions to correct distortions, other data can also be used as the source data if it meets this requirement.
4. Data used for analysis is generated from image data after preprocessing. The final data can be found in this [github project folder](https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/brain_water.csv).

### Deliverables

At the end of this project, we will have: Jupyter notebook will be developed, allowing diffusion MR reconstruction and data analyzation. Weekly Deliverables are as following:
 
 - Week 1: [Assignment 2](https://github.com/zhangerjun/Zhang-EJ-QLS612)
 - Week 2: [README file](https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/README.md)
 - Week 3: [Data visualization](https://github.com/brainhack-school2020/BHS_Project_dMRI/tree/master/Visualization)
 - Week 4: [Project report](https://github.com/brainhack-school2020/BHS_Project_dMRI) and [project prosentation](https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/BHS_dMRI_Project.pdf)
 

## Methods and Results 

1. Data Visualization (see [gif figure](https://github.com/brainhack-school2020/BHS_Project_dMRI/tree/master/Visualization) below):
  - 3D volume slices image
  	1. Show different slices of images;
  	2. Change observe view point;
  	3. Play animation;
  - Interactive widgets use to show preprocessed results
  	1. Select different maps;
  	2. Select slices;
  	3. Select maximum diffusion sthrength;
  	4. Display title
  - Interactive widgets use to show reconstruction results;
  	1. Play different maps;
  	2. Select slices;
  	3. Slect maximum diffusion sthrength;
  	4. Display give title.
  - Interactive widgets 2 use to show preprocessed results
  	1. play different maps;
  	2. Select slices;
  	3. Select maximum diffusion sthrength;
  	4. Display title.

<div align="left">
	<img src="https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/Visualization/VolumeSlicesImg.gif" width="300" alt="1" title="3D volume slices image">
	<img src="https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/Visualization/Preprocessing.gif" width="300" title="Interactive widgets use to show preprocess results">
</div>
<div align="left">
	<img src="https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/Visualization/ReconstructedImg.gif" width="300" title="Interactive widgets use to show reconstruction results">
	<img src="https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/Visualization/Preprocessing2.gif" width="300" title="Interactive widgets use to show preprocess results">	
</div>
2. Preprocessing

* **Method** 
	1. Load diffusion weighted image data and set data path;
	2. Denoise data by using MP-PCA method of DIPY;
	3. Correct distortion by using FSL TOPUP;
	4. Extract brain and create brain mask by using FST bet;
	5. Correct head movement artifacts by using FSL EDDY;
	5. Extract maps from 4D data and show results.

* **Results** 

<div align="left">
	<img src="https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/Fig/PreproResults.png" width="650" alt="1" title="DTI Results">
</div>

3. DTI reconstruction

* **Method** 
	1. DIPY was used to fit tensor model;
	2. Different maps were saved;
	3. Colored diffusion map was coded and saved;
	4. Show maps
	
* **Results**

<div align="left">
	<img src="https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/Fig/DTI_Results.png" width="800" alt="1" title="DTI Results">
</div>

4. Left and right hemispheres classification

* **Method** 
	1. 80 Slices of brain images (40 left hemisphere slice and 40 right hemisphere) were extracted and transfered to brain parts classification;
	2. Left hemisphere brain image and right hemisphere brain iamge were taged with 0 and 1 specifically;
	3. Slice number was treated as one of features used for classification;
	4. Diffusino strength of each slice hemisphere was calculated  as the second feature of classification;
	5. Total effictive voxel of eahc slice hemisphere was calculated as the third feature for classification;
	6. Dataset was splitted into train dataset (70%) and test dataset (30%);
	7. Use KNN to classify
	
* **Classification Reports**

<div align="left">
	<img src="https://github.com/brainhack-school2020/BHS_Project_dMRI/blob/master/Fig/classification.png" width="400" alt="1" title="DTI Results">
</div>


### Progress overview

Since May 11, this project goes well and three goals of this project have been reached. This is just to let me be familiar with steps and tools of diffusion MRI processing. Next, I will combine different processing methods into this project. Specifically, I would like to look deep into DTI model fitting and try to replace it by a new model created by myself.

## What I have learned
1. Python
	* FSL, Nipype.interfaces, DIPY
	* matplotlib, plotly, ipywidgets
	* Function definition and calling
2. Markdown
	* Format this README file
	* Insert figures and animation
	* LaTex to edit mathematical equations
3. Github
	* Version control
	* Project organization
4. BIDS
5. Jupter notebook
6. Found and learnt to use some small but useful tools
	* [Peek](https://github.com/phw/peek) for GIF making
	* [Gedit](https://wiki.gnome.org/Apps/Gedit) to edit code or markdown
7. Medical file format (NII) and data structure (BIDS)
8. Statistical method and machine learning





## Conclusion and acknowledgement

This project started with medical imaging data format, then preprocessed the diffusion weighted images, which includes MP-PCA denoising, FSL TOPUP distortion correction and head movement correction. After this, DTI images were reconstructed from these preprocessed images successfully. Additionally, a dataset for left and right hemispheres classification was generated from these preprocessed images. By using the KNN method, classification accuracy of 92% was reached. As a starter, I will continue this project in the future. Soon, self-made models, instead of DTI model, will be used to reconstruct diffusion images. After that, I would like to use machine learning methods to classify potential changes of brain microstructures.


Thanks to [Brainhack Summer School 2020](https://school.brainhackmtl.org/) and all instructors. Specifically, I would like to thank my instructors Noor, Greg and Agah for your advice, instruction and encouragement. I feel so lucky to find and take this summer school. During this short one month, I touched so many new skills and tools and began my first neuroscience project. I would also like to thank all the summer school students, just because of you, I know how wonderful the neuroscience world is and how active the neuroscience group is! 


## References

1. FMRIB Software Library v6.0, https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSL
2. MARKDOWN Syntax, https://www.markdownguide.org/basic-syntax/
3. RDadarwal (2020), https://github.com/RDadarwal
4. Nipype interface FSL, https://nipype.readthedocs.io/en/latest/api/generated/nipype.interfaces.fsl.html
5. Plotly Python Open Source Graphing Library, https://plotly.com/python/
6. Jupyter Widgets, https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Basics.html
7. Scikit-learn Classifier comparison, https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html

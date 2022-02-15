# Homework 1 #

## Introduction 
  	This file includes python program solution for Homework 1 for
	UMD ENPM 673 Spring 2022 batch. The folders consists of python
	program along with some generated outputs as .jpg image. 
	
	These files are executable:
		FOV & Pixel count.py
		Ball_Video_1.py
                Ball_Video_2.py
                Covarience matrix.py
		LS,TLS,RANSAC.py
		SVD .py
    

	All other files are either pictures of generated output or the
	the media files.
## Requirements
       ***Important****************************************************************
       *Change the path of the video in cv2.VideoCapture() function in python file*
       *Change the path of the video in cv.imwrite() function in python file*
       *Change the path of  pd.read_csv() function in python file to obtain the dataset*
       *If graph does not apper then comment the Extracting frames from video after images are extracted*
       ****************************************************************************
### To run this code following libraries are required
* OpenCV, 
* random, 
* matplotlib, 
* NumPy, 
* time,
* glob,
* pandas.

### Installation (For ubuntu 18.04) ###
* OpenCV
	````
	sudo apt install python3-opencv
	````
* matplotlib
	````
	python -m pip install -U matplotlib
	````
* NumPy
	````
	pip install numpy
	````
	
### Running code in ubuntu
After changing the path of the video source file and installing dependencies
Make sure that current working derectory is same as the directory of program
You can change the working derectory by using **cd** command

* Run the following command which will give the FOV and the numbers of pixels
````
FOV & Pixel count.py
````
* Run the following command which will generate curve plot for video 1
````
Ball_Video_1.py
````
* Run the following command which will generate curve plot for video 2
````
Ball_Video_2.py
````
It is important to note that if both python files are in different directory
we have to change to the correct directory again.

* Run the following command to get Covarience Matrix and to plot the eiganvectors
````
Covarience matrix.py
````
* Run the following command to plot the LS, TLS, RANSAC on the dataset 
````
LS,TLS,RANSAC.py
````
* Run the following command to compute the SVD
````
SVD .py
````

### Troubleshooting ###
	Most of the cases the issue will be incorrect file path.
	Double check the path by opening the properies of the video
	and copying path directly from there.

	For issues that you may encounter create an issue on GitHub.
### Maintainers ###
	Nisarg Upadhyay(nisargupadhyay2@gmail.com)

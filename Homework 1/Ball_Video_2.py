# Importing the libraries

import cv2 as cv
import glob
import numpy as np
import matplotlib.pyplot as plt

# Defining variables

new_array=[]
x_cor = []
y_cor=[]
y_new = []
x_val = []
count=0

# Extracting frames from video
'''
video = cv.VideoCapture("/home/nisarg/Desktop/ball_video2.mp4")
while True:
    B,frame = video.read()
    if B == True:
        if count < 10:
            cv.imwrite("/home/nisarg/Desktop/ENPM 673 - Perception/Assignment/Homework 1/Project 2/Images 2/frame0" + str(count) + ".jpg", frame)
            count+=1
            cv.waitKey(30)
        else:
            cv.imwrite("/home/nisarg/Desktop/ENPM 673 - Perception/Assignment/Homework 1/Project 2/Images 2/frame" + str(count) + ".jpg", frame)
            count+=1
            cv.waitKey(30)

'''
# Function to resize the image

def resize(frames,scale):
    
    widht = int(frames.shape[1] * scale)
    height = int(frames.shape[0] * scale)
    dim = (widht,height)
    return cv.resize(frames,dim)

# Calling Images

filename = [img for img in glob.glob("C:/Users/nisar/Desktop/Homework 1/Project 2/Images 2/*.jpg")]
filename.sort()

# Filtering red Channel

for img in filename:
   image = cv.imread(img)
   
   image = resize(image, 0.2)
   result = image.copy()
   image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    

   l_1 = np.array([0, 100, 20])
   u_1 = np.array([10, 255, 255])
    
 
   l_2 = np.array([160,100,20])
   u_2 = np.array([179,255,255])
    
   lower_mask = cv.inRange(image, l_1, u_1)
   upper_mask = cv.inRange(image, l_2, u_2)
    
   full_mask = lower_mask + upper_mask;
   
# Extracting x and y coordinates from an image

   x_upper= np.max(np.argmax(full_mask==255,axis = 1))
   y_upper= np.max(np.argmax(full_mask==255,axis = 0))


   x_cors = x_upper
   y_cors = y_upper
   x_cor.append(x_cors)
   y_cor.append(y_cors)

# Function for Polonomial Regrassion

def poly_reg(x,y):
  x = np.array(x)
  y = np.array(y)
  x_a = np.concatenate((np.ones(x.shape),x,x**2)).reshape(3,-1)
  x_transpose = np.transpose(x_a)
  x_dot = np.dot(x_a,x_transpose)
  x_inv = np.linalg.inv(x_dot)
  x_dot_y = np.dot(y,x_transpose)
  constants = np.dot(x_inv,x_dot_y)
  return  constants

b_val = poly_reg(x_cor, y_cor)
b_0= b_val[0]
b_1 = b_val[1]
b_2 = b_val[2]

# Calculating new y variable 

for i in range(len(x_cor)):
    y_new+= [b_0 + np.dot(b_1, x_cor[i]) + np.dot(b_2, x_cor[i]**2)]

# Ploting the regression curve 

plt.plot(x_cor,y_cor, "ro")
plt.axis([0,700, 500,0])
plt.plot(x_cor,y_new, color='green') 
plt.title('Line Fitted through points using Least Squares of second degree polynomial')
plt.legend(["Data", "Regression Line"], loc ="upper left")
plt.show()


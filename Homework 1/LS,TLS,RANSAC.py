# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random

# Importing the Data
dataset  = pd.read_csv("C:/Users/nisar/Downloads/Sheet1.csv",header = None)
dataset.head()

# Accessing the x & y coordinates

x = dataset.loc[1:,0].values
y = dataset.loc[1:,6].values
y_new = []
val = []

x = [int(x) for x in x]

y = [int(float(y)) for y in y]


# Least Square Method

x_mean = np.mean(x)
y_mean = np.mean(y)
y_mean = y_mean.astype(int)
x_mean = x_mean.astype(int)

num = 0
den = 0

# Calculating slope and intercept

for i in range(len(x)):
    num+= (x[i]-x_mean)*(y[i]-y_mean)
    den+= (x[i]-x_mean)**2
    
m = num/den
c = y_mean - m*x_mean

m = m.astype(int)
c = c.astype(int)

# predicted y

for i in x:
   y_new.append(m*x[i] + c)
   
# Total Least Square Method
p = 0
q = 0
z = 0
y_new1 = []

x_mean = np.mean(x)
y_mean = np.mean(y)

# Calculating slope and intercept

for i in range(len(x)):
    p+= ((y[i]-y_mean))
    q+= ((x[i]-x_mean))

w = p-q

for i in range(len(x)):
    z+= ((x[i]-x_mean)*(y[i]-y_mean))

r = 2*z

m1 = (w + (np.sqrt(w**2 + r**2)))
m1 = m1/r
c1 = y_mean - (m1*x_mean)

# predicted y

for i in x:
   y_new1.append(m1*x[i] + c1)

# RANSAC

y_new3 = []
for i in range(len(x)):
    val.append((x[i],y[i]))
    
# Select random points to form a line

def random_pairs():
    i_1 = random.randint(0, len(val)-1)
    i_2 = random.randint(0, len(val)-1)
    while i_1 == i_2:
        i_2 = random.randint(0,len(val)-1)

    return(i_1, i_2)

numberOfIterations = 700
tolerance = 7
maximum_inlierscount = 0
coefficients = []

for iteration in range(0, numberOfIterations):
    (i1, i2) = random_pairs()
    
#find the coefficients for the line
    
    b0 = val[i1][1] - val[i2][1]
    b1 = val[i2][0] - val[i1][0]
    b2 = val[i1][0]*val[i2][1] - val[i1][1]*val[i2][0]
    
#numbers of inliers 
    
    inlierscount = 0
    for i in range(0, len(val)):
        distance = abs(b0*val[i][0] + b1*val[i][1] + b2)/(np.sqrt(b0**2 + b1**2))
        
        if distance < tolerance:
            inlierscount += 1
    if inlierscount > maximum_inlierscount:
        coefficients = [b0, b1, b2]
        maximum_inlierscount = inlierscount

# coefficients for the line for the given tolarance

b0 = coefficients[0]
b1 = coefficients[1]
b2 = coefficients[2]

# predicted y

for i in range(len(x)):
    y_new3.append((-b2-b0*x[i])/b1)

# Ploting the graphs    
plt.scatter(x,y)

# Least square method
plt.plot([min(x), max(x)], [min(y_new), max(y_new)], color='green') 

# Total Least square method
plt.plot([min(x), max(x)], [min(y_new1), max(y_new1)], color='red')
 
# RANSAC
plt.plot([min(x), max(x)], [min(y_new3), max(y_new3)], color='black') 

plt.title('Line Fitted through points using LS, TLS, RANSAC')
plt.xlabel("Age")
plt.ylabel("Insurance Cost")
plt.legend(["Data", "LS", "TLS", "RANSAC"], loc ="upper left")
plt.show()




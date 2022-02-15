# Importing the libraries

import numpy as np
from numpy.linalg import eig
import matplotlib.pyplot as plt
import pandas as pd

# Defining variables

sqr_x = []
sqr_y = []

# Accessing the x & y coordinates

dataset  = pd.read_csv("C:/Users/nisar/Downloads/Sheet1.csv",header = None)
dataset.head()

x = dataset.loc[1:,0].values
y = dataset.loc[1:,6].values

x = [int(x) for x in x]

y = [int(float(y)) for y in y]

# Computing covarience matrix

product = np.multiply(x,y)
mean_xy = np.mean(product)
mean_x = np.mean(x)
mean_y = np.mean(y)
for i in x:
   sqr_x.append(i**2)

mean_xx = np.mean(sqr_x)

for j in y:
   sqr_y.append(j**2)

mean_yy = np.mean(sqr_y)
covariance_matrix = [[mean_xx-(mean_x**2),(mean_xy)-(mean_x*mean_y)],[(mean_xy)-(mean_x*mean_y),mean_yy-(mean_y**2)]]

print(covariance_matrix)
print("is the covarience matrix")

# eigenvalues and eigenvectors

w,v= eig(covariance_matrix)
print(w,v)


origin = [45,30000]

eig_vec1 = v[:,0]
eig_vec2 = v[:,1]

# Ploting eiganvectors on the graph

plt.scatter(x,y)
plt.quiver(*origin, *eig_vec1, color=['r'], scale=3.2)
plt.quiver(*origin, *eig_vec2, color=['b'], scale=3.2)
plt.title('Eiganvectors of the data')
plt.xlabel("Age")
plt.ylabel("Insurance Cost")
plt.legend(["Data", "EV1", "EV2",], loc ="upper left")
plt.show()



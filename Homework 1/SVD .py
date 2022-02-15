import numpy as np
v = []

x  = 5,150,150,5
y = 5,5,150,150
xp = 100,200,220,100
yp = 100,80,80,200

points = [x,y,xp,yp]
points = np.transpose(points)

for i in points:
    for c in i:
        v.append(c)


a = [-v[0],-v[1],-1,0,0,0,v[0]*v[2],v[1]*v[2],v[2]]
c = [-v[4],-v[5],-1,0,0,0,v[4]*v[6],v[5]*v[6],v[6]]
e = [-v[8],-v[9],-1,0,0,0,v[8]*v[10],v[9]*v[10],v[10]]
g = [-v[12],-v[13],-1,0,0,0,v[12]*v[14],v[13]*v[14],v[14]] 
b = [0,0,0,-v[0],-v[1], -1,v[0]*v[3],v[1]*v[3],v[3]]
d = [0,0,0,-v[4],-v[5], -1,v[4]*v[7],v[5]*v[7],v[7]]
f = [0,0,0,-v[8],-v[9], -1,v[8]*v[11],v[9]*v[11],v[11]]
h = [0,0,0,-v[12],-v[13],-1,v[12]*v[15],v[13]*v[15],v[15]]

Z = ([a,b,c,d,e,f,g,h])

# Function to find the SVD

def svd(matrix):
    
    AT = np.transpose(matrix) 
    AT_A = AT@matrix
    

    eig_val, eig_vec = np.linalg.eig(AT_A)
    sorted_val = eig_val.argsort()[::-1]

   
    new_eig_vec = eig_vec[:, sorted_val]

    # The final VT matrix 
    new_eig_vec_VT = np.transpose(new_eig_vec)

   
    A_AT = matrix@AT

    
    eig_val_U, eig_vec_U = np.linalg.eig(A_AT)

    
    sorted_val1 = eig_val_U.argsort()[::-1]
    new_eig_val_U = eig_val_U[sorted_val1]
    
    # The final U matrix 
    new_eig_vec_U = eig_vec_U[:, sorted_val1]

    
    diagonal_matt = np.diag((np.sqrt(new_eig_val_U)))

    # The final Sigma matrix
    S_F = np.zeros_like(matrix).astype(np.float64)
    S_F[:diagonal_matt.shape[0], :diagonal_matt.shape[1]] = diagonal_matt

    # Return the parameters U, S, VT
    return new_eig_vec_U, S_F, new_eig_vec_VT

# The 3 componenets of the SVD Matrix
U, S, VT = svd(Z)

print(U,S,VT)


Homography = VT[8]
Homography = np.reshape(Homography, (3, 3)) 
print('Homography Matrix')
print(Homography)






# calculate the translation of the pivot using n rigid boyd transformation matrixes
#-----------------------------------------------

import numpy as np

def pivot_calibration(F):
    Nf = F.shape[2]
    # Dimension check
    assert F.shape[0] == F.shape[1] == 4, "Need 4*4 homogeneous transformation matrix as input"
    # detF = np.linalg.det(F)
    # assert (detF < 1.001 and detF > 0.999),"The determinant should be 1."

    # Create Matrices
    A = np.concatenate((F[0:3,0:3,0], -np.identity(3)),axis =1)
    b = -F[0:3,3,0].reshape(3,1)
    for i in range (1,Nf):
        A_temp = np.concatenate((F[0:3,0:3,i], -np.identity(3)),axis =1)
        b_temp = -F[0:3,3,i].reshape(3,1)
        A = np.concatenate((A,A_temp), axis = 0)
        b = np.concatenate((b,b_temp), axis = 0)

    # print(A)
    # print(b)
    #Initial Guess of q by Psudeo Inverse approach
    # Ax = b
    # x = (A.T * A)^-1 * A.T * b
    q = np.matmul(np.matmul(np.linalg.inv(np.matmul(A.T,A)),A.T),b)
    #Iteration until dq is small enough
    dq = np.ones((6,1))
    while np.linalg.norm(dq) > 1e-5:
        dq = np.matmul(np.linalg.inv(np.matmul(A.T,A)),np.matmul(A.T,(b - np.matmul(A,q))))
        q = q + dq
    return q
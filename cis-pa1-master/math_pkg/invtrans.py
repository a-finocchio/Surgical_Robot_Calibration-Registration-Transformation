#inverse from F to -F
#-----------------------------------------------

import numpy as np 

def invtrans(T):

	assert T.shape[0] == T.shape[1] == 4, "Need 4*4 homogeneous transformation matrix as input"
	detT = np.linalg.det(T)
	assert (detT < 1.001 and detT > 0.999),"The determinant should be 1."

	T[0:3,0:3] = T[0:3,0:3].T
	T[0:3,3] = -np.matmul(T[0:3,0:3],T[0:3,3])
	return T
# Generate the rigid body transformation matrix from rotation matrix and
# translation matrix using homogeneous representation.
#-----------------------------------------------


import numpy as np
def trans(R,p):

	# Dimension Check
	assert (R.shape == (3,3) and p.shape ==(3,1)), "This function requires 3*3 matrix and a 3*1 matrix as input"

	# Det Check
	detR = np.linalg.det(R)

	assert (detR > 0.999 and detR < 1.001), "The determinant of R should be 1, please check your rotation matrix"

	T = np.concatenate((np.concatenate((R, p), axis=1),np.array([[0,0,0,1]])), axis = 0)
	return T
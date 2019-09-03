# Generate the rigid body transformation matrix from angle matrix and
# translation matrix using homogeneous representation.
#-----------------------------------------------

import numpy as np
from math_pkg import *

def trans_angle(angle,p):

	# Dimension Check
	assert (angle.shape == (1,3) and p.shape ==(3,1)), "This function requires 1*3 matrix and a 3*1 matrix as input"

	Rot_matrix = np.dot(rotz(angle[0,0]) ,np.dot(roty(angle[0,1]) , rotz(angle[0,2])))

	T = np.concatenate((np.concatenate((Rot_matrix, p), axis=1),np.array([[0,0,0,1]])), axis = 0)
	return T



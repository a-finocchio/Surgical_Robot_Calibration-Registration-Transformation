# Generate the rigid body transformation matrix from two rotation matrixs and
# translations matrix using homogeneous representation.
#-----------------------------------------------

import numpy as np
from math_pkg import *

def F_Rp_multiple(R1,p1,R2,p2):

	# Dimension Check
	assert (R1.shape == (3,3) and R2.shape ==(3,3)), "This function requires 3*3 matrix and a 3*3 matrix as input"
	assert (p1.shape == (3,1) and p2.shape ==(3,1)), "This function requires 3*1 matrix and a 3*1 matrix as input"

	F1 = trans(R1,p1)
	F2 = trans(R2,p2)

	F3 = np.dot(F1 , F2)
	
	return F3
# Generate the rotation matrix from a angle array
#-----------------------------------------------

import numpy as np
from math_pkg import *

def angle_2_rot(angle):
	# Generate the rotation matrix from angle matrix
	# using left multiplication



	# Dimension Check
	assert (angle.shape == (1,3) ), "This function requires 1*3 matrix"

	Rot_matrix = np.dot(rotz(angle[0,2]), np.dot( roty(angle[0,1]) , rotx(angle[0,0])))

	
	return Rot_matrix


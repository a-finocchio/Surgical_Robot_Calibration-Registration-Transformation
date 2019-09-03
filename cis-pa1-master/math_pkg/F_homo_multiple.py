# Generate the rigid body transformation matrix bewteen two homogenius 4*4 F matrix
# using homogeneous representation.
#-----------------------------------------------

import numpy as np
from math_pkg import *

def F_homo_multiple(F1,F2):
	
	# Dimension Check
	assert (F1.shape == (4,4) and F2.shape ==(4,4)), "This function requires 4*4 matrix and a 4*4 matrix as input"

	F3 = np.dot(F1 , F2)

	
	return F3
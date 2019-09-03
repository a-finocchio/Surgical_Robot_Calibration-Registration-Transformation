# Generate the skew matrix from a 3*1 matrix 
#-----------------------------------------------

import numpy as np
from math_pkg import *

def skew_build(xyz):

	# Dimension Check
	assert (xyz.shape == (3,1) or xyz.shape ==(1,3)), "This function requires 3*1 matrix or a 1*3 matrix as input"

	if xyz.shape == (3,1):
		skew = np.array([[0,(-1)*xyz[2], xyz[1]],[xyz[2],0,(-1)*xyz[0]],[(-1)*xyz[1],xyz[2],0]])
	else:
		skew = np.array([[0,(-1)*xyz[0,2], xyz[0,1]],[xyz[0,2],0,(-1)*xyz[0,0]],[(-1)*xyz[0,1],xyz[0,2],0]])

	return skew	
# do an automatic test rot_2_angle.py and angle_2_rot.py
# method: randomly generate angle matrix and transfrom it to rotation matrix
# then transform back into the angle matrix, check the residual error between 
# the original angle matrix and the new angle matrix.
#-----------------------------------------------


import numpy as np
import sys
sys.path.append("..")
from math_pkg import *


# test rounds
num_rounds = 1


# do angle to rotation matrix and back to angle
def angle_2_angle():
	angle_random = np.random.rand(1,3)
	# build rotation matrix
	rot = angle_2_rot(angle_random)
	# transform back to angle array
	angle_calculated = rot_2_angle(rot)
	# residual error
	error = np.absolute(angle_random - angle_calculated)
	print(angle_random)
	print(rot)
	return error



# auto test, check the total error
def auto_test_angle2angle(num_rounds):
	
	error_residual = np.zeros((1,3))

	for j in range(num_rounds):

		error_temp = angle_2_angle()
		error_residual = error_residual + np.absolute(error_temp)

	return error_residual	


error_residual = auto_test_angle2angle(num_rounds)
print('the total residual array')
print(error_residual)
print('\n')
print('the sum of all residual error')
error_value = np.sum(np.sum(error_residual , axis = 0),axis = 0)
print(error_value)



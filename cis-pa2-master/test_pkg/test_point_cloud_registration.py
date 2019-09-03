# do an automatic test point_cloud_registration.py
# method: randomly generate point cloud and F transformation
# then sum the absolute error between the calculated F_c from the point_cloud_registration.py 
# and the generated F transformation.
# if the residual is almost zero, then the F_calculated is correct,
# which means the point_cloud_registration.py is good to use
#-----------------------------------------------


import numpy as np
import sys
sys.path.append("..")
from math_pkg import *


# test rounds
num_rounds = 100


# transform generated random point cloud with transformation matrix F
def tranfrom_cloud(cloud_random,F):
	num = cloud_random.shape[0]
	cloud_transformed = np.random.rand(num,3)

	for i in range(num):
		point = np.array([cloud_random[i,:]])

		point_homo = np.concatenate((np.transpose(point), np.array([[1]])),axis=0)

		translation_transformed = np.dot(F,point_homo)

		point_temp = translation_transformed[0:3,:]

		cloud_transformed[i] = point_temp.T

	return cloud_transformed


# test the F_calculated from point_cloud_registration.py
def test_point_cloud_registration(roll,pitch,yaw,x,y,z,num_points):

	# generate random point cloud
	cloud_random = np.random.rand(num_points,3)

	# generate 4*4 transform matrix
	angle = np.array([[roll,pitch,yaw]])
	translation = np.array([[x],[y],[z]])
	F = trans_angle(angle,translation) 

	# transform the point cloud
	cloud_transformed = tranfrom_cloud(cloud_random,F)

	# calculated the point cloud 
	F_calculated = point_cloud_registration(cloud_random,cloud_transformed)

	# print('----------F original-----------')
	# print(F)
	# print('\n')
	# print('----------F calculated---------')
	# print(F_calculated)
	# print('\n')

	error = F - F_calculated
	return error


# auto test, check the total error
def auto_test_PCR(num_rounds):
	roll = np.random.rand(num_rounds)
	pitch = np.random.rand(num_rounds)
	yaw = np.random.rand(num_rounds)
	x = np.random.rand(num_rounds)
	y = np.random.rand(num_rounds)
	z = np.random.rand(num_rounds)
	num_points = np.random.randint(3,100, size=num_rounds)

	error = np.zeros((4,4))

	for j in range(num_rounds):

		error_temp = test_point_cloud_registration(roll[j],pitch[j],yaw[j],x[j],y[j],z[j],num_points[j])
		error = error + np.absolute(error_temp)

		if np.sum(np.sum(np.absolute(error_temp), axis = 0), axis = 0)>0.00001:
			print(roll[j],pitch[j],yaw[j],x[j],y[j],z[j],num_points[j])
		# print out the error between original F and the calculated F
		# print('----------error temp---------------')
		# print(error_temp)
		# print('\n')	

	return error	
	

print('the total residual matrix')
error_check = auto_test_PCR(num_rounds)
print(error_check)
print('\n')
print('the sum of all element in the total residual matrix')
error_value = np.sum(np.sum(error_check, axis = 0), axis = 0)
print(error_value)


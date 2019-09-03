import numpy as np
import sys
sys.path.append("..")
from math_pkg import *


char = 'abcdefghij'
for test_char in char:
	if test_char in 'abcdef':
		data_type = 'debug'
	else:
		data_type = 'unknown'
	# define read in empivot data
	def ReadData(filename):  
	    with open(filename, mode = 'r') as csv_file:
	        csv_reader = csv.reader(csv_file)
	        datalist = list(csv_reader)
	    Ng = int(datalist[0][0])
	    Nf = int(datalist[0][1])
	    datalist.pop(0)
	    data = np.array([[float(j) for j in i] for i in datalist])
	    return Ng,Nf,data

	# -----------------------------------------------------------------
	# step 1 input the body calibration data file and the calculate the ground truth point cloud data
	# -----------------------------------------------------------------
	
	# -----------------------------------------------------------------
	c_expect,c_measure = import_calibrate_data(test_char)
	correction_coeff_matrix = distor_coef_matrix(c_measure,c_expect,5)
	Ng, Nf, data = ReadData('../PA 1-2 Student Data/pa2-'+ data_type + '-'+ test_char +'-empivot.txt')


	# -----------------------------------------------------------------
	# step 2 dewarp the measured data 
	data = distortion_correction(correction_coeff_matrix,data,5)


	# -----------------------------------------------------------------
	# step 3 calculate P_em_dimple
	# -----------------------------------------------------------------
	g = np.zeros((Ng,3))
	Fg = np.zeros((4,4,Nf))
	t = 0
	G0 = np.mean(data[0:Ng],axis = 0).reshape(1,3)
	g[0:Ng] = data[0:Ng] - G0
	for j in range (0, len(data), Ng):
		Fg[:,:,t] = point_cloud_registration(g, data[j:j+Ng])
		t += 1

	q_EM = pivot_calibration(Fg)
	P_EM_dimple = q_EM[3:6].reshape(3,1)
	P_tip = q_EM[0:3].reshape(3,1)
	output1 = np.round(P_EM_dimple, 2)
	# print (output1)

	# output result of P_dimple to file
	with open('../OUTPUT/pa2-'+ data_type + '-'+ test_char +'-our-output1.txt', 'w') as csvfile:
	    csv_writer = csv.writer(csvfile, delimiter=',')
	    csv_writer.writerow([Ng, Nf, 'pa2-'+ data_type + '-'+ test_char +'-our-output1.txt'])
	    csv_writer.writerow([output1[0][0], output1[1][0], output1[2][0]])
	print ('pa2-'+ data_type + '-'+ test_char +'-our-output1.txt generated!')

	# def ReadDebugData1(filename):  
	#     with open(filename, mode = 'r') as csv_file:
	#         csv_reader = csv.reader(csv_file)
	#         datalist = list(csv_reader)
	#     datalist.pop(0)
	#     data = np.array([[float(j) for j in i] for i in datalist])
	#     return data
	# debugdata1 = ReadDebugData1('../PA 1-2 Student Data/pa2-'+data_type + '-'+ test_char+'-output1.txt')[0]
	# res1 = np.round(debugdata1 - P_EM_dimple.T,2)
	# print ('Output 1 Residual:')
	# for i in res1:
	# 	print(i[0],',',i[1],',',i[2])


	# -----------------------------------------------------------------
	# step 4 compute the corrected locations of fiducial points
	# -----------------------------------------------------------------
	def ReadData1(filename):  
	    with open(filename, mode = 'r') as csv_file:
	        csv_reader = csv.reader(csv_file)
	        datalist = list(csv_reader)
	    NG = int(datalist[0][0])
	    NB = int(datalist[0][1])
	    datalist.pop(0)
	    data = np.array([[float(j) for j in i] for i in datalist])
	    return NG,NB,data

	NG, NB, data1 = ReadData1('../PA 1-2 Student Data/pa2-'+ data_type + '-'+ test_char +'-em-fiducialss.txt')

	# dewarp data
	G_corrected = distortion_correction(correction_coeff_matrix,data1,5)


	# -----------------------------------------------------------------
	# step 5 compute the registration frame
	# -----------------------------------------------------------------
	G0 = np.mean(G_corrected[0:NG],axis = 0).reshape(1,3)
	Fg = np.zeros((4,4,NB))
	B = np.zeros([4,1,NB])
	t = 0
	for j in range (0, len(G_corrected), NG):
	    Fg[:,:,t] = point_cloud_registration(g, G_corrected[j:j+NG])
	    B[:,:,t] = np.matmul(Fg[:,:,t],np.concatenate((P_tip,np.ones([1,1])), axis = 0 ))
	    t += 1
	Bj = np.transpose(B[0:3,:,:],(2,0,1)).reshape(NB,3)

	def ReadData2(filename):  
	    with open(filename, mode = 'r') as csv_file:
	        csv_reader = csv.reader(csv_file)
	        datalist = list(csv_reader)
	    datalist.pop(0)
	    data = np.array([[float(j) for j in i] for i in datalist])
	    return data

	bj = ReadData2('../PA 1-2 Student Data/pa2-'+ data_type + '-'+ test_char +'-ct-fiducials.txt')

	F_reg = point_cloud_registration(bj,Bj)


	# -----------------------------------------------------------------
	# step 6 apply distortion correction and compute the tip location with respect to the CT image
	# -----------------------------------------------------------------	
	# apply distortion correction
	def ReadData3(filename):  
	    with open(filename, mode = 'r') as csv_file:
	        csv_reader = csv.reader(csv_file)
	        datalist = list(csv_reader)
	    NG = int(datalist[0][0])
	    Nf = int(datalist[0][1])
	    datalist.pop(0)
	    data = np.array([[float(j) for j in i] for i in datalist])
	    return NG,Nf,data

	NG, Nf, data3 = ReadData3('../PA 1-2 Student Data/pa2-'+ data_type + '-'+ test_char +'-EM-nav.txt')

	G_co = distortion_correction(correction_coeff_matrix,data3,5)
	t = 0
	Fg = np.zeros((4,4,Nf))
	P_f = np.zeros([4,1,Nf])
	for j in range (0, len(G_co), NG):
	    Fg[:,:,t] = point_cloud_registration(g, G_co[j:j+NG])
	    P_f[:,:,t] = np.matmul(Fg[:,:,t],np.concatenate((P_tip,np.ones([1,1])), axis = 0 ))
	    t += 1

	# compute the tip location with respect to the CT image 
	P_CT_tip = np.zeros([4,1,Nf])
	invF_reg = np.linalg.inv(F_reg)
	for i in range(Nf):
	    P_CT_tip[:,:,i] = np.matmul(invF_reg,P_f[:,:,i])
	P_CT = np.transpose(P_CT_tip[0:3,:,:], (2,0,1))
	output  =  np.round(P_CT,2)
	with open('../OUTPUT/pa2-'+ data_type + '-'+ test_char +'-our-output2.txt', 'w') as csvfile:
	    csv_writer = csv.writer(csvfile, delimiter=',')
	    csv_writer.writerow([Nf, 'pa2-'+ data_type + '-'+ test_char +'-our-output2.txt'])
	    for i in range (Nf):
	    	csv_writer.writerow([output[i,0,:][0], output[i,1,:][0], output[i,2,:][0]])
	print ('pa2-'+ data_type + '-'+ test_char +'-our-output2.txt generated!')

	# def ReadDebugData2(filename):  
	#     with open(filename, mode = 'r') as csv_file:
	#         csv_reader = csv.reader(csv_file)
	#         datalist = list(csv_reader)
	#     datalist.pop(0)
	#     data = np.array([[float(j) for j in i] for i in datalist])
	#     return data
	# debugdata2 = ReadDebugData2('../PA 1-2 Student Data/pa2-'+data_type + '-'+ test_char+'-output2.txt')
	# res = np.round(debugdata2 - P_CT[:,:,0],2)
	# print ('Output 2 Residual:')
	# for i in res:
	# 	print(i[0],',',i[1],',',i[2])

print ("Evaulated all data!")
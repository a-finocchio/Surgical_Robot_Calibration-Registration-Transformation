import numpy as np
import sys
sys.path.append("..")
from ReadInput import *
from BoundingSphere import *
from FindClosestPoint import *

NA, a, tipA = ReadData1('../PA 345 - Student Data/Problem3-BodyA.txt')
NB, b, tipB = ReadData1('../PA 345 - Student Data/Problem3-BodyB.txt')

char = 'ABCDEFGHJ'
for test_char in char:
	if test_char in 'ABCDEF':
		data_type = 'Debug'
	else:
		data_type = 'Unknown'
	Nv, v, Nt, tri = ReadMesh('../PA 345 - Student Data/Problem3MeshFile.sur')
	NS, Nsamps, data = ReadData('../PA 345 - Student Data/PA3-'+ test_char + '-'+ data_type +'-SampleReadingsTest.txt')
	ND = NS - NA - NB
	FA = np.zeros((4,4,Nsamps))
	FB = np.zeros((4,4,Nsamps))
	d = np.zeros((4,1,Nsamps))
	t = 0
	for i in range (0,len(data),NS):
	    FA[:,:,t] = point_cloud_registration(a, data[i:i+NA])
	    FB[:,:,t] = point_cloud_registration(b, data[i+NA:i+NA+NB])
	    d[:,:,t] = np.matmul(np.matmul(np.linalg.inv(FB[:,:,t]),FA[:,:,t]),np.concatenate((tipA,np.ones([1,1])), axis = 0 ))
	    t += 1
	# Freg = I
	s_1 = d
	s = np.transpose(s_1[0:3,:,:], (2,0,1))
	q , r = BoundingSphere(v,tri)
	c = np.zeros((Nsamps,3,1))
	for i in range (Nsamps):
	    pt = s[i]
	    bound = 999
	    for j in range (Nt):
	        if (np.linalg.norm(q[j].reshape((3,1)) - pt) - r[j]) <= bound:
	            h = FindClosestPoint(pt,v[tri[j]])
	            dist = np.linalg.norm(h - pt)
	            if dist < bound:
	                c_tmp = h
	                bound = dist
	    c[i] = c_tmp
	d_cs = np.linalg.norm(c - s,axis = 1)

	with open('../OUTPUT/pa3-'+ test_char +'-Output.txt', 'w') as file:
	    file.write(str(Nsamps) + ', pa3-'+ test_char +'-Output.txt\n')
	    for i in range (Nsamps):
	    	line = ["{0:.2f}".format(s[i][0][0]),"{0:.2f}".format(s[i][1][0]),"{0:.2f}".format(s[i][2][0]),"{0:.2f}".format(c[i][0][0]),"{0:.2f}".format(c[i][1][0]),"{0:.2f}".format(c[i][2][0]),"{0:.3f}".format(d_cs[i][0])]
	    	line_new = '{:>8}  {:>8}  {:>8}  {:>10}  {:>8}  {:>8}  {:>8}'.format(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
	    	file.write(str(line_new)+'\n')
	print ('pa3-'+ test_char +'-Output.txt generated!')

print ("Evaulated all data!")
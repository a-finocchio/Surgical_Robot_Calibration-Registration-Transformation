import numpy as np
from math_pkg import *
import csv
import scipy.io as sio

def ReadData1(filename):  
    with open(filename, mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        datalist = list(csv_reader)
    Nd = int(datalist[0][0])
    Na = int(datalist[0][1])
    Nc = int(datalist[0][2])
    datalist.pop(0)
    data = np.array([[float(j) for j in i] for i in datalist])
    return Nd, Na, Nc, data

def ReadData2(filename):  
    with open(filename, mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        datalist = list(csv_reader)
    ND = int(datalist[0][0])
    NA = int(datalist[0][1])
    NC = int(datalist[0][2])
    NF = int(datalist[0][3])
    datalist.pop(0)
    data = np.array([[float(j) for j in i] for i in datalist])
    return ND, NA, NC, NF, data

num = 'g'

Nd, Na, Nc, data1 = ReadData1('./PA 1-2 Student Data/pa1-debug-'+ num + '-calbody.txt')
ND, NA, NC, NF, data2 = ReadData2('./PA 1-2 Student Data/pa1-debug-'+ num + '-calreadings.txt')


d = data1[0:Nd]
a = data1[Nd:Na+Nd]
c = data1[Na+Nd:Nd+Na+Nc]

c_h = np.concatenate((c,np.ones([NC,1])), axis = 1)


FD = np.zeros((4,4,NF))
FA = np.zeros((4,4,NF))
C_exp = np.zeros((4,NC,NF))

t = 0
for i in range(0, len(data2), ND+NA+NC):
	D = data2[i:i+ND]
	A = data2[i+ND:i+ND+NA]
	FD[:,:,t] = point_cloud_registration(d, D)
	FA[:,:,t] = point_cloud_registration(a, A)
	C_exp[:,:,t] = np.matmul(np.matmul(invtrans(FD[:,:,t]),FA[:,:,t]),c_h.T)
	t += 1
our_results = np.round(C_exp[0:3,:,0:7].T[0][0:7],2)

print('Our Results (Only Show First 7 Lines) \n',our_results)

# for i in our_results:
# 	print(i[0],',',i[1],',',i[2])

# Calculate residual
def ReadData(filename):  
    with open(filename, mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        datalist = list(csv_reader)
    datalist.pop(0)
    data = np.array([[float(j) for j in i] for i in datalist])
    return data
debugdata = ReadData('./PA 1-2 Student Data/pa1-debug-'+ num + '-output1.txt')[2:9]

print ('Debug Data: (Only Show First 7 Lines)\n', debugdata)
res = np.round(debugdata - our_results,2)

print ('Residual:')
for i in res:
	print(i[0],',',i[1],',',i[2])


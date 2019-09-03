import numpy as np
from math_pkg import *
import csv

def ReadData(filename):  
    with open(filename, mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        datalist = list(csv_reader)
    ND = int(datalist[0][0])
    NH = int(datalist[0][1])
    Nf = int(datalist[0][2])
    datalist.pop(0)
    data = np.array([[float(j) for j in i] for i in datalist])
    return ND, NH, Nf, data

ND, NH, Nf, data = ReadData('./PA 1-2 Student Data/pa1-debug-a-optpivot.txt')

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

Nd, Na, Nc, data1 = ReadData1('./PA 1-2 Student Data/pa1-debug-a-calbody.txt')
ND, NA, NC, NF, data2 = ReadData2('./PA 1-2 Student Data/pa1-debug-a-calreadings.txt')

FD = np.zeros((4,4,Nf))
FH = np.zeros((4,4,Nf))
h = np.zeros((NH,3))
t = 0
H0 = np.mean(data[ND:ND+NH],axis = 0).reshape(1,3)
h[0:NH] = data[ND:ND+NH] - H0
d = data1[0:Nd]

for i in range(0, len(data), ND+NH):
	D = data[i:i+ND]
	H = data[i+ND:i+ND+NH]
	FH[:,:,t] = point_cloud_registration(h, H)
	FD[:,:,t] = point_cloud_registration(d, D)
	t += 1


# Calculate FD^-1*FH
FDH = np.zeros((4,4,Nf))


for i in range(Nf):
    FDH[:,:,i] = np.matmul(invtrans(FD[:,:,i]), FH[:,:,i])
q_opt = pivot_calibration(FDH)
P_opt_dimple = q_opt[3:6].reshape(3,1)
print (P_opt_dimple)

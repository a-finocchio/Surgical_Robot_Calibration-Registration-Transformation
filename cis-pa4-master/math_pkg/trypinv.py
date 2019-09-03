import numpy as np
import sys
sys.path.append("..")
from math_pkg import *
import csv
import scipy.io as sio
import numpy.linalg as nplinear



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







# 瞎写的pinv。 distorion correction
# show_result = np.concatenate()
# print(our_results-100 -c[0:7,:])
def pinv_distortion():


    num = 'a'
    file_name1 = '../PA 1-2 Student Data/pa2-debug-'+ num + '-calbody.txt'
    file_name2 = '../PA 1-2 Student Data/pa2-debug-'+ num + '-calreadings.txt'

    Nd, Na, Nc, data1 = ReadData1(file_name1)
    ND, NA, NC, NF, data2 = ReadData2(file_name2)


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



    C_exppp = C_exp[0:3,:,0:7].T[0] 
    difference = C_exppp - c
# print('/n')
    # print(difference)

    diff_ = c + 100
    dis_matrix =np.matmul(diff_ , nplinear.pinv(C_exppp))

# print(dis_matrix)

    C_exp_cal = np.matmul(nplinear.pinv(dis_matrix), diff_)

    error = C_exppp - C_exp_cal
    # print(np.sum(np.sum(error, axis = 0),axis = 0))
    return dis_matrix


    
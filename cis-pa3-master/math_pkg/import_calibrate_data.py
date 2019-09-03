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



def import_calibrate_data(a_string):

    num = a_string
    if num in 'abcdef':
        data_type = 'debug'
    else:
        data_type = 'unknown'

    file_name1 = '../PA 1-2 Student Data/pa2-'+data_type+'-'+ num + '-calbody.txt'
    file_name2 = '../PA 1-2 Student Data/pa2-'+data_type+'-'+ num + '-calreadings.txt'

    Nd, Na, Nc, data1 = ReadData1(file_name1)
    ND, NA, NC, NF, data2 = ReadData2(file_name2)

    d = data1[0:Nd]
    a = data1[Nd:Na+Nd]
    c = data1[Na+Nd:Nd+Na+Nc]

    c_h = np.concatenate((c,np.ones([NC,1])), axis = 1)

    FD = np.zeros((4,4,NF))
    FA = np.zeros((4,4,NF))
    C_exp = np.zeros((4,NC,NF))
    C_ori = np.zeros((3,NC,NF))
    C_exp_no = np.zeros((3,NC,NF))

    t = 0
    for i in range(0, len(data2), ND+NA+NC):
       D = data2[i:i+ND]
       A = data2[i+ND:i+ND+NA]
       C = data2[i+ND+NA:i+ND+NA+NC]
       FD[:,:,t] = point_cloud_registration(d, D)
       FA[:,:,t] = point_cloud_registration(a, A)
       C_exp[:,:,t] = np.matmul(np.matmul(invtrans(FD[:,:,t]),FA[:,:,t]),c_h.T)
       C_exp_no[:,:,t] = C_exp[0:3,:,t]
       C_ori[:,:,t] = C.T  
       t += 1
    # C_expected = C_exp_no.reshape(3,NC*NF).T
    # C_original = C_ori.reshape(3,NC*NF).T


    Cori = C_ori[:,:,0]
    Cexp = C_exp_no[:,:,0]
    for i in range(1, NF):
        Cori = np.concatenate((Cori, C_ori[:,:,i].data), axis=1)
        Cexp = np.concatenate((Cexp, C_exp_no[:,:,i].data), axis=1)
    return Cexp.T, Cori.T
    # return C_expected, C_original








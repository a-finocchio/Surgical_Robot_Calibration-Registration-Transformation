import numpy as np
import sys
sys.path.append("..")
from math_pkg import *

def ReadData(filename):  
    with open(filename, mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        datalist = list(csv_reader)
    NS = int(datalist[0][0])
    Nsamps = int(datalist[0][1])
    datalist.pop(0)
    data = np.array([[float(j) for j in i] for i in datalist])
    return NS,Nsamps,data

test_char = 'A'
data_type = 'Debug'

def ReadData1(filename):
    datalist = [] 
    with open(filename, mode = 'r') as csv_file:
        for line in csv_file:
            line = line.split()
            datalist.append(line)
    N = int(datalist[0][0])
    datalist.pop(0)
    data = np.array([[float(j) for j in i] for i in datalist])
    a = data[0:N]
    tip = data[N]
    return N,a,tip.reshape(3,1)

def ReadMesh(filename):
    datalist = [] 
    with open(filename, mode = 'r') as csv_file:
        for line in csv_file:
            line = line.split()
            datalist.append(line)
    Nv = int(datalist[0][0])
    Nt = int(datalist[Nv+1][0])
    datalist.pop(0)
    datalist.pop(Nv)
    v = np.array([[float(j) for j in i] for i in datalist[0:Nv]])
    tri = np.array([[int(j) for j in i] for i in datalist[Nv:]])
    return Nv,v,Nt,tri
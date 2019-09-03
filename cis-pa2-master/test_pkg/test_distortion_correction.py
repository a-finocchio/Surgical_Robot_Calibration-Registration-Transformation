import numpy as np
import sys
sys.path.append("..")
from math_pkg import *

# use for debug the distortion correction function
test_char = 'a'


def ReadData(filename):  
    with open(filename, mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        datalist = list(csv_reader)
    Ng = int(datalist[0][0])
    Nf = int(datalist[0][1])
    datalist.pop(0)
    data = np.array([[float(j) for j in i] for i in datalist])
    return Ng,Nf,data

# load data
c_expect,c_measure = import_calibrate_data(test_char)

# calculate the distortion correction function
coeff = distor_coef_matrix(c_expect,c_measure,5)

# dewarp data
Ng, Nf, data = ReadData('../PA 1-2 Student Data/pa2-debug-'+ test_char +'-empivot.txt')
data = distortion_correction(coeff,data,5)

# calculate the p_dimple
g = np.zeros((Ng,3))
Fg = np.zeros((4,4,Nf))
t = 0
G0 = np.mean(data[0:Ng],axis = 0).reshape(1,3)
g[0:Ng] = data[0:Ng] - G0
for j in range (0, len(data), Ng):
	Fg[:,:,t] = point_cloud_registration(g, data[j:j+Ng])
	t += 1
print('finish')

# print result
q_EM = pivot_calibration(Fg)
P_EM_dimple = q_EM[3:6].reshape(3,1)
print (P_EM_dimple)






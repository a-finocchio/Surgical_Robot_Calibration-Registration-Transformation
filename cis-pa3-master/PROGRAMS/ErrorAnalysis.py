import numpy as np
import sys
sys.path.append("..")
from math_pkg import *

char = 'ABCDEF'

def ReadData(filename):  
    datalist = [] 
    with open(filename, mode = 'r') as csv_file:
        for line in csv_file:
            line = line.split()
            datalist.append(line)
    datalist.pop(0)
    data = np.array([[float(j) for j in i] for i in datalist])
    return data

for test_char in char:
    data = ReadData('../OUTPUT/pa3-'+ test_char +'-Output.txt')
    data_debug = ReadData('../PA 345 - Student Data/PA3-'+ test_char +'-Debug-Output.txt') 
    error = data_debug[:,6] - data[:,6]
    np.savetxt('../errors_analysis/error'+ test_char +'.txt', error, fmt='%.3f');

import numpy as np
import sys
sys.path.append("..")

char = 'ABCDEF'
char1 = 'GHJK'

def ReadData(filename):  
    datalist = [] 
    with open(filename, mode = 'r') as csv_file:
        for line in csv_file:
            line = line.split()
            datalist.append(line)
    datalist.pop(0)
    datalist.pop(0)
    data = np.array([[float(j) for j in i] for i in datalist])
    return data

def ReadData1(filename):  
    datalist = [] 
    with open(filename, mode = 'r') as csv_file:
        for line in csv_file:
            line = line.split()
            datalist.append(line)
    datalist.pop(0)
    datalist.pop(0)
    data = np.array([[float(j) for j in i] for i in datalist])
    return data


for test_char in char:
    data = ReadData('../OUTPUT/pa5-' + test_char +'-Output.txt')
    data_debug = ReadData('../PA 345 - Student Data/PA5-'+ test_char +'-Debug-Output.txt') 

    mean_our = np.mean(data[:,6])
    # print(mean_our)
    mean_debug = np.mean(data_debug[:,6])
    # print(mean_debug)
    error = - mean_debug + mean_our

    out = np.array([mean_our, mean_debug, error])
    # print(out)


    np.savetxt('../errors_analysis/error'+ test_char +'.txt', out.T, fmt='%.3f');


for test_char in char1:
    data = ReadData1('../OUTPUT/pa5-' + test_char +'-Output.txt')
    # data_debug = ReadData('../PA 345 - Student Data/PA5-'+ test_char +'-Debug-Output.txt') 

    mean_our1 = np.mean(data[:,6])
    # print(mean_our)
    std_our1 = np.std(data[:,6])
    # print(mean_debug)
    # error = - mean_debug + mean_our

    out1 = np.array([mean_our1, std_our1])
    print(out1)


    np.savetxt('../errors_analysis/error'+ test_char +'.txt', out1.T, fmt='%.3f');    
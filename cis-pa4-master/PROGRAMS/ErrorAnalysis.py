import numpy as np
import sys
sys.path.append("..")
from math_pkg import *

char = 'ABC'


def ReadData(filename):
    datalist = []
    with open(filename, mode='r') as csv_file:
        for line in csv_file:
            line = line.split()
            datalist.append(line)
    datalist.pop(0)
    data = np.array([[float(j) for j in i] for i in datalist])
    return data


for test_char in char:
    data = ReadData('../OUTPUT/pa4-' + test_char + '-Output.txt')
    data_debug = ReadData('../PA 345 - Student Data/PA4-' +
                          test_char + '-Debug-Output.txt')
    ourmean = np.mean(np.abs(data[:, 6]))
    debugmean = np.mean(np.abs(data_debug[:, 6]))
    error = - np.mean(data_debug[:, 6] - data[:, 6])
    allerror = np.array([ourmean, debugmean, error])
    print(ourmean, '\n\n', debugmean, '\n\n', error, '\n')
    np.savetxt('../errors_analysis/error' +
               test_char + '.txt', allerror, fmt='%.6f')

# char = 'GHJK'
# for test_char in char:
#     data = ReadData('../OUTPUT/pa4-' + test_char + '-Output.txt')
#     # data_debug = ReadData('../PA 345 - Student Data/PA4-' +
#     #                       test_char + '-Debug-Output.txt')
#     ourmean = np.mean(np.abs(data[:, 6]))
#     # debugmean = np.mean(np.abs(data_debug[:, 6]))
#     # error = - np.mean(data_debug[:, 6] - data[:, 6])
#     std_dev = np.std(data[:, 6])
#     allerror = np.array([ourmean, std_dev])
#     print(ourmean, '\n\n', std_dev, '\n')
#     np.savetxt('../errors_analysis/error' +
#                test_char + '.txt', allerror, fmt='%.6f')
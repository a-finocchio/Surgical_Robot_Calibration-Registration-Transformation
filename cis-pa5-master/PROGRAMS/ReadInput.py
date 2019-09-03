import numpy as np
import sys
sys.path.append("..")
import csv

# Input: filename  *SampleReadingsTest.txt in the data directory
# Output: NS the sum of points recorded in A,B,D frames, Nsamps number of sample frames, data point cloud data in the frames


def ReadData(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        datalist = list(csv_reader)
    NS = int(datalist[0][0])
    Nsamps = int(datalist[0][1])
    datalist.pop(0)
    data = np.array([[float(j) for j in i] for i in datalist])
    return NS, Nsamps, data

# Input:  filename  *Problem3-Body*.txt in the data directory
# Output: N number of markers, a xyz coordinates of marker LEDs in body coordinates, tip xyz coordinates of tip in body coordinates


def ReadData1(filename):
    datalist = []
    with open(filename, mode='r') as csv_file:
        for line in csv_file:
            line = line.split()
            datalist.append(line)
    N = int(datalist[0][0])
    datalist.pop(0)
    data = np.array([[float(j) for j in i] for i in datalist])
    a = data[0:N]
    tip = data[N]
    return N, a, tip.reshape(3, 1)

# Input:  filename Problem3MeshFile.sur in the data directory
# Output: Nv number of vertices, v xyz coordinates of vertices in CT coordinates, Nt number of triangles, tri vertex indices of the three vertices for each triangle


def ReadMesh(filename):
    datalist = []
    with open(filename, mode='r') as csv_file:
        for line in csv_file:
            line = line.split()
            datalist.append(line)
    Nv = int(datalist[0][0])
    Nt = int(datalist[Nv + 1][0])
    datalist.pop(0)
    datalist.pop(Nv)
    v = np.array([[float(j) for j in i] for i in datalist[0:Nv]])
    tri = np.array([[int(j) for j in i] for i in datalist[Nv:]])
    return Nv, v, Nt, tri

# Input:  filename Problem5Modes.txt in the data directory
# Output: xyz coordinates of vertices in CT coordinates of mode 0 to 6


def ReadModes(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        datalist = list(csv_reader)
    datalist.pop(0)
    mode = np.zeros([1568, 3, 7])
    for i in range(7):
        datalist.pop(1568 * i)
        mode[:, :, i] = np.array([[float(j) for j in k]
                                  for k in datalist[1568 * i:1568 * (i + 1)]])
    return mode

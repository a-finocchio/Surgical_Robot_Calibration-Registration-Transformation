import numpy as np
import sys
from ReadInput import *
from ConstructBoundingSphere import *
from FindClosestPoint import *
from BoundingBoxTreeNode import *
from tryICP import *
sys.path.append("..")

# Read Coordinates of Body A
NA, a, tipA = ReadData1('../PA 345 - Student Data/Problem4-BodyA.txt')

# Read Coordinates of Body B
NB, b, tipB = ReadData1('../PA 345 - Student Data/Problem4-BodyB.txt')

# Read Coordinates of mesh file
Nv, v, Nt, tri = ReadMesh('../PA 345 - Student Data/Problem4MeshFile.sur')

# Construct bounding sphere
sphere = ConstructBoundingSphere(v, tri)

# construct octree
octree = BoundingBoxTreeNode(sphere, Nt)

char = 'ABCDEFGHJK'
for test_char in char:
    if test_char in 'ABCDEF':
        data_type = 'Debug'
    else:
        data_type = 'Unknown'

    # Read data in sample reading file
    NS, Nsamps, data = ReadData('../PA 345 - Student Data/PA4-' +
                                test_char + '-' + data_type + '-SampleReadingsTest.txt')
    ND = NS - NA - NB

    # Perform point could to point cloud registration
    # to find FA and FB as well as the d
    FA = np.zeros((4, 4, Nsamps))
    FB = np.zeros((4, 4, Nsamps))
    d = np.zeros((4, 1, Nsamps))
    t = 0
    for i in range(0, len(data), NS):

        # Point cloud to point cloud registration
        FA[:, :, t] = point_cloud_registration(a, data[i:i + NA])
        FB[:, :, t] = point_cloud_registration(b, data[i + NA:i + NA + NB])

        # Find out the coordinates of d
        d[:, :, t] = np.matmul(np.matmul(np.linalg.inv(
            FB[:, :, t]), FA[:, :, t]), np.concatenate((tipA, np.ones([1, 1])), axis=0))
        t += 1

    s, c = icp(Nsamps,d,sphere,octree)

    # Find how close is our point c to point s
    d_cs = np.linalg.norm(c - s, axis=0)

    #  ========================== OUTPUT ===========================

    with open('../OUTPUT/pa4-' + test_char + '-Output.txt', 'w') as file:
        file.write(str(Nsamps) + ', pa4-' + test_char + '-Output.txt\n')
        for i in range(Nsamps):
            line = ["{0:.2f}".format(s[0][i]), "{0:.2f}".format(s[1][i]), "{0:.2f}".format(s[2][i]), "{0:.2f}".format(
                c[0][i]), "{0:.2f}".format(c[1][i]), "{0:.2f}".format(c[2][i]), "{0:.3f}".format(d_cs[i])]
            line_new = '{:>8}  {:>8}  {:>8}  {:>10}  {:>8}  {:>8}  {:>8}'.format(
                line[0], line[1], line[2], line[3], line[4], line[5], line[6])
            file.write(str(line_new) + '\n')
    print('pa4-' + test_char + '-Output.txt generated!')

print("Evaulated all data!")

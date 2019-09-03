import numpy as np
import sys
from ReadInput import *
import time
sys.path.append("..")


def icp(Nsample, d, spheres,octree):

    dd = np.transpose(d[0:4, :, :], (2, 0, 1))
    dd = np.reshape(dd, (dd.shape[0], dd.shape[1])).T

    # initialization
    F_reg = np.identity(4)
    c = np.zeros((3, Nsample))
    s = np.zeros((3, Nsample))
    Bound_initial = np.zeros((1, Nsample))

    error_pos = 1
    error_pre = 10
    iter = 0
    # Begin Interation
    temp_error = error_pre / error_pos

    while temp_error < 0.999 or temp_error > 1.0:

        # check break point
        # temp_error = error_pre / error_pos
        # if temp_error > 0.9 and temp_error < 1.0:
        #     break

        # calculate the sample
        s = np.matmul(F_reg, dd)[0:3, :]
        

        for j in range(Nsample):
            # Find the closest point to pt for each loop
            pt = s[:, j]
            if iter == 0:
                bound = np.linalg.norm(spheres[0].Center - pt)
            else:
                bound = Bound_initial[0, j]

            temp_c = spheres[0].Center
            bound, temp_c = octree.FindCP(pt, bound, temp_c)

            # store the closest point to pt into c
            c[:, j] = temp_c
            Bound_initial[0, j] = np.linalg.norm(pt - temp_c) + 0.5

        # Calculate the F_reg for this sample
        
        F = point_cloud_registration(s.T, c.T)
        F_reg = np.matmul(F, F_reg)
        
        # Calculate the error term
        error_pos = error_pre
        error_pre = 0
        for i in range(Nsample):
            error_pre = error_pre + np.linalg.norm(c[:, i] - s[:, i])
        error_pre = error_pre / Nsample
        temp_error = error_pre / error_pos

    if iter == 0:
        iter = 1

    return s, c

# calculate the angle array from a 3*3 rotation matrix
#-----------------------------------------------


import numpy as np
import math
import sys
sys.path.append("..")
from math_pkg import *

def rot_check(R) :
    R_t = np.transpose(R)
    Identity = np.dot(R_t, R)
    I = np.identity(3, dtype = R.dtype)
    n = np.linalg.norm(I - Identity)
    return n < 1e-6
 
 

def rot_2_angle(R) :
 
    assert(rot_check(R))
     
    sqt = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
     
    singular = sqt < 1e-8
 
    if  not singular :
        x = math.atan2(R[2,1] , R[2,2])
        y = math.atan2(-R[2,0], sqt)
        z = math.atan2(R[1,0], R[0,0])
    else :
        x = math.atan2(-R[1,2], R[1,1])
        y = math.atan2(-R[2,0], sqt)
        z = 0
 
    return np.array([x, y, z])
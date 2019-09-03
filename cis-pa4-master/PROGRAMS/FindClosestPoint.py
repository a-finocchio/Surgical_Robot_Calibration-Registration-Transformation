import numpy as np
from ProjectOnSegment import *
def FindClosestPoint(a,tri):

    
    p = tri[0].reshape((3,1))
    q = tri[1].reshape((3,1))
    r = tri[2].reshape((3,1))
    A = np.concatenate((q-p,r-p), axis = 1)
    b = a - p
    x = np.matmul(np.matmul(np.linalg.inv(np.matmul(A.T,A)),A.T),b)
    c_temp = np.matmul(A,x) + p    
    if x[0] >= 0 and x[1] >= 0 and np.sum(x) <= 1:
        c = c_temp
    elif x[0] < 0:
        c = ProjectOnSegment(c_temp,r,p)
    elif x[1] < 0:
        c = ProjectOnSegment(c_temp,p,q)
    else:
        c = ProjectOnSegment(c_temp,q,r)
    return c
import numpy as np
import sys
sys.path.append("..")
from math_pkg import *



# test combine
a = 6
b = 2
print(combine(a,b))

# test load data
c1,c2 = import_calibrate_data('a')
print(N)

# test scale to box
u1 = scale_2_box(c1)
print(u)

# test F matrix
F_mat = F_matrix(5, u1)
print(F_mat[:,0].T)















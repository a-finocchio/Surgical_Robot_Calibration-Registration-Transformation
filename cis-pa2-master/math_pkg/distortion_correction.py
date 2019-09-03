import numpy as np
import sys
# sys.path.append("..")
# sys.path.append(".")
from math_pkg import *
import numpy.linalg as nplinear
import scipy 

        
        
def combine(n,m):
    result = scipy.misc.comb(n,m,exact=True)
    return result


def Bernstein_polynomials(order,k,u):
	v = 1 - u
	order_k = order - k
	com_value = combine(order,k)
	u_p = np.power(v,order_k)
	v_p = np.power(u,k)
	B_Nk = com_value * u_p * v_p		
	return B_Nk	


def F_matrix(order, u):
    N = u.shape[0]
    count = order+1
    col = count * count * count
    F_matrix = np.zeros([N, int(col)])
    for i in range(N):
        col_iter = 0
        for x in range(count):
            for y in range(count):
                for z in range(count):
                    temp_a = Bernstein_polynomials(order,x,u[i,0])
                    temp_b = Bernstein_polynomials(order,y,u[i,1])
                    temp_c = Bernstein_polynomials(order,z,u[i,2])
                    F_matrix[i][col_iter] = temp_a * temp_b * temp_c
                    col_iter = col_iter + 1
    return F_matrix


def scale_2_box(data):
    q_min = np.amin(data,0)
    q_max = np.amax(data,0)
    diff = q_max - q_min
    u = (data - q_min) / diff
    return u  


def distor_coef_matrix(data_measure,data_expect,order):
	u = scale_2_box(data_measure)
	P = scale_2_box(data_expect)
	F = F_matrix(order, u)
	C = nplinear.lstsq(F,P,rcond=None)
	return C[0]


def distortion_correction(C,data_warp,order):
	q_min = np.amin(data_warp,0)
	q_max = np.amax(data_warp,0)
	diff = q_max - q_min
    
	u = scale_2_box(data_warp)
	F = F_matrix(order, u)
	# C = distor_coef_matrix(train_data_measure,train_data_expect,order)

	P_expect = np.matmul(F,C)
	data_dewarp = P_expect * diff +q_min
                                       
	return data_dewarp



# def distor_coef_matrix(data_measure,data_expect,order):
#     u = scale_2_box(data_measure)
#     P = scale_2_box(data_expect)
#     F = F_matrix(order, u)
#     C = nplinear.lstsq(F,P,rcond=None)
#     return C[0]


# def distortion_correction(C,data_warp,order):
#     q_min = np.amin(data_warp,0)
#     q_max = np.amax(data_warp,0)
#     diff = q_max - q_min
    
#     u = scale_2_box(data_warp)
#     F = F_matrix(order, u)
    

#     P_expect = np.matmul(F,C)
#     data_dewarp = P_expect * diff +q_min
                                       
#     return data_dewarp

# calculate the F rigid body transformation matrix between two point clouds
# method: Method due to K. Arun, et. al., IEEE PAMI, Vol 9, no 5, pp 698-700, Sept 1987
#-----------------------------------------------


import numpy as np
#two point cloud  -> find transform matrix
def point_cloud_registration(A,B):
    
    # Dimension Check
    assert A.shape == B.shape

    # get number of dimensions
    m = A.shape[1]

    # get the center of point cloud a and b
    A_center = np.mean(A, axis=0)
    B_center = np.mean(B, axis=0)
    
    # get the local coordinates of each point cloud from it centers
    
    A_local = A - A_center
    B_local = B - B_center

    # Method due to K. Arun, et. al., IEEE PAMI, Vol 9, no 5, pp 698-700, Sept 1987
    
    # Direct Techniques to solve for R
    H = np.dot(A_local.T, B_local)
    U, S, Vt = np.linalg.svd(H)
    R = np.dot(Vt.T, U.T)
 
    # special reflection case
    if np.linalg.det(R) < 0:
       Vt[m-1,:] *= -1
       R = np.dot(Vt.T, U.T)
        
    # Check for det
    detR = np.linalg.det(R)
    assert (detR < 1.001 and detR > 0.999),"The determinant of R should be 1."

    # find translation
    t = B_center.T - np.dot(R,A_center.T)

    # combine R,t as a homogeneous transformation
    T = np.identity(m+1)
    T[:m, :m] = R
    T[:m, m] = t    
    
    return T
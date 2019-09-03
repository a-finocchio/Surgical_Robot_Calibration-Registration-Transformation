# Generate rotation matrix for specific xyz axis 
#-----------------------------------------------

import numpy as np

def rotx(rad):
    Rx = np.array([[1,0,0],[0,np.cos(rad),-np.sin(rad)],[0,np.sin(rad),np.cos(rad)]])
    return Rx

def roty(rad):
    Ry = np.array([[np.cos(rad),0,np.sin(rad)],[0,1,0],[-np.sin(rad),0,np.cos(rad)]])
    return Ry

def rotz(rad):
    Rz = np.array([[np.cos(rad),-np.sin(rad),0],[np.sin(rad),np.cos(rad),0],[0,0,1]])
    return Rz


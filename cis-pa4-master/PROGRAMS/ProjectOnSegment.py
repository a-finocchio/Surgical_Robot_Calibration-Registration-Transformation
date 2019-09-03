import numpy as np
def ProjectOnSegment(c,p,q):
    lamb = np.matmul((c-p).T,(q-p))/np.matmul((q-p).T,(q-p))
    lamb_s = max(0,min(lamb,1))
    c_s = p + lamb_s * (q - p)
    return c_s
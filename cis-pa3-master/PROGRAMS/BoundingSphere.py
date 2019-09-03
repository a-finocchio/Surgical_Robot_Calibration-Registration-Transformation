import numpy as np
def BoundingSphere(v,tri):
    N = v.shape[0]
    M = tri.shape[0]
    qq = np.zeros((M,3))
    rr = np.zeros((M,1))
    for i in range(M):
        p = v[tri[i][0]]
        q = v[tri[i][1]]
        r = v[tri[i][2]]
        pq = np.linalg.norm(p - q)
        pr = np.linalg.norm(p - r)
        qr = np.linalg.norm(q - r)
        ind = np.argmax([pq,pr,qr])
        if ind == 0:
            a = p
            b = q
            c = r
        elif ind == 1:
            a = p
            b = r
            c = q
        else:
            a = q
            b = r
            c = p
        f = (a+b)/2
        u = a - f
        vv = c - f
        d = np.cross(np.cross(u,vv),u)
        gamma = (np.matmul(vv,vv) - np.matmul(u,u)) / np.matmul((2*d),(vv - u))
        if gamma <= 0:
            lamb = 0
        else:
            lamb = gamma
        qq[i] = f + lamb * d
        rr[i] = np.linalg.norm(qq[i] - a) 
    return qq,rr
import numpy as np
from Sphere import *


def ConstructBoundingSphere(v, tri):
    M = tri.shape[0]
    sphere = [Sphere() for _ in range(M)]
    Center = np.zeros((M, 3))
    Radius = np.zeros((M, 1))
    Object = np.zeros((3, 3, M))
    for i in range(M):
        p = v[tri[i][0]]
        q = v[tri[i][1]]
        r = v[tri[i][2]]
        pq = np.linalg.norm(p - q)
        pr = np.linalg.norm(p - r)
        qr = np.linalg.norm(q - r)
        ind = np.argmax([pq, pr, qr])
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
        f = (a + b) / 2
        u = a - f
        vv = c - f
        d = np.cross(np.cross(u, vv), u)
        gamma = (np.matmul(vv, vv) - np.matmul(u, u)) / \
            np.matmul((2 * d), (vv - u))
        if gamma <= 0:
            lamb = 0
        else:
            lamb = gamma
        Center[i] = f + lamb * d
        Radius[i] = np.linalg.norm(Center[i] - a)
        Object[:, :, i] = np.array([p, q, r])
        sphere[i].Center = Center[i]
        sphere[i].Radius = Radius[i]
        sphere[i].Object = Object[:, :, i]
    return sphere

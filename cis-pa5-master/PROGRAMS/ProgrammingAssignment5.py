import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("..")
from ReadInput import *
from BoundingSphere import *
from FindClosestPoint import *
from Deform_tri_set import *
from point_cloud_registration import *

# Read Coordinates of Body A
NA, a, tipA = ReadData1('../PA 345 - Student Data/Problem5-BodyA.txt')

# Read Coordinates of Body B
NB, b, tipB = ReadData1('../PA 345 - Student Data/Problem5-BodyB.txt')

# Read Coordinates of mesh file
Nv, v, Nt, tri = ReadMesh('../PA 345 - Student Data/Problem5MeshFile.sur')

# Read Modes
Mode = ReadModes('../PA 345 - Student Data/Problem5Modes.txt')

char = 'ABCDEFGHJK'
for test_char in char:
    if test_char in 'ABCDEF':
        data_type = 'Debug'
    else:
        data_type = 'Unknown'

# Read data in sample reading file
    NS, Nsamps, data = ReadData('../PA 345 - Student Data/PA5-' +
                                test_char + '-' + data_type + '-SampleReadingsTest.txt')
    ND = NS - NA - NB

    # Perform point could to point cloud registration
    # to find FA and FB as well as the d
    FA = np.zeros((4, 4, Nsamps))
    FB = np.zeros((4, 4, Nsamps))
    d = np.zeros((4, 1, Nsamps))
    t = 0
    for i in range(0, len(data), NS):
        # Point cloud to point cloud registration
        FA[:, :, t] = point_cloud_registration(a, data[i:i + NA])
        FB[:, :, t] = point_cloud_registration(b, data[i + NA:i + NA + NB])
        # Find out the coordinates of d
        d[:, :, t] = np.matmul(np.matmul(np.linalg.inv(
            FB[:, :, t]), FA[:, :, t]), np.concatenate((tipA, np.ones([1, 1])), axis=0))
        t += 1
    # Initialization
    update_Lambda = np.zeros((6, 1))
    F_reg = np.identity(4)
    dd = np.transpose(d[0:4, :, :], (2, 0, 1))
    dd = np.reshape(dd, (dd.shape[0], dd.shape[1])).T
    c = np.zeros((Nsamps, 3, 1))
    s = np.zeros((Nsamps, 3, 1))
    c_in_which_triangle = np.zeros((Nsamps, 1))
    x = []
    y = []

    # Start iteration
    for it in range(150):

        # Linear Search with Bounding Sphere
        F_reg_old = F_reg
        triangle_set = Deform_tri_set(Mode, update_Lambda, tri[:, 0:3])
        q, r = BoundingSphere(triangle_set)
        for i in range(Nsamps):
            s_1 = np.matmul(F_reg, dd[:, i])
            pt = np.transpose(s_1[0:3]).reshape([3, 1])
            s[i] = pt
            bound = np.inf
            for j in range(Nt):
                if (np.linalg.norm(q[j].reshape((3, 1)) - pt) - r[j]) <= bound:
                    h = FindClosestPoint(pt, triangle_set[j].reshape([3, 3]))
                    dist = np.linalg.norm(h - pt)
                    if dist < bound:
                        c_tmp = h
                        c_in_which_triangle[i] = int(j)
                        bound = dist
            c[i] = c_tmp
        F = point_cloud_registration(s[:, :, 0], c[:, :, 0])
        F_reg = np.matmul(F, F_reg)

        # initialization
        m = np.zeros((4, 3, 1))

        # Deformable Registration

        Lambda = update_Lambda

        # vertices index of corresponding triangles to each closest point
        t_index = tri[c_in_which_triangle.astype(int).T][0][:, 0]
        u_index = tri[c_in_which_triangle.astype(int).T][0][:, 1]
        v_index = tri[c_in_which_triangle.astype(int).T][0][:, 2]

        # compute the coefficients of three vertices to the closest point
        m_t = np.zeros([Nsamps, 3])
        m_u = np.zeros([Nsamps, 3])
        m_v = np.zeros([Nsamps, 3])
        para = np.zeros([3, 1, Nsamps])
        S = np.zeros((Nsamps * 3, 1))
        Q = np.zeros((Nsamps * 3, 6))
        for i in range(Nsamps):
            triangle_idx_c = c_in_which_triangle[i]
            m_t[i, :] = triangle_set[triangle_idx_c.astype(int).T][0][0:3]
            m_u[i, :] = triangle_set[triangle_idx_c.astype(int).T][0][3:6]
            m_v[i, :] = triangle_set[triangle_idx_c.astype(int).T][0][6:9]

            # linear system for a b c
            m[:, 0, :] = np.c_[m_t[i, :].reshape([1, 3]), 1].T
            m[:, 1, :] = np.c_[m_u[i, :].reshape([1, 3]), 1].T
            m[:, 2, :] = np.c_[m_v[i, :].reshape([1, 3]), 1].T
            c_1 = np.c_[c[i, :, 0].reshape([1, 3]), 1].T
            A = m[:, :, 0]
            bb = c_1
            para[:, :, i] = np.matmul(
                np.matmul(np.linalg.inv(np.matmul(A.T, A)), A.T), bb)
            # samples' position - mode 0
            m_t0 = Mode[t_index[i], :, 0]
            m_u0 = Mode[u_index[i], :, 0]
            m_v0 = Mode[v_index[i], :, 0]
            qi0 = para[0, :, i] * m_t0 + para[1, :, i] * \
                m_u0 + para[2, :, i] * m_v0
            qi0 = qi0.reshape([1, 3])

            temp_S_new = s[i, :, :].T - qi0
            S[i * 3:(i + 1) * 3, :] = temp_S_new.T

            Q_row = np.zeros((3, 6))
            for j in range(6):
                m_tj = Mode[t_index[i], :, j + 1]
                m_uj = Mode[u_index[i], :, j + 1]
                m_vj = Mode[v_index[i], :, j + 1]
                qij = para[0, :, i] * m_tj + para[1, :, i] * \
                    m_uj + para[2, :, i] * m_vj
                Q_row[:, j] = qij

            Q[i * 3:(i + 1) * 3, :] = Q_row

        update_Lambda = np.matmul(
            np.matmul(np.linalg.inv(np.matmul(Q.T, Q)), Q.T), S)
        d_cs = np.linalg.norm(c - s, axis=1)
        x.append(it + 1)
        y.append(np.mean(d_cs))
        if np.linalg.norm(F_reg - F_reg_old) < 0.01 and np.linalg.norm(Lambda - update_Lambda) < 0.1:
            print("Converged")
            break
    # Find how close is our point c to point s
    d_cs = np.linalg.norm(c - s, axis=1)

    #  ========================== OUTPUT ===========================
    fig = plt.figure()
    ax = plt.subplot(111)
    plt.plot(x, y)
    plt.xlabel('Iteration')
    plt.ylabel('Error')
    plt.show()
    fig.savefig('../Figure/Err_' + test_char + '.png')
    with open('../OUTPUT/pa5-' + test_char + '-Output.txt', 'w') as file:
        file.write(str(Nsamps) + ', pa5-' + test_char + '-Output.txt, 6 \n')
        strlam = ["{0:.4f}".format(update_Lambda[0][0]), "{0:.4f}".format(update_Lambda[1][0]), "{0:.4f}".format(
            update_Lambda[2][0]), "{0:.4f}".format(update_Lambda[3][0]), "{0:.4f}".format(update_Lambda[4][0]), "{0:.4f}".format(update_Lambda[5][0])]
        lam_new = '{:>8}  {:>8}  {:>8}  {:>8}  {:>8}  {:>8}'.format(
            strlam[0], strlam[1], strlam[2], strlam[3], strlam[4], strlam[5])
        file.write(str(lam_new) + '\n')
        for i in range(Nsamps):
            line = ["{0:.2f}".format(s[i][0][0]), "{0:.2f}".format(s[i][1][0]), "{0:.2f}".format(s[i][2][0]), "{0:.2f}".format(
                c[i][0][0]), "{0:.2f}".format(c[i][1][0]), "{0:.2f}".format(c[i][2][0]), "{0:.3f}".format(d_cs[i][0])]
            line_new = '{:>8}  {:>8}  {:>8}  {:>10}  {:>8}  {:>8}  {:>8}'.format(
                line[0], line[1], line[2], line[3], line[4], line[5], line[6])
            file.write(str(line_new) + '\n')
    print('pa5-' + test_char + '-Output.txt generated!')

print("Evaulated all data!")

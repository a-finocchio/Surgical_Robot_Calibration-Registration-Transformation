import numpy as np


def Deform_tri_set(Mode, Lambda, tri):

    # update the vertices set by considering current deformation
    vertices_set = Mode[:, :, 0]

    temp_iter1 = Mode.shape[2]
    for i in range(1, temp_iter1):

        vertices_set = vertices_set + Lambda[i - 1] * Mode[:, :, i]

    # update the triangle set
    temp_iter2 = tri.shape[0]
    tri_set = np.zeros((temp_iter2, 9))
    for i in range(temp_iter2):

        temp_a = vertices_set[tri[i, 0], :].reshape([1, 3])
        temp_b = vertices_set[tri[i, 1], :].reshape([1, 3])
        temp_c = vertices_set[tri[i, 2], :].reshape([1, 3])
        tri_set[i, :] = np.c_[temp_a, temp_b, temp_c]
    return tri_set

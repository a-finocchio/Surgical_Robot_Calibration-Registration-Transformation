import numpy as np


class Sphere(object):
    def __init__(self):
        self.Center = np.zeros((3, 1))
        self.Radius = 0
        self.Object = np.zeros((3, 3))

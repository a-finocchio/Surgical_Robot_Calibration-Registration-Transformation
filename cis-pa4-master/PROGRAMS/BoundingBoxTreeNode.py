import numpy as np
from FindClosestPoint import *
from Sphere import *

# Empty Octree Class


class trees:

    def __init__(self):
        pass

# Class of Bounding box octree


class BoundingBoxTreeNode:

    # Initialize properties
    def __init__(self, BS, ns):

        # Bool indicating whether currrent node has subtrees
        self.HaveSubTrees = True
        # Subtrees (1*8 BoundingBoxTreeNode) divided by Center
        self.SubTrees = [trees()] * 8
        # All the spheres inside current node
        self.Spheres = BS
        # Number of spheres in current bounding box node
        self.nSpheres = ns
        centers = np.zeros((3, 1, ns))
        rads = np.zeros((1, ns))
        for i in range(ns):
            centers[:, :, i] = BS[i].Center.reshape((3, 1))
            rads[0, i] = BS[i].Radius
        # Splitting point of current bounding box node

        self.Center = np.mean(centers, axis=2).reshape((3, 1))
        # The maximum radius of the bounding spheres
        self.MaxRadius = np.max(rads)
        # Upper bound of the bounding box
        self.UB = np.max(centers, axis=2).reshape((3, 1))
        # Lower bound of the bounding box
        self.LB = np.min(centers, axis=2).reshape((3, 1))
        self.constructSubTrees()

    # Construct subtrees to the BoundingBoxTreeNode object passed in
    def constructSubTrees(self):
        minCount = 8
        minDiag = 8
        if (self.nSpheres < minCount) \
                and (np.linalg.norm(self.UB - self.LB) < minDiag):
            self.HaveSubTrees = False
            return
        self.HaveSubTrees = True
        numSpheres = self.SplitSort()
        pos = 0

        for i in range(8):
            if numSpheres[i] == 0:
                self.SubTrees[i].nSpheres = 0
                continue

            self.SubTrees[i] = BoundingBoxTreeNode(
                self.Spheres[pos: numSpheres[i] + pos], numSpheres[i])
            pos = pos + numSpheres[i]

    # Sort the spheres in current node according to their spatial position
    def SplitSort(self):
        # initializing
        numSpheres = np.zeros(8, dtype=int)
        sorted = 0
        # Get necessary parameters
        NS = len(self.Spheres)
        xS = self.Center[0]
        yS = self.Center[1]
        zS = self.Center[2]
        # initialize the SortedSpheres
        SortedSpheres = [Sphere() for i in range(NS)]

        # Split Sort for each region
        # 1
        for i in range(NS):
            if self.Spheres[i].Center[0] <= xS \
                    and self.Spheres[i].Center[1] <= yS \
                    and self.Spheres[i].Center[2] <= zS:
                sorted = sorted + 1
                numSpheres[0] = numSpheres[0] + 1
                SortedSpheres[sorted - 1] = self.Spheres[i]

        # 2
        for i in range(NS):
            if self.Spheres[i].Center[0] > xS \
                    and self.Spheres[i].Center[1] <= yS \
                    and self.Spheres[i].Center[2] <= zS:
                sorted = sorted + 1
                numSpheres[1] = numSpheres[1] + 1
                SortedSpheres[sorted - 1] = self.Spheres[i]
        # 3
        for i in range(NS):
            if self.Spheres[i].Center[0] > xS \
                    and self.Spheres[i].Center[1] > yS \
                    and self.Spheres[i].Center[2] <= zS:
                sorted = sorted + 1
                numSpheres[2] = numSpheres[2] + 1
                SortedSpheres[sorted - 1] = self.Spheres[i]

        # 4
        for i in range(NS):
            if self.Spheres[i].Center[0] <= xS \
                    and self.Spheres[i].Center[1] > yS \
                    and self.Spheres[i].Center[2] <= zS:
                sorted = sorted + 1
                numSpheres[3] = numSpheres[3] + 1
                SortedSpheres[sorted - 1] = self.Spheres[i]

        # 5
        for i in range(NS):
            if self.Spheres[i].Center[0] <= xS \
                    and self.Spheres[i].Center[1] <= yS \
                    and self.Spheres[i].Center[2] > zS:
                sorted = sorted + 1
                numSpheres[4] = numSpheres[4] + 1
                SortedSpheres[sorted - 1] = self.Spheres[i]

        # 6
        for i in range(NS):
            if self.Spheres[i].Center[0] > xS \
                    and self.Spheres[i].Center[1] <= yS \
                    and self.Spheres[i].Center[2] > zS:
                sorted = sorted + 1
                numSpheres[5] = numSpheres[5] + 1
                SortedSpheres[sorted - 1] = self.Spheres[i]
        # 7
        for i in range(NS):
            if self.Spheres[i].Center[0] > xS \
                    and self.Spheres[i].Center[1] > yS \
                    and self.Spheres[i].Center[2] > zS:
                sorted = sorted + 1
                numSpheres[6] = numSpheres[6] + 1
                SortedSpheres[sorted - 1] = self.Spheres[i]

        # 8
        for i in range(NS):
            if self.Spheres[i].Center[0] <= xS \
                    and self.Spheres[i].Center[1] > yS \
                    and self.Spheres[i].Center[2] > zS:
                sorted = sorted + 1
                numSpheres[7] = numSpheres[7] + 1
                SortedSpheres[sorted - 1] = self.Spheres[i]

        # Replace the sorted spheres with the unsorted
        self.Spheres = SortedSpheres
        return numSpheres

    # Find closest point in current node
    def FindCP(self, v, bound, closest):
        newBound = bound
        newClosest = closest
        dist = bound + self.MaxRadius
        # Check whether this node is worth searching
        flag = (v[0] > self.UB[0] + dist) or (v[1] > self.UB[1] + dist) \
            or (v[2] > self.UB[2] + dist) or (v[0] < self.LB[0] - dist) \
            or (v[1] < self.LB[1] - dist) or (v[2] < self.LB[2] - dist)
        if flag:
            return newBound, newClosest

        if self.HaveSubTrees:
            # if there's sub-trees, continue iterating FindCP on each
            # sub-trees
            for i in range(8):
                if self.SubTrees[i].nSpheres == 0:
                    continue
                newBound, newClosest = BoundingBoxTreeNode.FindCP(
                    self.SubTrees[i], v, newBound, newClosest)
        else:
            # if currrent node is the end of the tree,
            # find the closest point in this node
            for i in range(self.nSpheres):
                newBound, newClosest = BoundingBoxTreeNode.UpdateClosest(
                    self.Spheres[i], v, newBound, newClosest)
        return newBound, newClosest

    # Update the closest point in the node that do not have subtrees
    def UpdateClosest(S, v, bound, closest):
        newBound = bound
        newClosest = closest

        dist = np.linalg.norm(v - S.Center)
        # Test whether this sphere is worth calculating closest point
        if (dist - S.Radius > newBound):
            return newBound, newClosest
        # Find the closest point to v on the triangle (Object)
        cp = FindClosestPoint(v.reshape((3, 1)), S.Object)
        dist = np.linalg.norm(cp - v.reshape((3, 1)))
        # Updating
        if dist < newBound:
            newBound = dist
            newClosest = cp.reshape(3)
        return newBound, newClosest

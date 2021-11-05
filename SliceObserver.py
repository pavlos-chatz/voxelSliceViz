
import numpy as np


class SliceObserver:

    def __init__(self):
        self.voxel = None
        self.zDim = None
        self.yDim = None
        self.xDim = None
        self.currentIndex = 0

    def setVoxel(self, voxel: np.ndarray):
        """ Set the voxel to be visualized through an numpy ndarray object

        Parameters:
        voxel (np.ndarray): the voxel
        """
        self.voxel = voxel.astype(dtype=np.int8)
        shape = voxel.shape

        self.zDim = voxel.shape[0]
        self.yDim = voxel.shape[1]
        self.xDim = voxel.shape[2]

    def setCurrentIndex(self, index: int):
        """ Set the current z-index of the image to be visualized

        Parameters:
        index (int): the index
        """
        if (index >= 0 and index <= self.zDim - 1):
            self.currentIndex = index
        else:
            pass

    def incrementCurrentIndex(self):
        """ Increment z-index of the image to be visualized
        """
        if (self.currentIndex + 1 < self.zDim):
            self.currentIndex += 1
        else:
            pass


    def decrementCurrentIndex(self):
        """ Decrement z-index of the image to be visualized
        """
        if (self.currentIndex -1 >= 0):
            self.currentIndex -= 1
        else:
            pass

    def getCurrentIndex(self) -> np.ndarray:
        """ Get the current index for image to be visualized

        Returns:
         (int): index
        """
        return self.currentIndex

    def getCurrentImage(self) -> np.ndarray:
        """ Get the image to be visualized

        Returns:
         (np.ndarray): 2d image to be visualized
        """
        return self.voxel[self.currentIndex, :, :]
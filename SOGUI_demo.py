import numpy as np
from SliceObserverGUI import SliceObserverGUI

def demo():
    # create an array with the first axis being the axis along which you will move when visualizing
    shape = (10, 60, 60)
    min_ = 0
    max_ = 255
    voxel = np.random.randint(min_, max_, shape, dtype=int)

    # give the np array to the visualizer object
    SliceObserverGUI(voxel)

demo()
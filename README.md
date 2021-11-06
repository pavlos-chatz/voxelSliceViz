# voxelSliceViz
Super simple GUI to visualize voxel slices as 2D images.

### Purpose
Visualize voxels with just one line by iterating through their z dimension and looking at the 2D image corresponding to that index.  \
This was made as a tool while developing segmentation models on medical image volumes.


<img src="https://user-images.githubusercontent.com/92165053/140537547-18222ab6-3d3e-4070-ad67-889bf304e808.png" width="400" height="450">


### Usage
* Create a virtual environment and get dependencies using `pip install requirements.txt`
* Import SliceObserverGUI class in your script: `from SliceObserverGUI import SliceObserverGUI`
* Call the GUI class on your voxel: `SliceObserverGUI(voxel)`

See the demo in the SOGUI_Demo.py for example usage. 

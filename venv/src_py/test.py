from skimage import io
from skimage.external import tifffile
import matplotlib.pyplot as plt
from RSimage import RSimage
from MovingWindow import MovingWindow

img = RSimage('../data/09AUG11PILOT.tif', 1)
mw = MovingWindow('rectangle', 3, 0, img)
print('aaa')
print('bbb')
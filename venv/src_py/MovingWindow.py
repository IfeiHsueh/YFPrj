from RSimage import RSimage
import numpy as np

class MovingWindow(object):
    """
        'Moving window for satellite image'
        ~~~~~~~~~~
        This class is especially for WorldView satellite images.

        Attributes:
            owner (str): owner of this image.
            lst_wndType (list): list of window types.
            wndSize (int): size of this moving window. e.g. 1*1, 3*3, 5*5, ...
            wndStpLnth (int): step length of this moving window.
            imgPixelPosition (vector): Center coordinate of Moving Window on satellite image
    """

    lst_wndType = ['rectangle', 'circle']
    wndType = 'Did not defined!'
    wndSize = 3
    wndStpLnth = 0
    imgPixelPosition = [0, 0]

    def __init__(self, wt, ws, wsl, img:RSimage):
        """ initialize class MovingWindow

        :param wt: window type. Types in lst_wndType. e.g. 'rectangle'.
        :param ws: window size. 1*1, 3*3, ...
        :param wsl: window step length. To define how many pixels to move each time.
        :param img (RSimage): the satellite image to be scanned.
        """
        if wt in self.lst_wndType:
            self.wndType = wt
            self.wndSize = ws
            self.wndStpLnth = wsl
            self.imgWnd = np.empty((ws, ws), np.uint16)
            self.img = img

    # Getter and setter for
    @property
    def attribute(self):
        print('Window Type: ', self.wndType)
        print('Window Size: ', self.wndSize)
        print('Window Step Length: ', self.wndStpLnth)

    # @attribute.setter
    def set_attribute(self, wt:str, ws:int, wsl:int, img:RSimage):
        if wt in self.lst_wndType:
            self.wndType = wt
            self.wndSize = ws
            self.wndStpLnth = wsl
            self.imgWnd = np.empty((ws, ws), np.uint16)
            self.img = img

    # Get and set coordinate of Moving Window on satellite image
    @property
    def center(self):
        """
        To get center position of this window on satellite image
        :return: coord
        """
        coord = self.imgPixelPosition
        return coord

    @center.setter
    def center(self, imgPixelPosition):
        """
        To set center position of this window on satellite image
        :param imgPixelPosition: This is a list contains to integers
        :return: NULL
        """
        self.imgPixelPosition[0] = imgPixelPosition[0]
        self.imgPixelPosition[1] = imgPixelPosition[1]

# test
img = RSimage('../data/09AUG11PILOT.tif', 1)
mw = MovingWindow('rectangle', 3, 0, img)
# mw.attribute
# mw.set_attribute('circle', 5, 3, img)
# mw.attribute
# print('aaa')
print(mw.center)
coord = [1, 1]
mw.center = coord
print(mw.center)
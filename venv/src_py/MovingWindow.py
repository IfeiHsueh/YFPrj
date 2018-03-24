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

    __lst_wndType = ['rectangle', 'circle']
    __wndType = 'Did not defined!'
    __wndSize = 3
    __wndRadius = 1
    __wndStpLnth = 0
    __wndImg = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    __imgPixelPosition = [0, 0]

    def __init__(self, wt, ws, wsl, img: RSimage):
        """ initialize class MovingWindow

        :param wt: window type. Types in lst_wndType. e.g. 'rectangle'.
        :param ws: window size. 1*1, 3*3, ...
        :param wsl: window step length. To define how many pixels to move each time.
        :param img (RSimage): the satellite image to be scanned.
        """
        if wt in self.__lst_wndType:
            self.__wndType = wt
            self.__wndSize = ws
            self.__wndRadius = (self.__wndSize-1)/2
            self.__wndStpLnth = wsl
            self.__imgWnd = np.empty((ws, ws), np.uint16)
            self.__img = img

    # Getter and setter for
    @property
    def attribute(self):
        print('Window Type: ', self.__wndType)
        print('Window Size: ', self.__wndSize)
        print('Window Step Length: ', self.__wndStpLnth)

    # @attribute.setter
    def set_attribute(self, wt: str, ws: int, wsl: int, img: RSimage):
        if wt in self.__lst_wndType:
            self.__wndType = wt
            self.__wndSize = ws
            self.__wndStpLnth = wsl
            self.__imgWnd = np.empty((ws, ws), np.uint16)
            self.__img = img

    # Getter and setter window type of Moving Window on satellite image
    @property
    def wndtype(self):
        return self.__wndType

    @wndtype.setter
    def wndtype(self, type_str):
        self.__wndType = type_str

    # Getter and setter window size of Moving Window on satellite image
    @property
    def wndsize(self):
        return self.__wndSize

    @wndsize.setter
    def wndsize(self, size_int):
        self.__wndSize = size_int

    # Getter, setter and deleter of the parameter "__wndRadius" (window radius)
    @property
    def wndradius(self):
        return self.wndRadius

    @wndradius.setter
    def wndradius(self, wndRadius):
        self.__wndRadius = wndRadius

    @wndradius.deleter
    def wndradius(self):
        del self.__wndRadius
        self.__wndRadius = (self.__wndSize-1)/2
        print('Moving window radius are reset.')

    # Getter and setter window size of Moving Window on satellite image
    @property
    def wndstplnth(self):
        return self.__wndStpLnth

    @wndstplnth.setter
    def wndstplnth(self, length_int):
        self.__wndStpLnth = length_int

    # Getter and setter coordinate of Moving Window on satellite image
    @property
    def center(self):
        """
        To get center position of this window on satellite image
        :return: coord
        """
        coord = self.__imgPixelPosition
        return coord

    @center.setter
    def center(self, imgPixelPosition):
        """
        To set center position of this window on satellite image
        :param imgPixelPosition: This is a list contains to integers
        :return: NULL
        """
        self.__imgPixelPosition[0] = imgPixelPosition[0]
        self.__imgPixelPosition[1] = imgPixelPosition[1]


def main():
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


if __name__ == '__main__':
    main()
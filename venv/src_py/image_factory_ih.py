"""
This python file is to store image factory
"""
from RSimage import RSimage
from MovingWindow import MovingWindow


class ImageFactory(object):
    __coords = [[0, 0],
                     [0, 0]]

    def __init__(self, image: RSimage, movingwindow, coords):
        """ initialize class ImageFactory

        :param image: satellite image to be used
        :param movingwindow: the moving window, which will be applied on the imagery
        """
        self.__image = image
        self.__movingwindow = movingwindow
        if not coords:
            # coords is empty
            coords = [[0, 0],
                      [0, 0]]
        self.__coords = coords

    # Setter and Getter of target image
    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, imagedata):
        self.__image = imagedata

    # Setter and Getter of moving window
    @property
    def mwindow_config(self):
        return self.__movingwindow

    @mwindow_config.setter
    def mwindow_config(self, movingwindow):
        """
        change moving window
        :param movingwindow: class implementation of MovingWindow
        :return: NULL
        """
        self.__movingwindow = movingwindow

    # Getter, setter and deleter of coordinates
    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, coords):
        self.__coords = coords

    @coords.deleter
    def coords(self):
        del self.__coords
        self.__coords = [[0, 0],
                         [0, 0]]
        print('Coordinates of targets are reset.')

    # Add a input into list __coords
    def addcoord(self):
        pass

    def execute_mwindow(self):
        """
        run moving window on this image
        :return:
        """
        wnd = self.__movingwindow
        img = self.__image
        imgsize = img.imgSize
        coords = self.__coords
        size_coords = len(coords)

        print(imgsize)
        if self.__movingwindow.wndtype == 'rectangle':
            for i in range(0,size_coords):
                xcoord = coords[i][0]
                ycoord = coords[i][1]
                if (xcoord - wnd.wndsize + 1) >= 0 and (ycoord - wnd.wndsize + 1) >= 0:
                    wnd.center = [xcoord, ycoord]
                    
                else:
                    print('Out of boundary!')
                    return
        else:
            print('Did not defined. More codes are required here!')


def main():
    # test
    img = RSimage('../data/09AUG11PILOT.tif', 1)
    mw = MovingWindow('rectangle', 3, 0, img)
    coords = [[2, 3],
              [4, 5]]
    imf = ImageFactory(img, mw, coords)
    #del imf.coords
    imf.execute_mwindow()


if __name__ == '__main__':
    main()

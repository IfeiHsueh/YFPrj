"""
This python file is to store image factory
"""
from RSimage import RSimage
from MovingWindow import MovingWindow

class ImageFactory(object):

    def __init__(self, image:RSimage, movingwindow):
        """ initialize class ImageFactory

        :param image:
        :param movingwindow:
        """
        self.__image = image
        self.__movingwindow = movingwindow
        self.__coords = [0, 0]

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

    def execute_mwindow(self):
        """
        run moving window on this image
        :return:
        """
        if self.__movingwindow.wndtype == 'rectangle':
            wnd = self.__movingwindow
            img = self.__image
            imgsize = img.imgSize
            print(imgsize)
        else:
            print('Did not defined. More codes are required here!')

def main():
    # test
    img = RSimage('../data/09AUG11PILOT.tif', 1)
    mw = MovingWindow('rectangle', 3, 0, img)
    imf = ImageFactory(img, mw)
    imf.execute_mwindow()

if __name__ == '__main__':
    main()

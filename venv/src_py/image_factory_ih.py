"""
This python file is to store image factory
"""
from RSimage import RSimage

class ImageFactory(object):

    def __init__(self, image:RSimage, movingwindow):

        self.image = image
        self.movingwindow = movingwindow
        self.width = image
        self.coords = coords

    # Setter and Getter of target image
    @property
    def image(self):
        return self.image

    @image.setter
    def image(self, imageData):
        self.image = imageData

    # Setter and Getter of moving window
    @property
    def mwindow_config(self):
        return self.movingwindow

    @mwindow_config.setter
    def mwindow_config(self, movingwindow):
        """
        change moving window
        :param movingwindow: class implementation of MovingWindow
        :return: NULL
        """
        self.movingwindow = movingwindow

    def mwindow(self):
        """
        run moving window on this image
        :return:
        """

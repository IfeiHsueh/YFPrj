"""
This python file is to store image factory
"""
from RSimage import RSimage

class ImageFactory(object):

    def __init__(self, image:RSimage, movingwindow):
        self.image = image
        self.movingwindow = movingwindow
        self.width = image

    # Setter and Getter of target image
    @property
    def image(self):
        return self.image

    @image.setter
    def image(self, imageData):
        self.image = imageData

    # Setter and Getter of moving window
    @property
    def mwindow(self):
        return self.movingwindow

    @mwindow.setter
    def mwindow(self, movingwindow):
        self.movingwindow = movingwindow

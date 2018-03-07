from skimage import io
from skimage.external import tifffile
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class RSimage(object):
    """
    'Multispectral satellite image'
    ~~~~~~~~~~
    This class is especially for WorldView satellite images.

    Attributes:
        owner (str): owner of this image.
        imageName (str): name of this image.
        imageDir (str): relative directory of this image.
        lst_bandNames (list): list of band names.
        imgDict (dictionary): dictionary of image bands.
    """

    owner = 'Not Defined'
    imageName = 'Not Defined'
    imageDir = 'Not indicated'
    type = 0
    lst_bandNames = ['red', 'nir', 'green', 'blue']
    band1 = np.empty((2000, 2000), np.uint16)
    band2 = np.empty((2000, 2000), np.uint16)
    band3 = np.empty((2000, 2000), np.uint16)
    band4 = np.empty((2000, 2000), np.uint16)
    imgDict = {lst_bandNames[0]: band1, lst_bandNames[1]: band2, lst_bandNames[2]: band3, lst_bandNames[3]: band4}

    def __init__(self, imageDir, type):
        self.imageDir = imageDir
        self.type = type
        self.data = tifffile.imread(imageDir)
        self.imgDict[self.lst_bandNames[0]] = self.data[0]
        self.imgDict[self.lst_bandNames[1]] = self.data[1]
        self.imgDict[self.lst_bandNames[2]] = self.data[2]
        self.imgDict[self.lst_bandNames[3]] = self.data[3]

    def __set_name__(self, owner, name):
        self.owner = owner
        self.imageName = name

    #   Getter and setter for attributes
    @property
    def attributes(self):
        print(self.imageName)
        print(self.imageDir)

    @attributes.setter
    def attributes(self, imageName, imageDir):
        self.imageName = imageName
        self.imageDir = imageDir

    #   Getter and setter for bandData
    # @property
    # def bandData(self, bandName):
    #     if bandName in self.lst_bandNames:
    #         return self.imgDict[bandName]
    #     else:
    #         raise ValueError('Do not have such band.')
    @property
    def bandData(self):
        bandName = 'nir'
        if bandName in self.lst_bandNames:
            return self.imgDict[bandName]
        else:
            raise ValueError('Do not have such band.')

    @bandData.setter
    # def bandData(self, bandName, bandData):
    #     if bandName in self.lst_bandNames:
    #         self.imgDict[bandName] = bandData
    #     else:
    #         raise ValueError('Do not have such band.')
    def bandData(self, bandinfo):
        """
        To set band information of selected band of satellite image
        :param bandinfo: list. contains a string of band name and matrix of band data
        :return:
        """
        bandName = bandinfo[0]
        if bandName in self.lst_bandNames:
            self.imgDict[bandName] = bandinfo[1]
        else:
            raise ValueError('Do not have such band.')

    def displayImage(self):
        tifffile.imshow(self.data)
        plt.show()

    def displayBands(self):
        plt.figure()
        plt.subplot(2, 2, 1)
        plt.imshow(self.imgDict['red'])
        plt.subplot(2, 2, 2)
        plt.imshow(self.imgDict['nir'])
        plt.subplot(2, 2, 3)
        plt.imshow(self.imgDict['green'])
        plt.subplot(2, 2, 4)
        plt.imshow(self.imgDict['blue'])
        plt.show()

    def displayBand(self, bandName):
        if bandName in self.lst_bandNames:
            plt.figure()
            plt.imshow(self.imgDict[bandName])
            plt.show()
        else:
            raise ValueError('Do not have such band.')

    def get_band(self, bandName):
        '''
        To get the specific band.
        :param bandName: the name of the specific band. It should be in the list
        lst_bandNames = ['red', 'nir', 'green', 'blue']
        :return: matrix data of this band.
        '''
        if bandName in self.lst_bandNames:
            return self.imgDict[bandName]
        else:
            raise  ValueError('Do not have such band.')

# test
img = RSimage('../data/09AUG11PILOT.tif', 1)
img.attributes
# img.displayImage()
# img.displayBands()
# img.displayBand('nir')
# img2 = RSimage('../data/09AUG11PILOT.tif', 1)
# band2 = img2.get_band('nir')
# img.bandData = ['red', band2]
# img.displayBands()

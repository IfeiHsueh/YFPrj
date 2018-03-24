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

    __owner = 'Not Defined'
    __imageName = 'Not Defined'
    __imageDir = 'Not indicated'
    __type = 0
    __lst_bandNames = ['red', 'nir', 'green', 'blue']
    __band1 = np.empty((2000, 2000), np.uint16)
    __band2 = np.empty((2000, 2000), np.uint16)
    __band3 = np.empty((2000, 2000), np.uint16)
    __band4 = np.empty((2000, 2000), np.uint16)
    __imgDict = {__lst_bandNames[0]: __band1, __lst_bandNames[1]: __band2, __lst_bandNames[2]: __band3, __lst_bandNames[3]: __band4}

    def __init__(self, imageDir, type):
        self.__imageDir = imageDir
        self.__type = type
        self.__data = tifffile.imread(imageDir)
        self.__imgDict[self.__lst_bandNames[0]] = self.__data[0]
        self.__imgDict[self.__lst_bandNames[1]] = self.__data[1]
        self.__imgDict[self.__lst_bandNames[2]] = self.__data[2]
        self.__imgDict[self.__lst_bandNames[3]] = self.__data[3]
        self.__imgWidth = self.__imgDict[self.__lst_bandNames[0]].shape[0]
        self.__imgHeight = self.__imgDict[self.__lst_bandNames[0]].shape[1]
        self.__imgSizeXY = [self.__imgWidth, self.__imgHeight]

    def __set_name__(self, owner, name):
        self.__owner = owner
        self.__imageName = name

    #   Getter and setter for attributes
    @property
    def attributes(self):
        print(self.__imageName)
        print(self.__imageDir)

    @attributes.setter
    def attributes(self, imageName, imageDir):
        self.__imageName = imageName
        self.__imageDir = imageDir

    # Getter and setter for bandData
    @property
    def bandData(self):
        bandName = 'nir'
        # TODO(iflyhsueh@hotmail.com): Need to be modified. The formal edition should not be written like this.
        if bandName in self.__lst_bandNames:
            return self.__imgDict[bandName]
        else:
            raise ValueError('Do not have such band.')

    @bandData.setter
    def bandData(self, bandinfo):
        """
        To set band information of selected band of satellite image
        :param bandinfo: list. contains a string of band name and matrix of band data
        :return:
        """
        bandName = bandinfo[0]
        if bandName in self.__lst_bandNames:
            self.__imgDict[bandName] = bandinfo[1]
        else:
            raise ValueError('Do not have such band.')

    def displayImage(self):
        tifffile.imshow(self.__data)
        plt.show()

    def displayBands(self):
        plt.figure()
        plt.subplot(2, 2, 1)
        plt.imshow(self.__imgDict['red'])
        plt.subplot(2, 2, 2)
        plt.imshow(self.__imgDict['nir'])
        plt.subplot(2, 2, 3)
        plt.imshow(self.__imgDict['green'])
        plt.subplot(2, 2, 4)
        plt.imshow(self.__imgDict['blue'])
        plt.show()

    def displayBand(self, bandName):
        if bandName in self.__lst_bandNames:
            plt.figure()
            plt.imshow(self.__imgDict[bandName])
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
        if bandName in self.__lst_bandNames:
            return self.__imgDict[bandName]
        else:
            raise  ValueError('Do not have such band.')

    # Getter and setter for imgSize
    @property
    def imgSize(self):
        return self.__imgSizeXY

    @imgSize.setter
    def imgSize(self, imgSizeXY):
        """
        To set width and height of this image.
        :param imgSizeXY: a list contains width and height of this image.
        :return:
        """
        self.__imgSizeXY = imgSizeXY

def main():
    # test
    img = RSimage('../data/09AUG11PILOT.tif', 1)
    # img = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    #        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    #        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    #        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    img.attributes
    img.displayImage()
    img.displayBands()
    # img.displayBand('nir')
    # img2 = RSimage('../data/09AUG11PILOT.tif', 1)
    # band2 = img2.get_band('nir')
    # img.bandData = ['red', band2]
    # img.displayBands()

if __name__ == '__main__':
    main()

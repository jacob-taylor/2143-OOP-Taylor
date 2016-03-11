﻿#Jacob Taylor
#Assigment 3
#Ascii Cat
#
#Use given code to implement a flip and inverse method
#
import os
import numpy as np
import time
import urllib3, uuid
from PIL import Image
import sys


url = 'http://thecatapi.com/api/images/get'

def getCat(directory=None, filename=None, format='png'):
    basename = '%s.%s' % (filename if filename else str(uuid.uuid4()), format)
    savefile =  os.path.sep.join([directory.rstrip(os.path.sep), basename]) if directory else basename
    downloadlink = url + '?type=%s' % format
    http = urllib3.PoolManager()
    r = http.request('GET', downloadlink)
    fp = open(savefile, 'wb')
    fp.write(r.data)
    fp.close()
    return savefile

class RandomCat(object):

    def __init__(self):

        self.name = ''          # name of image
        self.path = '.'         # path on local file system
        self.format = 'png'
        self.width = 0          # width of image
        self.height = 0         # height of image
        self.img = None         # Pillow var to hold image


    """
    @Description:
    - Uses random cat to go get an amazing image from the internet
    - Names the image
    - Saves the image to some location
    @Returns:
    """
    def getImage(self):
        self.name = self.getTimeStamp()
        getCat(directory=self.path, filename=self.name, format=self.format)
        self.img = Image.open(self.name+'.'+self.format)

        self.width, self.heigth = self.img.size

    """
    Saves the image to the local file system given:
    - Names
    - Path
    """
    def saveImage(self):
        pass

    """

    """
    def nameImage(self):
        pass

    """
    Gets time stamp from local system
    """
    def getTimeStamp(self):
        seconds,milli = str(time.time()).split('.')
        return seconds


"""
The ascii character set we use to replace pixels.
The grayscale pixel values are 0-255.
0 - 25 = '#' (darkest character)
250-255 = '.' (lightest character)
"""


class AsciiImage(RandomCat):

    def __init__(self,new_width="not_set"):
        super(AsciiImage, self).__init__()

        self.newWidth = new_width
        self.newHeight = 0

        self.asciiChars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
        self.imageAsAscii = []
        self.matrix = None


    """
    Your comments here
    """
    def convertToAscii(self):

        if self.newWidth == "not_set":
            self.newWidth = self.width

        self.newHeight = int((self.heigth * self.newWidth) / self.width)

        if self.newWidth == None:
            self.newWidth = self.width
            self.newHeight = self.height

        self.newImage = self.img.resize((self.newWidth, self.newHeight))
        self.newImage = self.newImage.convert("L") # convert to grayscale
        all_pixels = list(self.newImage.getdata())

        # Put all pixels into an NxM matrix
        self.matrix = listToMatrix(all_pixels,self.newWidth)

        # Loop through matrix to convert to ascii
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = self.asciiChars[self.matrix[i][j] // 25]

    """
    Print the image to the screen
    """
    def printImage(self):
        # Using matrix to print out image
        for row in self.matrix:
            print(''.join(row))

    #Inverses the ascii characters based on light and dark
    def inverseAsciiImage(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                x = self.matrix[i][j]
                if x == '#':
	                x = '.'

                elif x == 'A':
	                x = ','

                elif x == '@':
	                x = ':'

                elif x == '%':
	                x = '*'

                elif x == 'S':
	                x = '<'

                elif x == ',':
	                x = 'A'

                elif x == '.':
	                x = '#'

                elif x == ':':
	                x = '@'

                elif x == '*':
	                x = '%'

                elif x == '<':
	                x = 'S'

                elif x == "+":
	                x = '+'

                self.matrix[i][j] = x

    #Depending on input either flips the 2D array vertically or horizontally
    #Imported numpy for easy array manipulation
    def flipImage(self,direction):
        if direction == "horizontal":
            self.matrix = np.flipud(self.matrix)
        elif direction == "vertical":
            self.matrix = np.fliplr(self.matrix)
            

def listToMatrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

if __name__=='__main__':
    awesomeCat = AsciiImage(50)
    awesomeCat.getImage()
    awesomeCat.convertToAscii()
    print 'Original Ascii'
    print '----------------------------------------------------'
    awesomeCat.printImage()
    print '----------------------------------------------------\n'
    print '\nVertically Flipped Image'
    print '----------------------------------------------------'
    awesomeCat.flipImage("vertical")
    awesomeCat.printImage()
    print '----------------------------------------------------\n'
    print '\nHorizontally Flipped Image'
    print '----------------------------------------------------'
    awesomeCat.flipImage("horizontal")
    awesomeCat.printImage()
    print '----------------------------------------------------\n'
    print '\nInversed Image after Vertical then Horizontal Flip'
    print '----------------------------------------------------'
    awesomeCat.inverseAsciiImage()
    awesomeCat.printImage()
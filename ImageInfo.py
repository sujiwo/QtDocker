'''
Created on 1 Mar 2023

@author: sujiwo
'''

from Widgets import *


class ImageInfo(WindowFromUiFile):

    def __init__(self, parentApp):
        self.parent = parentApp
        WindowFromUiFile.__init__(self, 'imageInfo.ui', parentApp.window)
        self.window.setWindowTitle('Image Info for {}'.format(self.parent.currentImage.tags[0]))
        imageInfo = self.parent.currentImage.attrs
        displayDictToTree(imageInfo, self.imageInfo)
        self.window.exec_()
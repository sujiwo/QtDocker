'''
Created on 1 Mar 2023

@author: sujiwo
'''

from .Widgets import *


class ImageInfo(WindowFromUiFile):

    def __init__(self, parentApp):
        self.wparent = parentApp
        WindowFromUiFile.__init__(self, 'imageInfo.ui', parentApp.window)
        self.window.setWindowTitle('Image Info for {}'.format(self.wparent.currentImage.tags[0]))
        imageInfo = self.wparent.currentImage.attrs
        displayDictToTree(imageInfo, self.imageInfo)
        for c in self.getRelatedContainers():
            self.relContainerList.addItem(c['Name'])
        self.window.exec_()
        
    def getRelatedContainers(self):
        relContainers = []
        for c in self.wparent.containerList:
            print('{} -> {}'.format(c['Image'], self.wparent.currentImage.tags[0]))
            if c['Image']==self.wparent.currentImage.tags[0]:
                relContainers.append(c)
        return relContainers
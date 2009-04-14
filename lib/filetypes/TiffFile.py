# -*- coding: utf-8 -*-

import Image

class TiffFile:
    def __init__(self, data):
        self.data = data
        
    def typeName(self):
        return 'TiffFile'
        
    def write(self, fileName):
        img = Image.fromarray(self.data.transpose())
        img.save(fileName)
        
    def fromFile(fileName, info=None):
        img = Image.open(fileName)
        return array(img).transpose()

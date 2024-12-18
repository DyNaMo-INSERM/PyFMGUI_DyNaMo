#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 17:59:13 2024

@author: evillz
"""

# from AFS_RICM__Analysis.source_code.stack_processing.functions.io import load
# from AFS_RICM__Analysis.source_code.stack_processing.functions.view.QViewImage import QViewImage
# from AFS_RICM__Analysis.source_code.stack_processing.functions.view.QViewStack import QViewStack
from PyQt5.QtWidgets import QWidget
from os.path import basename, dirname, isdir, isfile, splitext
from h5py import File
from functools import partial
from batchPrcoess_tdms import *



class QDragViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDragViewer')
        self.resize(200,200)
        self.setAcceptDrops(True)
        self.viewers = dict()
    
    def dragEnterEvent(self, event):
        # print('enter drag')
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        for url in urls:
            path = url.path()
            # print(url.path())
            if isdir(path):
                print('directory:',basename(path))
            
            elif isfile(path):
                filename,extension = splitext(basename(path))
                if extension =='.tdms':
                    print('tdms file:',filename)
                else:
                    print('file ',extension,':',filename)
                
    
    
    
from PyQt5.QtWidgets import QApplication
import sys



    
app = QApplication(sys.argv)
view_stack = QDragViewer()
view_stack.show()
sys.exit(app.exec())        
        
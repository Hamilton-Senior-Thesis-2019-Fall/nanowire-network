from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from mockup import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.activateButtons()
        self.show()

        # matplotlib canvas
        self.nav = NavigationToolbar(self.MplWidget.canvas, self)
        self.nav.setStyleSheet("QToolBar { border: 2px;\
        background:white; }")
        self.addToolBar(self.nav)

    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp *.tif)")
        if fileName:
            image = mpimg.imread(fileName)
            imgplot = self.MplWidget.canvas.axes.imshow(image)
            self.MplWidget.canvas.draw()


    def activateButtons(self):
        self.actionUpload_from_computer.triggered.connect(self.setImage)
        self.pushButton_standard_node.clicked.connect(self.addNode)

    def addNode(self):
        print('adding node')

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui_logic = Logic()
    sys.exit(app.exec_())

main()

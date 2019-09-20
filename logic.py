from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from mockup import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random
import math
from skimage import io
from skimage import feature
from skimage import draw
from skimage import util
from skimage import color
from skimage import morphology
from skimage import filters
from skimage import measure
from skimage import transform
from skimage import exposure
from sklearn.neighbors import NearestNeighbors

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.activateButtons()
        self.show()

        self.filename = ''

        self.cid = []

        self.nodes = []
        self.edges = []

        self.edgeStart = -1
        self.edgeEnd = -1

        # matplotlib canvas
        self.nav = NavigationToolbar(self.MplWidget.canvas, self)
        self.nav.setStyleSheet("QToolBar { border: 2px;\
        background:white; }")
        self.addToolBar(self.nav)

    def activateButtons(self):
        self.actionUpload_from_computer.triggered.connect(self.setImage)
        self.actionExport_to_Gephi.triggered.connect(self.convertToCSV)
        self.pushButton_standard_node.clicked.connect(self.addNode)
        self.pushButton_standard_edge.clicked.connect(self.addEdge)

    def distance(self, position1, position2):
        """finds the distance between two points"""
        return math.sqrt((position1[0] - position2[0]) ** 2 +
                         (position1[1] - position2[1]) ** 2)

    def plotNodes(self, img):
        updated_img = np.copy(img)
        for i in range(len(self.nodes)):
            rr, cc = draw.circle(self.nodes[i][1], self.nodes[i][0],12)
            updated_img[rr, cc] = [0, 0, 255]
        return updated_img

    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp *.tif)")
        if fileName:
            self.filename = fileName
            image = plt.imread(self.filename)
            gray_arr = np.asarray(image)
            rgb_arr = np.stack((gray_arr, gray_arr, gray_arr), axis=-1)
            imgplot = self.MplWidget.canvas.axes.imshow(rgb_arr)
            self.MplWidget.canvas.draw()

    def convertToCSV(self):
        if self.filename == '':
            f = open('output.csv', 'w+')
        else:
            f = open(self.filename + '_gephi.csv', 'w+')
        # matrix = [[2345,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3]]

        line = ''
        if (not len(self.edges)):
            f.close()
            return
        for i, val in enumerate(self.edges[0]):
            line += ';' + getNodeLetter(i)
        f.write(line + '\n')
        for i, row in enumerate(self.edges):
            line = getNodeLetter(i)
            for val in row:
                line += ';' + str(val)
            f.write(line + '\n')
        f.close()

    def replotImage(self):
        image = plt.imread(self.filename)
        gray_arr = np.asarray(image)
        rgb_arr = np.stack((gray_arr, gray_arr, gray_arr), axis=-1)
        marked_arr = self.plotNodes(rgb_arr)
        imgplot = self.MplWidget.canvas.axes.imshow(marked_arr)
        self.MplWidget.canvas.draw()

        for i in range(len(self.cid)):
            self.MplWidget.canvas.mpl_disconnect(self.cid[i])



    def addPoint(self, event):
        #Add more rows/col to edges adj matrix
        if len(self.nodes) == 0:
            self.edges = [[1]]
        else:
            self.edges = np.pad(self.edges, ((0,1),(0,1)), 'constant')
            self.edges[-1][-1] = 1

        self.nodes.append([event.xdata, event.ydata])
        self.replotImage()

    def lineStart(self, event):
        pt = [event.xdata, event.ydata]
        min_dist = self.distance(pt, self.nodes[0])
        min_ind = 0
        for i in range(len(self.nodes)):
            if self.distance(pt, self.nodes[i]) < min_dist:
                min_dist = self.distance(pt, self.nodes[i])
                min_ind = i

        self.edgeStart = min_ind

        print('line start')


    def lineEnd(self, event):
        pt = [event.xdata, event.ydata]

        if self.edgeStart != 0:
            min_dist = self.distance(pt, self.nodes[0])
            min_ind = 0
        else:
            min_dist = self.distance(pt, self.nodes[1])
            min_ind = 0
        for i in range(len(self.nodes)):
            if self.distance(pt, self.nodes[i]) < min_dist and i != self.edgeStart:
                min_dist = self.distance(pt, self.nodes[i])
                min_ind = i

        self.edgeEnd = min_ind

        self.edges[self.edgeStart,self.edgeEnd] = 1
        print('line end')
        print(self.edgeStart)
        print(self.edgeEnd)
        print(self.edges)

    def addNode(self):
        if self.filename != '':
            self.cid.append(self.MplWidget.canvas.mpl_connect('button_press_event', self.addPoint))

    def addEdge(self):
        if self.filename != '' and len(self.nodes) >= 2:
            self.cid.append(self.MplWidget.canvas.mpl_connect('button_press_event', self.lineStart))
            self.cid.append(self.MplWidget.canvas.mpl_connect('button_release_event', self.lineEnd))


def getNodeLetter(num):
    nodeLetter = ""
    num += 1
    while num > 0:
        num, remainder = divmod(num - 1, 26)
        nodeLetter = chr(65 + remainder) + nodeLetter
    return nodeLetter

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui_logic = Logic()
    sys.exit(app.exec_())

main()

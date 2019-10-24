from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from mockup import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random
import math
import datetime as dt
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
import matplotlib.lines as lines
import os

from automation import findNodes


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        self.cid = []

        QMainWindow.__init__(self, *args, **kwargs)

        self.setupUi(self)
        self.activateButtons()
        self.show()

        self.filename = ''

        self.button = "node"

        self.nodes = []
        self.edges = []
        self.edgeCenters = []
        self.edgeNodes = []

        self.edgeStarted = False;
        self.edgeStart = -1
        self.edgeEnd = -1

        self.press = False
        self.move = False

        # matplotlib canvas
        self.nav = NavigationToolbar(self.MplWidget.canvas, self)
        self.nav.setStyleSheet("QToolBar { border: 2px;\
        background:white; }")
        self.addToolBar(self.nav)
        self.MplWidget.canvas.setFocusPolicy( QtCore.Qt.ClickFocus )
        self.MplWidget.canvas.setFocus()

    def resetPlot(self):
        self.nodes = []
        self.edges = []
        self.edgeCenters = []
        self.edgeNodes = []

        self.edgeStarted = False;
        self.edgeStart = -1
        self.edgeEnd = -1

        self.press = False
        self.move = False

    def activateButtons(self):
        self.actionUpload_from_computer.triggered.connect(self.setImage)
        self.actionExport_to_Gephi.triggered.connect(self.convertToCSV)
        self.actionSave_file.triggered.connect(self.save_plot)
        self.actionUpload_from_saved_projects.triggered.connect(self.open_plot)
        self.pushButton_standard_node.clicked.connect(self.addNode)
        self.pushButton_standard_edge.clicked.connect(self.addEdge)

        self.cid.append(self.MplWidget.canvas.mpl_connect('button_press_event', self.onpress))
        self.cid.append(self.MplWidget.canvas.mpl_connect('motion_notify_event', self.onmove))
        self.cid.append(self.MplWidget.canvas.mpl_connect('button_release_event', self.onrelease))

        # self.cid.append(self.MplWidget.canvas.mpl_connect('button_press_event', self.onClick))
        self.cid.append(self.MplWidget.canvas.mpl_connect('key_press_event', self.onKey))
        self.cid.append(self.MplWidget.canvas.mpl_connect('key_release_event', self.onKeyRelease))

    def onClick(self, event):
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if self.filename != '':
            #If control is held down, removing stuff
            if modifiers == QtCore.Qt.ControlModifier:
                self.edgeStarted = False;
                self.removeNearest(event.xdata, event.ydata)
            else:
                if self.button == "node":
                    if modifiers == QtCore.Qt.ShiftModifier:
                        if self.edgeStarted:
                            self.lineEnd(event.xdata, event.ydata)
                            self.edgeStarted = False;
                        else:
                            self.lineStart(event.xdata, event.ydata)
                            self.edgeStarted = True;
                    else:
                        self.edgeStarted = False;
                        self.addPoint(event.xdata, event.ydata)
                elif self.button == "edge":
                    if modifiers == QtCore.Qt.ShiftModifier:
                        self.edgeStarted = False;
                        self.addPoint(event.xdata, event.ydata)
                    else:
                        if self.edgeStarted:
                            self.lineEnd(event.xdata, event.ydata)
                            self.edgeStarted = False;
                        else:
                            self.lineStart(event.xdata, event.ydata)
                            self.edgeStarted = True;
        #self.cid.append(self.MplWidget.canvas.mpl_connect('button_press_event', self.onClick))

    def addAutoNodes(self, list):
        for yslice,xslice in list:
            if ((yslice.stop - yslice.start) > 30) and ((xslice.stop - xslice.start) > 30):
                x = (xslice.start + xslice.stop - 1)/2
                y = (yslice.start + yslice.stop - 1)/2
                self.addPoint(x, y)

            # print('x: ', x, '  y: ', y, '\n')

    def onKey(self, event):
        if event.key == 'control':
            self.replotImage()
            x_coords = [i[0] for i in self.edgeCenters]
            y_coords = [i[1] for i in self.edgeCenters]
            self.MplWidget.canvas.axes.scatter(x_coords, y_coords, 12, 'red', zorder=3)
            self.MplWidget.canvas.draw()


    def onKeyRelease(self, event):
        self.replotImage()

    def distance(self, position1, position2):
        """finds the distance between two points"""
        return math.sqrt((position1[0] - position2[0]) ** 2 +
                         (position1[1] - position2[1]) ** 2)

    def midpoint(self, position1, position2):
        return [(position1[0] + position2[0]) / 2, (position1[1] + position2[1]) / 2]

    def findClosestNode(self, x_coord, y_coord):
        pt = [x_coord, y_coord]
        if self.edgeStarted and self.edgeStart == 0:
            min_dist = self.distance(pt, self.nodes[1])
            min_ind = 1
        else:
            min_dist = self.distance(pt, self.nodes[0])
            min_ind = 0
        for i in range(len(self.nodes)):
            if self.distance(pt, self.nodes[i]) < min_dist:
                min_dist = self.distance(pt, self.nodes[i])
                min_ind = i

        return min_ind, min_dist

    def findClosestEdge(self, x_coord, y_coord):
        pt = [x_coord, y_coord]
        if not self.edgeCenters:
            return -1, 0
        min_dist = self.distance(pt, self.edgeCenters[0])
        min_ind = 0
        for i in range(len(self.edgeCenters)):
            if self.distance(pt, self.edgeCenters[i]) < min_dist:
                min_dist = self.distance(pt, self.edgeCenters[i])
                min_ind = i

        return min_ind, min_dist

    def plotNodes(self):
        x_coords = [i[0] for i in self.nodes]
        y_coords = [i[1] for i in self.nodes]
        self.MplWidget.canvas.axes.scatter(x_coords, y_coords, 15, 'blue', zorder=3)

    def plotLines(self):
        self.edgeCenters = []
        self.edgeNodes = []
        for r in range(len(self.edges)):
            for c in range(len(self.edges)):
                if r != c and self.edges[r][c] > 0:
                    self.edgeCenters.append(self.midpoint(self.nodes[r], self.nodes[c]))
                    self.edgeNodes.append([r,c])
                    line_x = [self.nodes[r][0], self.nodes[c][0]]
                    line_y = [self.nodes[r][1], self.nodes[c][1]]
                    self.MplWidget.canvas.axes.add_line(lines.Line2D(line_x, line_y, linewidth=2, color='red'))

    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp *.tif)")
        if fileName:
            self.filename = fileName
            self.resetPlot()
            self.replotImage()
            image = plt.imread(self.filename)
            imgplot = self.MplWidget.canvas.axes.imshow(image, cmap = plt.cm.gist_gray)
            self.MplWidget.canvas.draw()
            self.addAutoNodes(findNodes(self.filename))


    def convertToCSV(self):
        if self.filename == '':
            f = open('output.csv', 'w+')
        else:
            f = open(os.path.splitext(self.filename)[0] + '_gephi.csv', 'w+')
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
        #Clearing the figure and getting rid of the axes labels
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.axis('off')
        #Plotting the image in greyscale
        image = plt.imread(self.filename)
        imgplot = self.MplWidget.canvas.axes.imshow(image, cmap = plt.cm.gist_gray)
        #Plotting lines and nodes
        self.plotLines()
        self.plotNodes()

        self.MplWidget.canvas.draw()

        #Disconnecting event handlers (not quite sure about this)
        #for i in range(len(self.cid)):
        #    self.MplWidget.canvas.mpl_disconnect(self.cid[i])



    def addPoint(self, x_coord, y_coord):
        #Add more rows/col to edges adj matrix
        if len(self.nodes) == 0:
            self.edges = [[1]]
        else:
            self.edges = np.pad(self.edges, ((0,1),(0,1)), 'constant')
            self.edges[-1][-1] = 1

        self.nodes.append([x_coord, y_coord])
        self.replotImage()

    def removePoint(self, x_coord, y_coord):
        del_ind, del_dist = self.findClosestNode(x_coord, y_coord)
        del self.nodes[del_ind]
        self.edges = np.delete(self.edges, del_ind, axis=0)
        self.edges = np.delete(self.edges, del_ind, axis=1)

        self.replotImage()

    def lineStart(self, x_coord, y_coord):
        min_ind, min_dist = self.findClosestNode(x_coord, y_coord)
        self.edgeStart = min_ind

    def lineEnd(self, x_coord, y_coord):
        min_ind, min_dist = self.findClosestNode(x_coord, y_coord)
        self.edgeEnd = min_ind

        self.edges[self.edgeStart,self.edgeEnd] = 1
        self.replotImage()

    def removeLine(self, x_coord, y_coord):
        del_ind, dist = self.findClosestEdge(x_coord, y_coord)

        del self.edgeCenters[del_ind]
        self.edges[self.edgeNodes[del_ind][0]][self.edgeNodes[del_ind][1]] = 0
        self.edges[self.edgeNodes[del_ind][1]][self.edgeNodes[del_ind][0]] = 0
        del self.edgeNodes[del_ind]

        self.replotImage()

    def removeNearest(self, x_coord, y_coord):
        ind1, node_dist = self.findClosestNode(x_coord, y_coord)
        ind2, edge_dist = self.findClosestEdge(x_coord, y_coord)
        if (node_dist < edge_dist) or (ind2 == -1):
            self.removePoint(x_coord, y_coord)
        else:
            self.removeLine(x_coord, y_coord)

    def onpress(self, event):
        self.press = True

    def onmove(self, event):
        if self.press:
            self.move = True

    def onrelease(self, event):
        if self.press and not self.move:
            self.onClick(event)
        self.press = False
        self.move = False

    def addNode(self):
        self.button = 'node'
    #     if self.filename != '':
    #       self.cid.append(self.MplWidget.canvas.mpl_connect('button_press_event', self.addPoint))

    def addEdge(self):
        self.button = 'edge'
        # if self.filename != '' and len(self.nodes) >= 2:
        #     self.cid.append(self.MplWidget.canvas.mpl_connect('button_press_event', self.lineStart))
        #     self.cid.append(self.MplWidget.canvas.mpl_connect('button_press_event', self.lineEnd))

    def save_plot(self):
        curr_time = str(dt.datetime.now())
        # QInputDialog.getText("Save Project", "Project name:", QLineEdit.Normal, "")
        # if okPressed:
        save_file_name = ("%s_" % self.filename) if self.filename != '' else "SaveFile"
        for c in curr_time:
            if not c in ['-', ' ', ':', '.']:
                save_file_name += c
            else:
                save_file_name += '_'
        out_file = open(save_file_name + ".nwas", "w+")

        # Write node coords
        for x, y in self.nodes[:-1]:
            out_file.write("%f,%f,%s," % (x, y, "STD_NODE"))
        out_file.write("%f,%f,%s\n" % (self.nodes[-1][0], self.nodes[-1][1], "STD_NODE"))

        # Write adjacency matrix
        out_file.write("%d\n" % len(self.edges))
        for i in range(len(self.edges)):
            for j in range(len(self.edges[i])):
                out_file.write("%f " % self.edges[i][j])
            out_file.write('\n')

        # Write image binary
        out_file.write("%s\n" % self.filename)
        out_file.close()
        out_file = open(save_file_name + ".nwas", "ab")
        with open(self.filename, "rb") as img_file:
            data = img_file.read()
            out_file.write(data)
        out_file.close()

    def open_plot(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Save File", "", "NWAS Files (*.nwas)")
        if fileName:
            # We will read this many lines again after reopening the file so that we can read the image file
            lines_read = 0
            with open(fileName, 'r') as saved_file:

                # Read the node coords and add them to self.nodes
                nodes = saved_file.readline().strip().split(',')
                lines_read += 1
                for i in range(0, len(nodes), 3):
                    self.nodes.append([float(nodes[i]), float(nodes[i + 1])])

                # Read in the number of nodes
                num_nodes = int(saved_file.readline().strip())
                lines_read += 1

                for i in range(num_nodes):
                    line = saved_file.readline().strip().split()
                    lines_read += 1

                    self.edges.append([float(x) for x in line])

                img_file_name = saved_file.readline().strip()
                lines_read += 1
                self.filename = img_file_name

            with open(fileName, "rb") as saved_file:
                # For now we'll just try to use the file name
                # for _ in range(lines_read):
                #     x = saved_file.readline()
                #     print(x)
                # img_binary = saved_file.read()
                # temp = open("__temp.tif", "wb+")
                # temp.write(img_binary)
                # temp.close()
                # image = plt.imread("$$temp$$")
                try:
                    image = plt.imread(self.filename)
                except (FileNotFoundError):
                    msg = QMessageBox.critical(self, "Error loading image: File not found",
                                            "Make sure file '%s' is in current directory" % self.filename)
                    return
                gray_arr = np.asarray(image)
                #print(gray_arr)
                rgb_arr = np.stack((gray_arr, gray_arr, gray_arr), axis=-1)
                #print(rgb_arr)
                imgplot = self.MplWidget.canvas.axes.imshow(rgb_arr)
                self.MplWidget.canvas.draw()
                self.replotImage()

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

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QInputDialog
from mockup import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random
import math
import platform
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
import matplotlib.lines as lines
import os
from matplotlib.patches import Rectangle

from automation import findNodes


class Logic(QMainWindow, Ui_MainWindow):
    """ This is the class that manages the interface """

    def __init__(self, *args, **kwargs):
        self.resetPlot()
        # Note: Initiation sequence is important, attributes need to go first
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.activateButtons()
        self.show()

        # Matplotlib canvas
        self.nav = NavigationToolbar(self.MplWidget.canvas, self)
        self.nav.setStyleSheet("QToolBar { border: 2px;\
        background:white; }")
        self.addToolBar(self.nav)
        self.MplWidget.canvas.setFocusPolicy( QtCore.Qt.ClickFocus )
        self.MplWidget.canvas.setFocus()

        self.resetCounterDisplay()

    def resetPlot(self):
        self.cid = []

        self.filename = ''
        self.save_loc = ''

        self.button = ""
        # track different button type, register with click event
        self.buttonType = "standard"

        # Distinguish different types of nodes
        self.nodeTypes = ['standard','spheroplast', 'curved', 'filament']
        self.edgeTypes = ['celltocell', 'celltosurface', 'cellcontact']
        self.nodeColor = {'standard':'blue', 'spheroplast':'yellow', 'curved':'lightgreen', 'filament':'violet'}
        self.nodeWithTypes = dict()
        # {nodeType: [list of [x,y]}
        self.edgeWithTypes = dict()
        # {edgeType: {(startNodex, startNodey): [list of [x,y]]}}
        self.nodeWithTypes.update((n,[]) for n in self.nodeTypes)
        self.edgeWithTypes.update((e,dict()) for e in self.edgeTypes)

        # microns per pixel (this is a rough estimate based on a 10 micron calibration on a 1080p screen.)
        self.pxdist = 0.018619356332001857

        # Record all nodes and edges regardless of their type
        self.nodes = []
        self.edges = []
        self.edgeCenters = []
        self.edgeNodes = []
        self.calibration_point_coords = []
        self.calibration_points = []

        self.edgeStarted = False;
        self.edgeStart = -1
        self.edgeEnd = -1
        self.edgeStartNode = [];

        self.press = False
        self.move = False
        self.saved = True
        self.calibrating = False

        self.shouldAutomate = True
        self.shouldPlotIssues = True
        self.issues = []


        # the pixel width of the node dot on the graph
        # It's important to avoid re-registering the same dot if clicked on nearby pixels
        self.nodeRdius = 12

        # Track cell to surface edges, because they don't require two nodes,
        # instead, they take one starting node a [x,y] finishing coordinates,
        # which shouldn't be counted into total nodes.
        # Those connections are handled differently when writing to the adjacency matrix.
        # {(startingNodex,startingNodey):[list of ending [x,y] coordinates]}

    def activateButtons(self):

        # These are the actions in the toolbar across the top of the window
        self.actionUpload_from_computer.triggered.connect(self.setImage)
        self.actionExport_to_CSV.triggered.connect(self.convertToCSV)
        self.actionExport_to_GEXF.triggered.connect(self.convertToGEXF)
        self.actionSave_file.triggered.connect(self.save_plot)
        self.actionUpload_from_saved_projects.triggered.connect(self.open_plot)
        self.actionColor_select.triggered.connect(self.automateFile)
        self.actionCalibrate_Distance.triggered.connect(self.calibrate_measure)

        # These are the actions for the nodes on the vertical toolbar
        self.clear_painter.clicked.connect(lambda:self.addNode('clear'))
        self.node_painter_standard.clicked.connect(lambda:self.addNode('standard'))
        self.node_painter_spheroplast.clicked.connect(lambda:self.addNode('spheroplast'))
        self.node_painter_curved.clicked.connect(lambda:self.addNode('curved'))
        self.node_painter_filament.clicked.connect(lambda:self.addNode('filament'))

        # These are the actions for the edgess on the vertical toolbar
        self.edge_painter_celltocell.clicked.connect(lambda:self.addEdge('celltocell'))
        self.edge_painter_celltosurface.clicked.connect(lambda:self.addEdge('celltosurface'))
        self.edge_painter_cellcontact.clicked.connect(lambda:self.addEdge('cellcontact'))

        self.updateToolTipDisplay("clear")

        self.cid.append(self.MplWidget.canvas.mpl_connect('button_press_event', self.onpress))
        self.cid.append(self.MplWidget.canvas.mpl_connect('motion_notify_event', self.onmove))
        self.cid.append(self.MplWidget.canvas.mpl_connect('button_release_event', self.onrelease))

        # self.cid.append(self.MplWidget.canvas.mpl_connect('button_press_event', self.onClick))
        self.cid.append(self.MplWidget.canvas.mpl_connect('key_press_event', self.onKey))
        self.cid.append(self.MplWidget.canvas.mpl_connect('key_release_event', self.onKeyRelease))

    def onClick(self, event):
        # print(self.nodes)
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if self.filename != '':

            # In calibration mode, no other clicks should work. self.calibrating flag activated by self.calibrate_measure
            if self.calibrating:
                # Saving points to diplay on the screen to see ends of the calibration range
                self.calibration_point_coords.append((event.xdata, event.ydata))
                print(self.calibration_point_coords)
                self.calibration_points.append(plt.scatter(event.x, event.y, 10, "magenta"))
                self.MplWidget.canvas.axes.scatter(event.xdata, event.ydata, 20, "magenta", zorder=3)
                self.MplWidget.canvas.draw()

                # When second calibration point selected re-call self.calibrate_measure to complete calibration process.
                if len(self.calibration_points) == 2:
                    line_x = [self.calibration_point_coords[0][0],self.calibration_point_coords[1][0]]
                    line_y = [self.calibration_point_coords[0][1],self.calibration_point_coords[1][1]]
                    self.MplWidget.canvas.axes.add_line(lines.Line2D(line_x,line_y, linewidth=2, color='white'))
                    self.MplWidget.canvas.draw()
                    self.calibrate_measure()
                    self.calibrating = False
            else:
            #If control is held down, removing stuff
              if modifiers == QtCore.Qt.ControlModifier:
                  self.edgeStarted = False;
                  self.removeNearest(event.xdata, event.ydata);

              else:
                  if self.button == "node":
                      # if modifiers == QtCore.Qt.ShiftModifier:
                      #     if self.edgeStarted:
                      #         self.(event.xdata, event.ydata)
                      #         self.edgeStarted = False;
                      #     else:
                      #         self.lineStart(event.xdata, event.ydata)
                      #         self.edgeStarted = True;
                      # else:
                          self.edgeStarted = False;
                          self.addPoint(event.xdata, event.ydata)
                  elif self.button == "edge":
                        if not self.nodes:
                            return
                        # if modifiers == QtCore.Qt.ShiftModifier:
                        #     self.edgeStarted = False;
                        #     self.addPoint(event.xdata, event.ydata)
                        # else:
                        if self.edgeStarted:
                            startNodeTuple = tuple(self.nodes[self.edgeStart])
                            if startNodeTuple not in self.edgeWithTypes[self.buttonType]:
                                self.edgeWithTypes[self.buttonType][startNodeTuple] = []
                            min_ind, min_dist = self.findClosestNode(event.xdata, event.ydata)
                            if startNodeTuple != tuple(self.nodes[min_ind]):
                                self.edgeWithTypes[self.buttonType][startNodeTuple].append(self.nodes[min_ind])

                        if self.buttonType == "celltocell" or self.buttonType == "cellcontact":
                            if self.edgeStarted:
                                self.lineEnd(event.xdata, event.ydata)
                                self.edgeStarted = False;
                            else:
                                self.lineStart(event.xdata, event.ydata)
                                self.edgeStarted = True;
                        elif self.buttonType == 'celltosurface':
                            if self.edgeStarted:
                                self.edgeStarted = False;
                                self.edgeWithTypes[self.buttonType][startNodeTuple].append([event.xdata, event.ydata])
                                self.replotImage()
                            else:
                                self.lineStart(event.xdata, event.ydata)
                                self.edgeStarted = True;
                  elif self.button == '':
                    if not self.nodes:
                        return
                    # Dan: clear_arrow allows type change for nodes
                    self.nodeTypeChange(event.xdata, event.ydata)
          #self.cid.append(self.MplWidget.canvas.mpl_connect('button_press_event', self.onClick))

    def removeNodesEdges(self):
        self.nodeWithTypes = dict()
        self.edgeWithTypes = dict()
        self.nodeWithTypes.update((n,[]) for n in self.nodeTypes)
        self.edgeWithTypes.update((e,dict()) for e in self.edgeTypes)
        self.nodes = []
        self.edges = []
        self.edgeCenters = []
        self.edgeNodes = []
        self.calibration_point_coords = []
        self.calibration_points = []
        self.edgeStarted = False;
        self.edgeStart = -1
        self.edgeEnd = -1
        self.edgeStartNode = [];
        self.press = False
        self.move = False
        self.saved = True
        self.calibrating = False
        self.shouldAutomate = False
        self.shouldPlotIssues = True
        self.issues = []
        self.nodeRdius = 12
        self.replotImage()

    def automateFile(self):
        modifiers = QtWidgets.QApplication.keyboardModifiers()

        # If control held down, this button toggles problem boxes otherwise runs automation
        if modifiers == QtCore.Qt.ControlModifier:
            self.shouldPlotIssues = not self.shouldPlotIssues
            self.replotImage()
        else:

            # Automation can only run once on any given image
            if (self.shouldAutomate):
                self.status_label.setText("Status: Automating...")
                msg = QMessageBox.warning(self, "Confirm Automation",
                                            "This process is going to take a while. Do you want to continue? ", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if msg == QMessageBox.No:
                    self.status_label.setText("")
                    return
                self.addAutoNodes(findNodes(self.filename))
                self.shouldAutomate = False
                self.status_label.setText("Status: Automated")
            else:
                msg = QMessageBox.warning(self, "Already automated",
                                            "Automation has already run on this image. Exiting automation process.")
                self.status_label.setText("Status: Automated")
                print("Already Automated")

    def addAutoNodes(self, values):
        list = values[0]
        av_size = values[1]
        for yslice,xslice in list:
            # if ((yslice.stop - yslice.start) * (xslice.stop - xslice.start) > av_size):
            if ((yslice.stop - yslice.start) > 100) and ((xslice.stop - xslice.start) > 100) or \
            ((yslice.stop - yslice.start) > 250) or ((xslice.stop - xslice.start) > 250):
                xlength = xslice.stop - xslice.start
                ylength = yslice.stop - yslice.start
                self.issues.append([xslice.start,yslice.start,xlength, ylength])
            elif ((yslice.stop - yslice.start) > 30) and ((xslice.stop - xslice.start) > 30):
                x = (xslice.start + xslice.stop - 1)/2
                y = (yslice.start + yslice.stop - 1)/2
                self.buttonType = "standard"
                # self.updateToolTipDisplay(buttonType)
                self.addPoint(x, y)
            # print('x: ', x, '  y: ', y, '\n')

    def onKey(self, event):
        ''' Pressing the control key provides the option to delete objects'''
        if event.key == 'control':
            self.replotImage()

            # Draw a red dot in the middle of edges. To delete click these
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
        """ Finds the midpoint between two points """
        return [(position1[0] + position2[0]) / 2, (position1[1] + position2[1]) / 2]

    def nodeTypeChange(self, x_coord, y_coord):
        """ This function allows you to change the type of a node """
        node_ind, node_dist = self.findClosestNode(x_coord, y_coord)
        currNode = self.nodes[node_ind]
        nodeType = ''

        # Find selected node and remove it from its current list
        for type in self.nodeWithTypes:
            if currNode in self.nodeWithTypes[type]:
                nodeType = type
                self.nodeWithTypes[type].remove(currNode)
                break

        # If node found add it to the next type's list
        if nodeType != '':
            nextTypeInd = (self.nodeTypes.index(nodeType) + 1) % len(self.nodeTypes)
            self.nodeWithTypes[self.nodeTypes[nextTypeInd]].append(currNode)
            self.replotImage()

        else:
            raise Exception("node {} not found in self.nodeWithTypes when attempting node type change").format(currNode)



    def findClosestNode(self, x_coord, y_coord):
        """ Find the closest node to a selected point """
        pt = [x_coord, y_coord]
        if self.edgeStarted and self.edgeStart == 0:
            min_dist = self.distance(pt, self.nodes[1])
            min_ind = 1
        else:
            if not self.nodes:
                return -1, -1
            min_dist = self.distance(pt, self.nodes[0])
            min_ind = 0
        for i in range(len(self.nodes)):
            if self.distance(pt, self.nodes[i]) < min_dist:
                min_dist = self.distance(pt, self.nodes[i])
                min_ind = i

        return min_ind, min_dist

    def findClosestEdge(self, x_coord, y_coord):
        """ Find the closest edge to a selected point """
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
        """ Plot nodes on the canvas """
        for type in self.nodeWithTypes:
            for n in self.nodeWithTypes[type]:
                x_coords,y_coords = n
                self.MplWidget.canvas.axes.scatter(x_coords, y_coords, 20, self.nodeColor[type], zorder=3)
        self.updateCounterDisplay()

    def plotLines(self):
        """ Plot edges on the canvas """
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

        celltosurface = self.edgeWithTypes['celltosurface']
        for s in list(celltosurface):
            for e in self.edgeWithTypes['celltosurface'][s]:
                line_x = [s[0],e[0]]
                line_y = [s[1],e[1]]
                self.edgeCenters.append(e)
                self.MplWidget.canvas.axes.add_line(lines.Line2D(line_x, line_y, linewidth=2, color='orange'))

    def setImage(self):
        """ Sets background of the Matplotlib canvas to a selected image """
        if not self.saved:
            msg = QMessageBox.warning(self, "File not saved",
                                        "You are about to leave the current project. Do you want to continue without saving?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if msg == QMessageBox.No:
                return
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp *.tif)")
        if fileName:
            self.shouldAutomate = True
            self.resetPlot()
            self.resetCounterDisplay();

            self.filename = fileName
            self.replotImage()
            image = plt.imread(self.filename)
            imgplot = self.MplWidget.canvas.axes.imshow(image, cmap = plt.cm.gist_gray)
            self.MplWidget.canvas.draw()
            #self.calibrate_measure()

    def convertToCSV(self):
        """ Outputs the adjacency matrix of file to a .csv file """
        if self.filename == '':
            f = open('output.csv', 'w+')
        else:
            try:
                f = open(os.path.splitext(self.filename)[0] + '_gephi.csv', 'w+')
            except (PermissionError):
                msg = QMessageBox.critical(self, "Error loading file",
                                            "Unable to open this file. Make sure it is not in use by another program")
                return
        # matrix = [[2345,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3]]

        line = ''
        if (not len(self.edges)):
            f.close()
            return
        for i, val in enumerate(self.edges[0]):
            # assign label to each node
            line += ',' + getNodeLetter(i)

        # take the cell to surface edge into account
        # Give a ghost node which handles all of such edges from different cells
        line += "," + "SURFACE_NODE"

        f.write(line + '\n')
        for i, row in enumerate(self.edges):
            line = getNodeLetter(i)
            for val in row:
                line += ',' + str(val)

            # cell to surface edge
            currCoord = tuple(self.nodes[i])
            if currCoord in self.edgeWithTypes['celltosurface'] and len(self.edgeWithTypes['celltosurface'][currCoord]) > 0:
                line += "," + "1"
            else:
                line += "," + "0"
            f.write(line + '\n')
        f.close()

    def convertToGEXF(self):
        """ Outputs graph as a .gexf file """
        date = dt.datetime.now()
        save_file_name, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","", "GEXF Files (*.gexf)")
        save_file_name += (".gexf" if save_file_name[-5:] != ".gexf" else "")
        if not save_file_name:
            return


        with open(save_file_name, "w+") as out_file:
            # output boilerplate XML
            out_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            out_file.write('<gexf xmlns="http://www.gexf.net/1.2draft"\n' +
            '      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n' +
            '      xmlns:viz="http://www.gexf.net/1.1draft/viz"\n' +
            '      xsi:schemaLocation="http://www.gexf.net/1.2draft http://www.gexf.net/1.2draft/gexf.xsd"\n'+
            '      version="1.2">\n')
            out_file.write(" <meta lastmodifieddate=\"%s\">\n" % dt.datetime.strftime(date, "%m-%d-%y"))
            out_file.write("  <creator>Nanowire Network Analysis Tool</creator>\n")
            out_file.write("  <description>CS410 Hamilton College Senior Project generated from: %s</description>\n" % self.save_loc)
            out_file.write("  <keywords>cells, schewanella, Hamilton, 410</keywords>\n")
            out_file.write(" </meta>\n")

            # Output graph settings
            # Edge type: Undirected
            # Edge Attributes: edgetype, length, conductivity
            out_file.write(" <graph defaultedgetype=\"undirected\">\n")
            out_file.write("  <attributes class=\"edge\">\n")
            out_file.write("   <attribute id=\"0\" title=\"edgetype\" type=\"string\" />\n")
            out_file.write("   <attribute id=\"1\" title=\"length\" type=\"float\" />\n")
            out_file.write("   <attribute id=\"2\" title=\"conductivity\" type=\"float\" />\n")
            out_file.write("  </attributes>\n")

            # Output nodes
            out_file.write("  <nodes>\n")
            self.write_nodes_gexf(out_file)
            out_file.write("  </nodes>\n")

            # Outpus edges
            out_file.write("  <edges>\n")
            self.write_edges_gexf(out_file)
            out_file.write("  </edges>\n")
            out_file.write(" </graph>\n")
            out_file.write("</gexf>")

    def write_nodes_gexf(self, out_file):
        """ Helper function to output nodes to gexf file. Called by convertToGEXF
            Current visualization settings:
                Color:
                    standard - r:42, g:55, b:235
                    spheroplast - r:255, g:255, b:0
                    curved - r:41, g:235, b:3
                    filament - r:211, g:3, b:235
                Shape:
                    standard - disc
                    spheroplast - square
                    curved - triangle
                    filament - diamond
                Location:
                    same as location in tool
                Size:
                    10
        """
        viz_color_shape = {'standard' : (42, 55, 235, "disc"), 'spheroplast':(255, 255, 0, "square"),
                           'curved': (41, 235, 3, "triangle"), 'filament': (211, 3, 235, "diamond")}
        count = 0
        for key, lst in self.nodeWithTypes.items():
            for elt in lst:
                r, g, b, shape = viz_color_shape[key]
                out_file.write("   <node id=\"%s\" label=\"%s\" >\n" % (getNodeLetter(count), key))
                out_file.write('    <viz:color r="%d" g="%d" b="%d" />\n' % (r, g, b))
                out_file.write('    <viz:position x="%f" y="%f" z="0.0" />\n' % (elt[0], elt[1]))
                out_file.write('    <viz:shape value="%s" />\n' % shape)
                out_file.write('    <viz:size value="10"/>\n')
                out_file.write("   </node>\n")
                count += 1
        out_file.write("   <node id=\"SURFACE\" label=\"surfaceGhost\">\n")
        out_file.write('    <viz:color r="135" g="135" b="135" />\n')
        out_file.write('    <viz:position x="0.0" y="0.0" z="0.0" />\n')
        out_file.write('    <viz:shape value="disc" />\n')
        out_file.write('    <viz:size value="0.01"/>\n')
        out_file.write("   </node>\n")

    def write_edges_gexf(self, out_file):
        """ Helper function to output edges to gexf file. Called by convertToGEXF
            Current visualization settings:
                Color:
                    r:255, g:0, b:0
                Shape:
                    solid
                Thickness:
                    5
        """
        count = 0
        print("Here are all the nodes", self.nodes)
        for i in range(len(self.edges)):
            for j in range(len(self.edges[i])):
                if self.edges[i][j] != 0 and i != j:
                    out_file.write("   <edge id = \"%d\" source=\"%s\" target=\"%s\" weight=\"%f\">\n" % (count, getNodeLetter(i), getNodeLetter(j), self.edges[i][j]))
                    out_file.write("    <attvalues>\n")
                    out_file.write("     <attvalue for=\"0\" value=\"%s\" />\n" % self.get_edge_type(i, j))
                    out_file.write("     <attvalue for=\"1\" value=\"%f\" />\n" % self.get_edge_dist(i, j))
                    out_file.write("     <attvalue for=\"2\" value=\"%f\" />\n" % self.get_edge_ohms(i, j))
                    out_file.write("    </attvalues>\n")
                    out_file.write('    <viz:color r="255" g="0" b="0" />\n')
                    out_file.write('    <viz:thickness value="5" />\n')
                    out_file.write('    <viz:shape value="solid" />\n')
                    out_file.write("   </edge>\n")
                    count += 1
        for node in self.edgeWithTypes['celltosurface']:
            for loc in self.edgeWithTypes['celltosurface'][node]:
                print("Here is the node:", node)
                out_file.write("   <edge id = \"%d\" source=\"%s\" target=\"SURFACE\" weight=\"%f\">\n" % (count, getNodeLetter(self.nodes.index([round(x, 6) for x in node])), self.weight(node, loc)))
                out_file.write("    <attvalues>\n")
                out_file.write("     <attvalue for=\"0\" value=\"celltosurface\" />\n")
                out_file.write("     <attvalue for=\"1\" value=\"%f\" />\n" % self.distance(node, loc))
                out_file.write("     <attvalue for=\"2\" value=\"%f\" />\n" % self.get_edge_ohms(node, loc))
                out_file.write("    </attvalues>\n")
                out_file.write('    <viz:color r="235" g="111" b="3" />\n')
                out_file.write('    <viz:thickness value="0.05" />\n')
                out_file.write('    <viz:shape value="solid" />\n')
                out_file.write("   </edge>\n")
                count += 1

    def get_edge_type(self, i, j):
        """Get type of edge"""
        for key in self.edgeWithTypes:
            if tuple(self.nodes[j]) in self.edgeWithTypes[key]:
                return key

    def get_edge_dist(self, i, j):
        """ Return distance of an edge. Takes indices in self.nodes as parameters """
        return self.distance(self.nodes[i], self.nodes[j])

    def get_edge_ohms(self, i, j):
        return 1.0

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
        if (self.shouldPlotIssues == True):
            self.plotIssues()
        self.MplWidget.canvas.draw()
        self.updateCounterDisplay()
        if (self.shouldAutomate):
            self.status_label.setText("Status: Not Automated")
        else:

            self.status_label.setText("Status: Automated")


        #Disconnecting event handlers (not quite sure about this)
        #for i in range(len(self.cid)):
        #    self.MplWidget.canvas.mpl_disconnect(self.cid[i])

    def plotIssues(self):
        """ Plot rectangles around problem areas after automation """
        for issue in self.issues:
            rect = Rectangle((issue[0],issue[1]),issue[2],issue[3],linewidth=1,edgecolor='g',facecolor='none')
            self.MplWidget.canvas.axes.add_patch(rect)


    def addPoint(self, x_coord, y_coord):
        """ Add node to adjacency matrix """

        #Add more rows/col to edges adj matrix
        x_coord = round(x_coord, 6)
        y_coord = round(y_coord, 6)
        #when a new point is very close to a nearby point, consider to merge it
        #at this point, forbid creating new point which is close to a nearby point to avoid double-clicking
        duplicateNode = False
        for (x,y) in self.nodes:
            if self.distance((x,y), (x_coord, y_coord)) < self.nodeRdius * 2:
                duplicateNode = True
                break

        if not duplicateNode:
            if len(self.nodes) == 0:
                self.edges = [[1]]
            else:
                self.edges = np.pad(self.edges, ((0,1),(0,1)), 'constant')
                self.edges[-1][-1] = 1

            self.nodes.append([x_coord, y_coord])

            self.nodeWithTypes[self.buttonType].append([x_coord, y_coord])
            self.replotImage()
            self.saved = False

    def removePoint(self, x_coord, y_coord):
        """ Remove node from adjacency matrix """
        if len(self.nodes) > 0:
            del_ind, del_dist = self.findClosestNode(x_coord, y_coord)
            # delete from nodeWithTypes
            for ntype in self.nodeWithTypes:
                for i in self.nodeWithTypes[ntype]:
                    if self.nodes[del_ind] == i:
                        self.nodeWithTypes[ntype].remove(self.nodes[del_ind])

            del self.nodes[del_ind]
            self.edges = np.delete(self.edges, del_ind, axis=0)
            self.edges = np.delete(self.edges, del_ind, axis=1)
            self.replotImage()
            self.saved = False

    def lineStart(self, x_coord, y_coord):
        """ Save where the line starts """
        x_coord = round(x_coord, 6)
        y_coord = round(y_coord, 6)
        min_ind, min_dist = self.findClosestNode(x_coord, y_coord)
        self.edgeStart = min_ind
        self.edgeStartNode = [x_coord, y_coord]

    def lineEnd(self, x_coord, y_coord):
        """ At the end of the line add edge to matrix """
        x_coord = round(x_coord, 6)
        y_coord = round(y_coord, 6)
        min_ind, min_dist = self.findClosestNode(x_coord, y_coord)
        self.edgeEnd = min_ind
        # print(self.weight())

        self.edges[self.edgeStart][self.edgeEnd] = self.weight()
        self.edges[self.edgeEnd][self.edgeStart] = self.weight()
        # self.edgeWithTypes[self.buttonType].append([x_coord, y_coord])
        print(self.edgeWithTypes)
        self.replotImage()
        self.saved = False

    def removeLine(self, x_coord, y_coord):
        """ Remove an edge from the matrix """
        x_coord = round(x_coord, 6)
        y_coord = round(y_coord, 6)
        del_ind, dist = self.findClosestEdge(x_coord, y_coord)
        # print(self.buttonType)
        # if self.buttonType == "celltocell":
        found = False
        # print("before:", self.edgeWithTypes)
        for edgeType in self.edgeWithTypes:
            if edgeType != "celltosurface":
                try:
                    endpoint1 = self.nodes[self.edgeNodes[del_ind][0]]
                    endpoint2 = self.nodes[self.edgeNodes[del_ind][1]]
                    print("1:", endpoint1)
                    print("2:", endpoint2)
                    print("current edgeWithTypes", self.edgeWithTypes)
                except IndexError:
                    # Dan: prevent index out of bound
                    continue

                if tuple(endpoint1) in self.edgeWithTypes[edgeType] and \
                endpoint2 in self.edgeWithTypes[edgeType][tuple(endpoint1)]:
                    self.edgeWithTypes[edgeType][tuple(endpoint1)].remove(endpoint2)
                    self.edges[self.edgeNodes[del_ind][0]][self.edgeNodes[del_ind][1]] = 0
                    self.edges[self.edgeNodes[del_ind][1]][self.edgeNodes[del_ind][0]] = 0
                    del self.edgeNodes[del_ind]
                    found = True
                    break
                elif tuple(endpoint2) in self.edgeWithTypes[edgeType] and \
                endpoint1 in self.edgeWithTypes[edgeType][tuple(endpoint2)]:
                    self.edgeWithTypes[edgeType][tuple(endpoint2)].remove(endpoint1)
                    self.edges[self.edgeNodes[del_ind][0]][self.edgeNodes[del_ind][1]] = 0
                    self.edges[self.edgeNodes[del_ind][1]][self.edgeNodes[del_ind][0]] = 0
                    del self.edgeNodes[del_ind]
                    found = True
                    break
            else:
                surface = self.edgeCenters[del_ind]
                for k in self.edgeWithTypes["celltosurface"]:
                    for surfaceNode in self.edgeWithTypes["celltosurface"][k]:
                        if surfaceNode == surface:
                            self.edgeWithTypes["celltosurface"][k].remove(surfaceNode)
                            found = True
                            break
        if not found:
            raise Exception("edge with {} center point is not found, current edges:{}".format(self.edgeCenters[del_ind],self.edgeWithTypes))
         # for startNode in self.edgeWithTypes[edgeType]:
         #     if endpoint1[0] - self.nodeRdius <= startNode[0] <= endpoint1[0] + self.nodeRdius and \
         #     endpoint1[1] - self.nodeRdius <= startNode[1] <= endpoint1[1] + self.nodeRdius:
         #         print("SP:",self.edgeWithTypes[edgeType][startNode])
         #         tempList = self.edgeWithTypes[edgeType][startNode]
         #         tempList.remove(endpoint2)
         #         self.edgeWithTypes[edgeType][startNode] = tempList
         #     elif endpoint2[0] - self.nodeRdius <= startNode[0] <= endpoint2[0] + self.nodeRdius and \
         #     endpoint2[1] - self.nodeRdius <= startNode[1] <= endpoint2[1] + self.nodeRdius:
         #         print("EP:",self.edgeWithTypes[edgeType][startNode])
         #         tempList = self.edgeWithTypes[edgeType][startNode]
         #         tempList.remove(endpoint1)
         #         self.edgeWithTypes[edgeType][startNode] = tempList

        del self.edgeCenters[del_ind]
        self.replotImage()
        # print("After deletion", self.edgeWithTypes)
        self.saved = False

    def removeNearest(self, x_coord, y_coord):
        """ Remove nearesr edge or node """
        x_coord = round(x_coord, 6)
        y_coord = round(y_coord, 6)
        ind1, node_dist = self.findClosestNode(x_coord, y_coord)
        ind2, edge_dist = self.findClosestEdge(x_coord, y_coord)
        if (node_dist < edge_dist) or (ind2 == -1):
            self.removePoint(x_coord, y_coord)
        else:
            self.removeLine(x_coord, y_coord)
        self.saved = False

    def onpress(self, event):
        """ Save that mouse is clicked """
        self.press = True

    def onmove(self, event):
        """ Save when mouse is moved"""
        if self.press:
            self.move = True

    def onrelease(self, event):
        """ Called when a click occurs. Calls onClick which handles the logic of a click"""
        if self.press and not self.move:
            self.onClick(event)
        self.press = False
        self.move = False

    def resetCounterDisplay(self):
        """Set counter text to zeros """
        counterDisplayText = "Node Counters:\n\n"
        for n in self.nodeTypes:
            self.nodeWithTypes[n] = []
            counterDisplayText += n + ": 0\n"
        counterDisplayText += "\nEdge Counters:\n\n"
        for e in self.edgeTypes:
            self.edgeWithTypes[e] = dict()
            counterDisplayText += e + ": 0\n"
        self.counter_label.setText(counterDisplayText)

    def updateCounterDisplay(self):
        """Update counter text when things are selected """
        counterDisplayText = "Node Counters:\n\n"
        for n in self.nodeTypes:
            counterDisplayText += n + ": " + str(len(self.nodeWithTypes[n])) +  "\n"
        counterDisplayText += "\nEdge Counters:\n\n"
        for e in self.edgeTypes:
            counterDisplayText += e + ": "
            if e == 'celltosurface':
                counter = 0
                for k in self.edgeWithTypes['celltosurface']:
                    counter += len(self.edgeWithTypes['celltosurface'][k])
                counterDisplayText += str(counter) + "\n"
            else:
                counter = 0
                for n in self.edgeWithTypes[e]:
                    counter += len(self.edgeWithTypes[e][n])
                counterDisplayText += str(counter) + "\n"
        self.counter_label.setText(counterDisplayText)

    def updateToolTipDisplay(self, button):
        """Update tip text that tells how to use selected tool"""
        text = 'Current Button Type: ' + button + "\n\n"
        if button == "clear":
            text = text + "Tip:\nYou can click on any existing \n" + \
            "node to change their type.\n" + \
            "Clicking elsewhere will not \n" + \
            "create a new object."
        elif button == "standard" or button == "spheroplast" or button == "curved" or button == "filament":
            text = text + "Tip:\nYou can click anywhere \n" + \
            "on the image to create a node\n" + \
            "indicating a" + button + "cell.\n"
        elif button == "celltocell":
            text = text + "Tip:\nYou can click on two nodes \n" + \
            "on the image to create\n" + \
            "a cell to cell edge. Such an edge\n" + \
            "has weight based on length."
        elif button == "celltosurface":
            text = text + "Tip:\nYou can click on a node \n" + \
            "and anywhere on image to create\n" + \
            "a cell to surface edge. Such an edge\n" + \
            "has weight based on length."
        elif button == "cellcontact":
            text = text + "Tip:\nYou can click on two nodes \n" + \
            "on the image to create\n" + \
            "a cell to cell edge. Such an edge\n" + \
            "has a constant weight."

        self.tooltip_label.setText(text)

    def addNode(self, buttonType):
        self.button = 'node'
        self.buttonType = buttonType
        if buttonType == "clear":
            self.button = ''
        self.saved = False
        self.updateToolTipDisplay(buttonType)

    def addEdge(self, buttonType):
        self.button = 'edge'
        self.buttonType = buttonType
        self.saved = False
        self.updateToolTipDisplay(buttonType)
        # if self.filename != '' and len(self.nodes) >= 2:
        #     self.cid.append(self.MplWidget.canvas.mpl_connect('button_press_event', self.lineStart))
        #     self.cid.append(self.MplWidget.canvas.mpl_connect('button_press_event', self.lineEnd))

    def weight(self, a_start=None, an_end=None):
        """ Our weighting function. Returns the distance in microns"""
        if a_start and an_end:
            print("Start/end", a_start, an_end)
            return self.distance(a_start, an_end) * self.pxdist
        if self.button == "celltocell":
            return self.pxdist
        x1, y1 = self.nodes[self.edgeStart]
        x2, y2 = self.nodes[self.edgeEnd]
        dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
        return self.pxdist * dist

    def save_plot(self):
        """ This function creates a save file for user to pick up their project where they left off """
        curr_time = str(dt.datetime.now())
        # QInputDialog.getText("Save Project", "Project name:", QLineEdit.Normal, "")
        # if okPressed:
        #print("Save path is: %s, File name is: %s, Save file location is: %s" % (self.save_loc, self.filename, os.path.join(self.save_loc, self.filename)))
        # save_file_name = os.path.join(self.save_loc, self.filename.split('/')[-1]) if self.filename != '' else os.path.join("%s" % self.save_loc, "SaveFile")
        save_file_name, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","", "NWAS Files (*.nwas)")
        save_file_name += (".nwas" if save_file_name[-5:] != ".nwas" else "")
        if not save_file_name:
            return
        self.save_loc = save_file_name
        print(save_file_name)
        # for c in curr_time:
        #     if not c in ['-', ' ', ':', '.']:
        #         save_file_name += c
        #     else:
        #         save_file_name += '_'
        with open(save_file_name, "w+") as out_file:

            out_file.write("%f\n" % self.pxdist)
            # Write node coords
            for i in range(len(self.nodeTypes)):
                n_type = self.nodeTypes[i]
                for x, y in self.nodeWithTypes[n_type][:-1]:
                    out_file.write("%.6f,%.6f,%s," % (x, y, n_type))
                try:
                    if (i < len(self.nodeTypes) - 1):
                        out_file.write("%.6f,%.6f,%s," % (self.nodeWithTypes[n_type][-1][0], self.nodeWithTypes[n_type][-1][1], n_type))
                    else:
                        out_file.write("%.6f,%.6f,%s" % (self.nodeWithTypes[n_type][-1][0], self.nodeWithTypes[n_type][-1][1], n_type))
                except:
                    out_file.write("")
            out_file.write("\n")

            # Write adjacency matrix
            out_file.write("%d\n" % len(self.edges))
            for i in range(len(self.edges)):
                for j in range(len(self.edges[i])):
                    out_file.write("%.6f " % self.edges[i][j])
                out_file.write('\n')

            # Write node to surface dict
            for key in self.edgeWithTypes['celltosurface']:
                print("Examining Key {}".format(key))
                print("Seeing: ",self.edgeWithTypes)
                kx, ky = key
                val = self.edgeWithTypes['celltosurface'][key]
                for [vx, vy] in val:
                    out_file.write("%s,%s:%s,%s\n" % (kx, ky, vx, vy))
                    # for elt in val[:-1]:
                    #     out_file.write("%s:" % elt)
                    # try:
                    #     out_file.write("%s\n" % val[-1])
                    # except:
                    #     out_file.write("NONE")
            out_file.write("$img$\n")

            # Write image binary
            out_file.write("%s\n" % self.filename)

            # Dan: above code stores edge matrix, but we also need to store edge type,
            # so I append edgeWithTypes in the end to avoid file read conflict
            out_file.write(str(self.edgeWithTypes) + "\n")
            out_file.write(str(self.nodes) + "\n")
            out_file.write(str(self.edges) + "\n")
            out_file.write(str(self.edgeCenters) + "\n")
            out_file.write(str(self.edgeNodes) + "\n")
            out_file.write(str(self.calibration_point_coords) + "\n")
            out_file.write(str(self.calibration_points) + "\n")



            out_file.close()
            # out_file = open(save_file_name, "ab")
            # with open(self.filename, "rb") as img_file:
            #     data = img_file.read()
            #     out_file.write(data)

            # out_file.close()
            self.saved = True

    def open_plot(self):
        """ Opens a .nwas file and restores session """
        if self.filename != '':
            if not self.saved:
                msg = QMessageBox.warning(self, "File not saved",
                                            "You are about to leave the current project. Do you want to continue without saving?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if msg == QMessageBox.No:
                    return
        #fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Save File", self.save_loc, "NWAS Files (*.nwas)")
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Save File", "","NWAS Files (*.nwas)")
        if fileName:
            self.resetPlot()
            self.save_loc = fileName
            # We will read this many lines again after reopening the file so that we can read the image file
            lines_read = 0
            with open(fileName, 'r') as saved_file:
                self.pxdist = float(saved_file.readline().strip())
                # Read the node coords and add them to self.nodes
                nodes = saved_file.readline().strip().split(',')
                lines_read += 1
                for i in range(0, len(nodes), 3):
                    if (len(str(nodes[i]).strip()) > 0):
                        nx, ny = float(nodes[i]), float(nodes[i + 1])
                        self.nodes.append([nx, ny])
                        if not nodes[i + 2] in self.nodeWithTypes:
                            self.nodeWithTypes[nodes[i + 2]] = []
                        self.nodeWithTypes[nodes[i + 2]].append([nx, ny])

                # Read in the number of nodes
                num_nodes = int(saved_file.readline().strip())
                lines_read += 1

                for i in range(num_nodes):
                    line = saved_file.readline().strip().split()
                    lines_read += 1

                    self.edges.append([float(x) for x in line])

                line = saved_file.readline().strip()
                while line != "$img$":
                    bits = line.split(':')
                    kx, ky = [float(x) for x in bits[0].split(',')]
                    vx, vy = [float(x) for x in bits[1].split(',')]
                    if not (kx, ky) in self.edgeWithTypes['celltosurface']:
                        self.edgeWithTypes['celltosurface'][(kx, ky)] = []
                    self.edgeWithTypes['celltosurface'][(kx, ky)].append([vx, vy])
                    line = saved_file.readline().strip()
                img_file_name = saved_file.readline().strip()
                lines_read += 1
                self.filename = img_file_name

                # Dan: read edgeWithTypes into dictionary
                # eval is not the safest way, but don't want to import new lib
                try:
                    self.edgeWithTypes = eval(saved_file.readline().strip())
                    self.nodes = eval(saved_file.readline().strip())
                    self.edges = eval(saved_file.readline().strip())
                    self.edgeCenters = eval(saved_file.readline().strip())
                    self.edgeNodes = eval(saved_file.readline().strip())
                    self.calibration_point_coords = eval(saved_file.readline().strip())
                    self.calibration_points = eval(saved_file.readline().strip())

                    print(self.edgeWithTypes)
                    print(self.nodes)
                except SyntaxError:
                    # older test file don't have this,so it needs to be handled
                    print("older test file don't have edgeWithTypes saved,so it needs to be handled")



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
                                            "Make sure file '%s' exists" % self.filename)
                    return
                gray_arr = np.asarray(image)
                #print(gray_arr)
                rgb_arr = np.stack((gray_arr, gray_arr, gray_arr), axis=-1)
                #print(rgb_arr)
                imgplot = self.MplWidget.canvas.axes.imshow(rgb_arr)

                self.MplWidget.canvas.draw()
                self.replotImage()
                self.saved = True

    def calibrate_measure(self, args=[]):
        """ This function serves two distinct purposes depending on when it is called.
            if it is called while not currently calibrating then it starts calibration mode
            otherwise it calculates a length per pixel in microns """
        if not self.calibrating:
            self.pxdist = 0.0
            msg = QMessageBox.information(self, "Measure calibration",
                                                u"To calibrate the measurement tool, select point A and point B, then enter the distance between the two in \u03bcm")
            self.calibration_points = []
            self.calibrating = True
        else:
            val = self.get_int()
            if val:
                x1, y1 = self.calibration_point_coords[0]
                x2, y2 = self.calibration_point_coords[1]
                dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
                self.pxdist = val / dist
                for p in self.calibration_points:
                    p.remove()
                print(self.pxdist)
                self.calibrating = False

    def get_int(self):
        """ Get an int value from a dialog box """
        i, okPressed = QInputDialog.getInt(self, "Set distance",u"Distance (\u03bcm):", 10, 0, 100, 1)
        return i if okPressed else None


def getNodeLetter(num):
    """ Converts a number to a letter A-Z, AA-ZZ, ... """
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
    #ui_logic.calibrate_measure()
    sys.exit(app.exec_())

main()

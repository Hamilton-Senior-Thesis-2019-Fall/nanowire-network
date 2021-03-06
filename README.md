# About
Nanowire-Network is an analysis tool to measure characteristics of biologically produced
nanowire networks that spontaneously form between Shewanella oneidensis bacteria under
specific growth conditions.
![alt text](https://github.com/Hamilton-Senior-Thesis-2019-Fall/nanowire-network/blob/master/demo.PNG "demo")


## Installation
**Python is needed to run this program:**
Download from here: *https://www.python.org/downloads/*

**Clone or download the git repo:**
To download click green *Clone or Download* button on this page and then click *Download ZIP*.

**Install dependencies:**
Navigate inside Nanowire-Network folder to *NanowireNetworkInstall*. Double click file.

**To Run:**
Navigate inside Nanowire-Network folder to *NanowireNetworkRun*. Double click file. A window should open up with tools around the edge and a blank white screen in the middle.


## User Guide
### Open File
1.  Navigate to **Import** and click **Upload** from computer.
2.  Select the image you wish to work with. (Ideally .tiff)
### Get Started
Once image is opened, a pop up will ask you to calibrate the distance.
1.  Click ok and then click either side of the ruler in the image.
2.  Another popup will show up asking you how far the two points you clicked were.
3.  The default is 10 micrometers but this can be altered if the ruler is a different length.
### Automation
1. Navigate to **Automation** and click **Activate**
2. Click Yes in the pop up to start automation. This process is going to take some time. (* You will see a Status: Automating... on the right bottom corner of the window which indicates the process is still ongoing.)
3. Once finished, you will see green squares and blue nodes. The green squares are areas where the cells were too crowded to differentiate between and should be examined by a human.
4. At this point you can continue to work on the image as needed, adding nodes and edges.
5. To change the node type use the top button on the left. Clicking a node will cycle through the different types.
6. To toggle the green squares simply hold down `cmd` on Mac or `ctrl` on Windows, and click on the **Activate**  again. The green squares can be contiuously toggled as needed.
### Add Nodes
To add a node, select the type from the left side and simply click on the cell you wish to place it. The nodes are on the left, in descending order – normal, spherical cells, curved cells, and long cells. A tool tip will appear on the right of the screen explaining more.
### Add Edges
To add an edge, select the type from the left side and click two spots between which an edge will appear. The edges are below the cells in descending order, cell to cell, cell to surface, and cell to cell contact. A tool tip will appear on the right of the screen explaining more. The program will connect the two nodes closest to the spots you have clicked. However, if you choose to use a cell to surface edge, the second connection will not jump to a close cell, instead staying where your second click was.
### Delete Edges
Hold down `cmd` on Mac, `ctrl` on Windows, you will see a dot appear on the center of the edges. To delete simply click on the center dot of the edge you intend to delete.
### Delete Nodes
Hold down `cmd` on Mac, `ctrl` on Windows, and simply click nearby the node you intend to delete.
### Save File
To save navigate to *Export*. Click *Save file*. A window will pop up, choose where to save the project, and what to name it.
### Export
To export navigate to *Export*. Click *Export to Gephi* to create a .csv file. Click *Export to Cytoscape* to create a .gexf, which is the recommended choice. These will just create a file with the exported information in the same folder. You can then navigate to this and load it into Gephi. Both file types are recognized by Gephi.
### Import from Saved File
To upload this saved file navigate to *Import*. Click *Upload from saved projects* and select the file. It should load to where you were before.

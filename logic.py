from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from mockup import Ui_MainWindow

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.activateButtons()
        self.show()


    def activateButtons(self):
        self.actionUpload_from_computer.triggered.connect(self.setImage)
        self.pushButton_standard_node.clicked.connect(self.addNode)

    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp *.tif)") # Ask for file
        if fileName: # If the user gives a file
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.viewPort.width(), self.viewPort.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.viewPort.setPixmap(pixmap) # Set the pixmap onto the label
            self.viewPort.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center

    def addNode(self):
        print('adding node')

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui_logic = Logic()
    sys.exit(app.exec_())

main()

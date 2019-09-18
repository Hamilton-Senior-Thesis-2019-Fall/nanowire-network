# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mockup.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 682)
        MainWindow.setStyleSheet("#MainWindow {\n"
"background: #2c3539\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_info_layers = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_info_layers.setGeometry(QtCore.QRect(986, 20, 141, 621))
        self.tabWidget_info_layers.setAutoFillBackground(True)
        self.tabWidget_info_layers.setStyleSheet("tabWidget_info_layers {\n"
"background: #d8d8d8\n"
"}")
        self.tabWidget_info_layers.setObjectName("tabWidget_info_layers")
        self.tab_info_tab = QtWidgets.QWidget()
        self.tab_info_tab.setObjectName("tab_info_tab")
        self.tabWidget_info_layers.addTab(self.tab_info_tab, "")
        self.tab_layers_tab = QtWidgets.QWidget()
        self.tab_layers_tab.setObjectName("tab_layers_tab")
        self.tabWidget_info_layers.addTab(self.tab_layers_tab, "")
        self.frame_photo_frame = QtWidgets.QFrame(self.centralwidget)
        self.frame_photo_frame.setGeometry(QtCore.QRect(69, 39, 921, 601))
        self.frame_photo_frame.setMouseTracking(True)
        self.frame_photo_frame.setAutoFillBackground(False)
        self.frame_photo_frame.setStyleSheet("#frame_photo_frame {\n"
"background: #ffffff\n"
"}")
        self.frame_photo_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_photo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_photo_frame.setObjectName("frame_photo_frame")
        self.tabWidget_toolbar = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_toolbar.setGeometry(QtCore.QRect(0, 20, 71, 621))
        self.tabWidget_toolbar.setAutoFillBackground(True)
        self.tabWidget_toolbar.setStyleSheet("tabWidget_toolbar {\n"
"background: #d8d8d8\n"
"}")
        self.tabWidget_toolbar.setObjectName("tabWidget_toolbar")
        self.tabWidget_toolbarPage1 = QtWidgets.QWidget()
        self.tabWidget_toolbarPage1.setObjectName("tabWidget_toolbarPage1")
        self.pushButton_standard_node = QtWidgets.QPushButton(self.tabWidget_toolbarPage1)
        self.pushButton_standard_node.setGeometry(QtCore.QRect(10, 40, 51, 41))
        self.pushButton_standard_node.setStyleSheet("#pushButton_standard_node {\n"
"background-color: transparent;\n"
"border-image: url(:imgs/standard_node.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#pushButton_standard_node:pressed{\n"
"border: 2px solid #000000\n"
"}\n"
"    ")
        self.pushButton_standard_node.setText("")
        self.pushButton_standard_node.setObjectName("pushButton_standard_node")
        self.pushButton_standard_edge = QtWidgets.QPushButton(self.tabWidget_toolbarPage1)
        self.pushButton_standard_edge.setGeometry(QtCore.QRect(20, 90, 31, 31))
        self.pushButton_standard_edge.setStyleSheet("#pushButton_standard_edge {\n"
"background-color: transparent;\n"
"border-image: url(:imgs/standard_edge.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#pushButton_standard_edge:pressed{\n"
"border: 2px solid #000000\n"
"}\n"
"    ")
        self.pushButton_standard_edge.setText("")
        self.pushButton_standard_edge.setObjectName("pushButton_standard_edge")
        self.tabWidget_toolbar.addTab(self.tabWidget_toolbarPage1, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 21))
        self.menubar.setObjectName("menubar")
        self.menuImport = QtWidgets.QMenu(self.menubar)
        self.menuImport.setObjectName("menuImport")
        self.menuExport = QtWidgets.QMenu(self.menubar)
        self.menuExport.setObjectName("menuExport")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUpload_from_computer = QtWidgets.QAction(MainWindow)
        self.actionUpload_from_computer.setObjectName("actionUpload_from_computer")
        self.actionUpload_from_saved_projects = QtWidgets.QAction(MainWindow)
        self.actionUpload_from_saved_projects.setObjectName("actionUpload_from_saved_projects")
        self.actionSave_file = QtWidgets.QAction(MainWindow)
        self.actionSave_file.setObjectName("actionSave_file")
        self.actionExport_to_Gephi = QtWidgets.QAction(MainWindow)
        self.actionExport_to_Gephi.setObjectName("actionExport_to_Gephi")
        self.actionExport_to_Cytoscape = QtWidgets.QAction(MainWindow)
        self.actionExport_to_Cytoscape.setObjectName("actionExport_to_Cytoscape")
        self.actionColor_select = QtWidgets.QAction(MainWindow)
        self.actionColor_select.setObjectName("actionColor_select")
        self.menuImport.addAction(self.actionUpload_from_computer)
        self.menuImport.addAction(self.actionUpload_from_saved_projects)
        self.menuExport.addAction(self.actionSave_file)
        self.menuExport.addAction(self.actionExport_to_Gephi)
        self.menuExport.addAction(self.actionExport_to_Cytoscape)
        self.menuSettings.addAction(self.actionColor_select)
        self.menubar.addAction(self.menuImport.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.viewPort = QtWidgets.QLabel(self.centralwidget)
        self.viewPort.setGeometry(QtCore.QRect(69, 39, 921, 601))
        self.viewPort.setFrameShape(QtWidgets.QFrame.Box)
        self.viewPort.setFrameShadow(QtWidgets.QFrame.Plain)
        self.viewPort.setLineWidth(1)
        self.viewPort.setMidLineWidth(0)
        self.viewPort.setObjectName("viewPort")

        self.retranslateUi(MainWindow)
        self.tabWidget_info_layers.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget_info_layers.setTabText(self.tabWidget_info_layers.indexOf(self.tab_info_tab), _translate("MainWindow", "Info"))
        self.tabWidget_info_layers.setTabText(self.tabWidget_info_layers.indexOf(self.tab_layers_tab), _translate("MainWindow", "Layers"))
        self.tabWidget_toolbar.setTabText(self.tabWidget_toolbar.indexOf(self.tabWidget_toolbarPage1), _translate("MainWindow", "Tools"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionUpload_from_computer.setText(_translate("MainWindow", "Upload from computer"))
        self.actionUpload_from_saved_projects.setText(_translate("MainWindow", "Upload from saved projects"))
        self.actionSave_file.setText(_translate("MainWindow", "Save file"))
        self.actionExport_to_Gephi.setText(_translate("MainWindow", "Export to Gephi"))
        self.actionExport_to_Cytoscape.setText(_translate("MainWindow", "Export to Cytoscape"))
        self.actionColor_select.setText(_translate("MainWindow", "Color select"))
        self.viewPort.setText(_translate("MainWindow", "TextLabel"))

import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

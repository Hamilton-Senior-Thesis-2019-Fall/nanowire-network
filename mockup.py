# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dehao\Desktop\nanowire-network\mockup.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 847)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 0))
        MainWindow.setStyleSheet("#MainWindow {\n"
"background: #2c3539\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget_toolbar = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_toolbar.setMaximumSize(QtCore.QSize(80, 16777215))
        self.tabWidget_toolbar.setAutoFillBackground(True)
        self.tabWidget_toolbar.setStyleSheet("tabWidget_toolbar {\n"
"background: #d8d8d8\n"
"}")
        self.tabWidget_toolbar.setObjectName("tabWidget_toolbar")
        self.tabWidget_toolbarPage1 = QtWidgets.QWidget()
        self.tabWidget_toolbarPage1.setObjectName("tabWidget_toolbarPage1")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tabWidget_toolbarPage1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(6, 100, 61, 611))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.node_painter_standard = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.node_painter_standard.sizePolicy().hasHeightForWidth())
        self.node_painter_standard.setSizePolicy(sizePolicy)
        self.node_painter_standard.setMinimumSize(QtCore.QSize(0, 0))
        self.node_painter_standard.setMaximumSize(QtCore.QSize(40, 40))
        self.node_painter_standard.setToolTip("")
        self.node_painter_standard.setStyleSheet("#node_painter_standard {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#node_painter_standard:pressed{\n"
"border: 6px solid #000000\n"
"}\n"
"    ")
        self.node_painter_standard.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("standard_node.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.node_painter_standard.setIcon(icon)
        self.node_painter_standard.setObjectName("node_painter_standard")
        self.gridLayout_2.addWidget(self.node_painter_standard, 2, 0, 1, 1)
        self.pushButton_standard_node = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_standard_node.sizePolicy().hasHeightForWidth())
        self.pushButton_standard_node.setSizePolicy(sizePolicy)
        self.pushButton_standard_node.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButton_standard_node.setMaximumSize(QtCore.QSize(30, 30))
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
        self.gridLayout_2.addWidget(self.pushButton_standard_node, 0, 0, 1, 1)
        self.node_painter_filament = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.node_painter_filament.sizePolicy().hasHeightForWidth())
        self.node_painter_filament.setSizePolicy(sizePolicy)
        self.node_painter_filament.setMinimumSize(QtCore.QSize(40, 40))
        self.node_painter_filament.setMaximumSize(QtCore.QSize(40, 40))
        self.node_painter_filament.setToolTip("")
        self.node_painter_filament.setText("")
        self.node_painter_filament.setObjectName("node_painter_filament")
        self.gridLayout_2.addWidget(self.node_painter_filament, 5, 0, 1, 1)
        self.node_painter_spheroplast = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.node_painter_spheroplast.sizePolicy().hasHeightForWidth())
        self.node_painter_spheroplast.setSizePolicy(sizePolicy)
        self.node_painter_spheroplast.setMinimumSize(QtCore.QSize(40, 40))
        self.node_painter_spheroplast.setMaximumSize(QtCore.QSize(40, 40))
        self.node_painter_spheroplast.setToolTip("")
        self.node_painter_spheroplast.setText("")
        self.node_painter_spheroplast.setObjectName("node_painter_spheroplast")
        self.gridLayout_2.addWidget(self.node_painter_spheroplast, 3, 0, 1, 1)
        self.edge_painter_celltocell = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edge_painter_celltocell.sizePolicy().hasHeightForWidth())
        self.edge_painter_celltocell.setSizePolicy(sizePolicy)
        self.edge_painter_celltocell.setMinimumSize(QtCore.QSize(40, 40))
        self.edge_painter_celltocell.setMaximumSize(QtCore.QSize(40, 40))
        self.edge_painter_celltocell.setToolTip("")
        self.edge_painter_celltocell.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("standard_edge.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edge_painter_celltocell.setIcon(icon1)
        self.edge_painter_celltocell.setObjectName("edge_painter_celltocell")
        self.gridLayout_2.addWidget(self.edge_painter_celltocell, 6, 0, 1, 1)
        self.pushButton_standard_edge = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_standard_edge.sizePolicy().hasHeightForWidth())
        self.pushButton_standard_edge.setSizePolicy(sizePolicy)
        self.pushButton_standard_edge.setMaximumSize(QtCore.QSize(30, 30))
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
        self.gridLayout_2.addWidget(self.pushButton_standard_edge, 1, 0, 1, 1)
        self.node_painter_curved = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.node_painter_curved.sizePolicy().hasHeightForWidth())
        self.node_painter_curved.setSizePolicy(sizePolicy)
        self.node_painter_curved.setMinimumSize(QtCore.QSize(40, 40))
        self.node_painter_curved.setMaximumSize(QtCore.QSize(40, 40))
        self.node_painter_curved.setToolTip("")
        self.node_painter_curved.setText("")
        self.node_painter_curved.setObjectName("node_painter_curved")
        self.gridLayout_2.addWidget(self.node_painter_curved, 4, 0, 1, 1)
        self.node_painter_celltosurface = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.node_painter_celltosurface.sizePolicy().hasHeightForWidth())
        self.node_painter_celltosurface.setSizePolicy(sizePolicy)
        self.node_painter_celltosurface.setMinimumSize(QtCore.QSize(40, 40))
        self.node_painter_celltosurface.setMaximumSize(QtCore.QSize(40, 40))
        self.node_painter_celltosurface.setToolTip("")
        self.node_painter_celltosurface.setText("")
        self.node_painter_celltosurface.setObjectName("node_painter_celltosurface")
        self.gridLayout_2.addWidget(self.node_painter_celltosurface, 7, 0, 1, 1)
        self.node_painter_cellcontact = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.node_painter_cellcontact.sizePolicy().hasHeightForWidth())
        self.node_painter_cellcontact.setSizePolicy(sizePolicy)
        self.node_painter_cellcontact.setMinimumSize(QtCore.QSize(40, 40))
        self.node_painter_cellcontact.setMaximumSize(QtCore.QSize(40, 40))
        self.node_painter_cellcontact.setToolTip("")
        self.node_painter_cellcontact.setText("")
        self.node_painter_cellcontact.setObjectName("node_painter_cellcontact")
        self.gridLayout_2.addWidget(self.node_painter_cellcontact, 8, 0, 1, 1)
        self.tabWidget_toolbar.addTab(self.tabWidget_toolbarPage1, "")
        self.horizontalLayout_2.addWidget(self.tabWidget_toolbar)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.MplWidget.setToolTip("")
        self.MplWidget.setObjectName("MplWidget")
        self.horizontalLayout_2.addWidget(self.MplWidget)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.tabWidget_info_layers = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_info_layers.setMaximumSize(QtCore.QSize(200, 16777215))
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
        self.horizontalLayout_2.addWidget(self.tabWidget_info_layers)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 21))
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

        self.retranslateUi(MainWindow)
        self.tabWidget_info_layers.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget_toolbar.setTabText(self.tabWidget_toolbar.indexOf(self.tabWidget_toolbarPage1), _translate("MainWindow", "Tools"))
        self.tabWidget_info_layers.setTabText(self.tabWidget_info_layers.indexOf(self.tab_info_tab), _translate("MainWindow", "Info"))
        self.tabWidget_info_layers.setTabText(self.tabWidget_info_layers.indexOf(self.tab_layers_tab), _translate("MainWindow", "Layers"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionUpload_from_computer.setText(_translate("MainWindow", "Upload from computer"))
        self.actionUpload_from_saved_projects.setText(_translate("MainWindow", "Upload from saved projects"))
        self.actionSave_file.setText(_translate("MainWindow", "Save file"))
        self.actionExport_to_Gephi.setText(_translate("MainWindow", "Export to Gephi"))
        self.actionExport_to_Cytoscape.setText(_translate("MainWindow", "Export to Cytoscape"))
        self.actionColor_select.setText(_translate("MainWindow", "Color select"))
from mplwidget import MplWidget
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lavimoe\Desktop\cs2019F\nanowire-network\mockup.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1216, 904)
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
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 71, 661))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.edge_painter_cellcontact = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edge_painter_cellcontact.sizePolicy().hasHeightForWidth())
        self.edge_painter_cellcontact.setSizePolicy(sizePolicy)
        self.edge_painter_cellcontact.setMinimumSize(QtCore.QSize(40, 40))
        self.edge_painter_cellcontact.setMaximumSize(QtCore.QSize(40, 40))
        self.edge_painter_cellcontact.setToolTip("")
        self.edge_painter_cellcontact.setStyleSheet("#edge_painter_cellcontact{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#edge_painter_cellcontact:pressed{\n"
"background-color: #cccccc;\n"
"}\n"
"    ")
        self.edge_painter_cellcontact.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cellcontact_edge.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edge_painter_cellcontact.setIcon(icon)
        self.edge_painter_cellcontact.setIconSize(QtCore.QSize(40, 40))
        self.edge_painter_cellcontact.setObjectName("edge_painter_cellcontact")
        self.gridLayout_2.addWidget(self.edge_painter_cellcontact, 7, 0, 1, 1)
        self.node_painter_standard = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
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
"background-color: #cccccc;\n"
"}\n"
"    ")
        self.node_painter_standard.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("standard_node.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.node_painter_standard.setIcon(icon1)
        self.node_painter_standard.setIconSize(QtCore.QSize(30, 30))
        self.node_painter_standard.setObjectName("node_painter_standard")
        self.gridLayout_2.addWidget(self.node_painter_standard, 0, 0, 1, 1)
        self.node_painter_spheroplast = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.node_painter_spheroplast.sizePolicy().hasHeightForWidth())
        self.node_painter_spheroplast.setSizePolicy(sizePolicy)
        self.node_painter_spheroplast.setMinimumSize(QtCore.QSize(0, 0))
        self.node_painter_spheroplast.setMaximumSize(QtCore.QSize(40, 40))
        self.node_painter_spheroplast.setToolTip("")
        self.node_painter_spheroplast.setStyleSheet("#node_painter_spheroplast {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#node_painter_spheroplast:pressed{\n"
"background-color: #cccccc;\n"
"}\n"
"    ")
        self.node_painter_spheroplast.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("spheroplast_node.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.node_painter_spheroplast.setIcon(icon2)
        self.node_painter_spheroplast.setIconSize(QtCore.QSize(30, 30))
        self.node_painter_spheroplast.setObjectName("node_painter_spheroplast")
        self.gridLayout_2.addWidget(self.node_painter_spheroplast, 1, 0, 1, 1)
        self.node_painter_curved = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.node_painter_curved.sizePolicy().hasHeightForWidth())
        self.node_painter_curved.setSizePolicy(sizePolicy)
        self.node_painter_curved.setMinimumSize(QtCore.QSize(40, 40))
        self.node_painter_curved.setMaximumSize(QtCore.QSize(40, 40))
        self.node_painter_curved.setToolTip("")
        self.node_painter_curved.setStyleSheet("#node_painter_curved{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#node_painter_curved:pressed{\n"
"background-color: #cccccc;\n"
"}\n"
"    ")
        self.node_painter_curved.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("curved_node.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.node_painter_curved.setIcon(icon3)
        self.node_painter_curved.setIconSize(QtCore.QSize(30, 30))
        self.node_painter_curved.setObjectName("node_painter_curved")
        self.gridLayout_2.addWidget(self.node_painter_curved, 2, 0, 1, 1)
        self.node_painter_filament = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.node_painter_filament.sizePolicy().hasHeightForWidth())
        self.node_painter_filament.setSizePolicy(sizePolicy)
        self.node_painter_filament.setMinimumSize(QtCore.QSize(40, 40))
        self.node_painter_filament.setMaximumSize(QtCore.QSize(40, 40))
        self.node_painter_filament.setToolTip("")
        self.node_painter_filament.setStyleSheet("#node_painter_filament {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#node_painter_filament:pressed{\n"
"background-color: #cccccc;\n"
"}\n"
"    ")
        self.node_painter_filament.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("filament_node.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.node_painter_filament.setIcon(icon4)
        self.node_painter_filament.setIconSize(QtCore.QSize(30, 30))
        self.node_painter_filament.setObjectName("node_painter_filament")
        self.gridLayout_2.addWidget(self.node_painter_filament, 3, 0, 1, 1)
        self.edge_painter_celltocell = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edge_painter_celltocell.sizePolicy().hasHeightForWidth())
        self.edge_painter_celltocell.setSizePolicy(sizePolicy)
        self.edge_painter_celltocell.setMinimumSize(QtCore.QSize(40, 40))
        self.edge_painter_celltocell.setMaximumSize(QtCore.QSize(40, 40))
        self.edge_painter_celltocell.setToolTip("")
        self.edge_painter_celltocell.setStyleSheet("#edge_painter_celltocell {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#edge_painter_celltocell:pressed{\n"
"background-color: #cccccc;\n"
"}\n"
"    ")
        self.edge_painter_celltocell.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("standard_edge.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edge_painter_celltocell.setIcon(icon5)
        self.edge_painter_celltocell.setIconSize(QtCore.QSize(35, 35))
        self.edge_painter_celltocell.setObjectName("edge_painter_celltocell")
        self.gridLayout_2.addWidget(self.edge_painter_celltocell, 5, 0, 1, 1)
        self.edge_painter_celltosurface = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edge_painter_celltosurface.sizePolicy().hasHeightForWidth())
        self.edge_painter_celltosurface.setSizePolicy(sizePolicy)
        self.edge_painter_celltosurface.setMinimumSize(QtCore.QSize(40, 40))
        self.edge_painter_celltosurface.setMaximumSize(QtCore.QSize(40, 40))
        self.edge_painter_celltosurface.setToolTip("")
        self.edge_painter_celltosurface.setStyleSheet("#edge_painter_celltosurface {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#edge_painter_celltosurface:pressed{\n"
"background-color: #cccccc;\n"
"}\n"
"    ")
        self.edge_painter_celltosurface.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("celltosurface_edge.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edge_painter_celltosurface.setIcon(icon6)
        self.edge_painter_celltosurface.setIconSize(QtCore.QSize(40, 40))
        self.edge_painter_celltosurface.setObjectName("edge_painter_celltosurface")
        self.gridLayout_2.addWidget(self.edge_painter_celltosurface, 6, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 4, 0, 1, 1)
        self.tabWidget_toolbar.addTab(self.tabWidget_toolbarPage1, "")
        self.horizontalLayout_2.addWidget(self.tabWidget_toolbar)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setMinimumSize(QtCore.QSize(600, 700))
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
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_info_tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 202, 661))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(200, 300))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.counter_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.counter_label.setMinimumSize(QtCore.QSize(200, 300))
        self.counter_label.setObjectName("counter_label")
        self.verticalLayout.addWidget(self.counter_label)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.tabWidget_info_layers.addTab(self.tab_info_tab, "")
        self.tab_layers_tab = QtWidgets.QWidget()
        self.tab_layers_tab.setObjectName("tab_layers_tab")
        self.tabWidget_info_layers.addTab(self.tab_layers_tab, "")
        self.horizontalLayout_2.addWidget(self.tabWidget_info_layers)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1216, 21))
        self.menubar.setObjectName("menubar")
        self.menuImport = QtWidgets.QMenu(self.menubar)
        self.menuImport.setObjectName("menuImport")
        self.menuExport = QtWidgets.QMenu(self.menubar)
        self.menuExport.setObjectName("menuExport")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
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
        self.actionAutomation = QtWidgets.QAction(MainWindow)
        self.actionAutomation.setObjectName("actionAutomation")
        self.menuImport.addAction(self.actionUpload_from_computer)
        self.menuImport.addAction(self.actionUpload_from_saved_projects)
        self.menuExport.addAction(self.actionSave_file)
        self.menuExport.addAction(self.actionExport_to_Gephi)
        self.menuExport.addAction(self.actionExport_to_Cytoscape)
        self.menuSettings.addAction(self.actionColor_select)
        self.menuTools.addAction(self.actionAutomation)
        self.menubar.addAction(self.menuImport.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_info_layers.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget_toolbar.setTabText(self.tabWidget_toolbar.indexOf(self.tabWidget_toolbarPage1), _translate("MainWindow", "Tools"))
        self.counter_label.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget_info_layers.setTabText(self.tabWidget_info_layers.indexOf(self.tab_info_tab), _translate("MainWindow", "Info"))
        self.tabWidget_info_layers.setTabText(self.tabWidget_info_layers.indexOf(self.tab_layers_tab), _translate("MainWindow", "Layers"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionUpload_from_computer.setText(_translate("MainWindow", "Upload from computer"))
        self.actionUpload_from_saved_projects.setText(_translate("MainWindow", "Upload from saved projects"))
        self.actionSave_file.setText(_translate("MainWindow", "Save file"))
        self.actionExport_to_Gephi.setText(_translate("MainWindow", "Export to Gephi"))
        self.actionExport_to_Cytoscape.setText(_translate("MainWindow", "Export to Cytoscape"))
        self.actionColor_select.setText(_translate("MainWindow", "Color select"))
        self.actionAutomation.setText(_translate("MainWindow", "Automation"))
from mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

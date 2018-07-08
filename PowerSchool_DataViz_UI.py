# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PowerSchool_DataViz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PowerSchool_DataViz(object):
    def setupUi(self, PowerSchool_DataViz):
        PowerSchool_DataViz.setObjectName("PowerSchool_DataViz")
        PowerSchool_DataViz.resize(1108, 856)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/Round_Landmark_Icon_School.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PowerSchool_DataViz.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(PowerSchool_DataViz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.Graph_Tab = QtWidgets.QWidget()
        self.Graph_Tab.setObjectName("Graph_Tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Graph_Tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Graph_Grid = QtWidgets.QGridLayout()
        self.Graph_Grid.setObjectName("Graph_Grid")
        self.Graph_View = QtWebEngineWidgets.QWebEngineView(self.Graph_Tab)
        self.Graph_View.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.Graph_View.setUrl(QtCore.QUrl("about:blank"))
        self.Graph_View.setObjectName("Graph_View")
        self.Graph_Grid.addWidget(self.Graph_View, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.Graph_Grid, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Graph_Tab, "")
        self.Data_Table_Tab = QtWidgets.QWidget()
        self.Data_Table_Tab.setObjectName("Data_Table_Tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Data_Table_Tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Data_Table_Grid = QtWidgets.QGridLayout()
        self.Data_Table_Grid.setObjectName("Data_Table_Grid")
        self.Data_Table = QtWidgets.QTableWidget(self.Data_Table_Tab)
        self.Data_Table.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.Data_Table.setFrameShape(QtWidgets.QFrame.Panel)
        self.Data_Table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Data_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Data_Table.setAlternatingRowColors(True)
        self.Data_Table.setObjectName("Data_Table")
        self.Data_Table.setColumnCount(0)
        self.Data_Table.setRowCount(0)
        self.Data_Table.horizontalHeader().setVisible(True)
        self.Data_Table.horizontalHeader().setCascadingSectionResizes(True)
        self.Data_Table.horizontalHeader().setSortIndicatorShown(True)
        self.Data_Table.verticalHeader().setVisible(True)
        self.Data_Table.verticalHeader().setCascadingSectionResizes(True)
        self.Data_Table.verticalHeader().setHighlightSections(True)
        self.Data_Table_Grid.addWidget(self.Data_Table, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.Data_Table_Grid, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Data_Table_Tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        PowerSchool_DataViz.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PowerSchool_DataViz)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.File_Menu = QtWidgets.QMenu(self.menubar)
        self.File_Menu.setObjectName("File_Menu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        PowerSchool_DataViz.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(PowerSchool_DataViz)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/baseline-folder_open-24px.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(PowerSchool_DataViz)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/baseline-exit_to_app-24px.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout_PowerSchool_DataViz = QtWidgets.QAction(PowerSchool_DataViz)
        self.actionAbout_PowerSchool_DataViz.setObjectName("actionAbout_PowerSchool_DataViz")
        self.actionNew_Window = QtWidgets.QAction(PowerSchool_DataViz)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/baseline-open_in_new-24px.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Window.setIcon(icon3)
        self.actionNew_Window.setObjectName("actionNew_Window")
        self.actionSave_Graph_As = QtWidgets.QAction(PowerSchool_DataViz)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/baseline-save_alt-24px.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Graph_As.setIcon(icon4)
        self.actionSave_Graph_As.setObjectName("actionSave_Graph_As")
        self.actionPrint = QtWidgets.QAction(PowerSchool_DataViz)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/baseline-print-24px.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon5)
        self.actionPrint.setObjectName("actionPrint")
        self.actionAbout_Qt = QtWidgets.QAction(PowerSchool_DataViz)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.File_Menu.addAction(self.actionNew_Window)
        self.File_Menu.addAction(self.actionOpen)
        self.File_Menu.addAction(self.actionSave_Graph_As)
        self.File_Menu.addAction(self.actionPrint)
        self.File_Menu.addSeparator()
        self.File_Menu.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout_PowerSchool_DataViz)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.File_Menu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(PowerSchool_DataViz)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PowerSchool_DataViz)

    def retranslateUi(self, PowerSchool_DataViz):
        _translate = QtCore.QCoreApplication.translate
        PowerSchool_DataViz.setWindowTitle(_translate("PowerSchool_DataViz", "PowerSchool DataViz"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Graph_Tab), _translate("PowerSchool_DataViz", "Graph"))
        self.Data_Table.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Data_Table_Tab), _translate("PowerSchool_DataViz", "Data"))
        self.File_Menu.setTitle(_translate("PowerSchool_DataViz", "File"))
        self.menuHelp.setTitle(_translate("PowerSchool_DataViz", "Help"))
        self.actionOpen.setText(_translate("PowerSchool_DataViz", "Open"))
        self.actionOpen.setShortcut(_translate("PowerSchool_DataViz", "Ctrl+O"))
        self.actionQuit.setText(_translate("PowerSchool_DataViz", "Quit"))
        self.actionQuit.setShortcut(_translate("PowerSchool_DataViz", "Ctrl+Q"))
        self.actionAbout_PowerSchool_DataViz.setText(_translate("PowerSchool_DataViz", "About PowerSchool DataViz"))
        self.actionNew_Window.setText(_translate("PowerSchool_DataViz", "New Window"))
        self.actionNew_Window.setShortcut(_translate("PowerSchool_DataViz", "Ctrl+N"))
        self.actionSave_Graph_As.setText(_translate("PowerSchool_DataViz", "Save Graph As..."))
        self.actionSave_Graph_As.setShortcut(_translate("PowerSchool_DataViz", "Ctrl+S"))
        self.actionPrint.setText(_translate("PowerSchool_DataViz", "Print"))
        self.actionPrint.setShortcut(_translate("PowerSchool_DataViz", "Ctrl+P"))
        self.actionAbout_Qt.setText(_translate("PowerSchool_DataViz", "About Qt"))

from PyQt5 import QtWebEngineWidgets
import PowerSchool_DataViz_Resources

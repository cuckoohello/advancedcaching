# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'files/qt/MainWindow.ui'
#
# Created: Mon Aug  2 12:41:45 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 392)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 21))
        self.menubar.setObjectName("menubar")
        self.menuMap = QtGui.QMenu(self.menubar)
        self.menuMap.setObjectName("menuMap")
        self.menuSearch = QtGui.QMenu(self.menubar)
        self.menuSearch.setObjectName("menuSearch")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout_AGTL = QtGui.QMenu(self.menuHelp)
        self.menuAbout_AGTL.setObjectName("menuAbout_AGTL")
        self.menuTest = QtGui.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.BottomToolBarArea), self.toolBar)
        self.actionHallo_Welt = QtGui.QAction(MainWindow)
        self.actionHallo_Welt.setObjectName("actionHallo_Welt")
        self.actionTsch_ss_Welt = QtGui.QAction(MainWindow)
        self.actionTsch_ss_Welt.setObjectName("actionTsch_ss_Welt")
        self.actionSelect_Map_Style = QtGui.QAction(MainWindow)
        self.actionSelect_Map_Style.setObjectName("actionSelect_Map_Style")
        self.actionGeocaches = QtGui.QAction(MainWindow)
        self.actionGeocaches.setObjectName("actionGeocaches")
        self.actionDownload_Map_Tiles = QtGui.QAction(MainWindow)
        self.actionDownload_Map_Tiles.setObjectName("actionDownload_Map_Tiles")
        self.actionBlub = QtGui.QAction(MainWindow)
        self.actionBlub.setCheckable(True)
        self.actionBlub.setObjectName("actionBlub")
        self.actionBla = QtGui.QAction(MainWindow)
        self.actionBla.setObjectName("actionBla")
        self.actionBlub_1 = QtGui.QAction(MainWindow)
        self.actionBlub_1.setCheckable(True)
        self.actionBlub_1.setObjectName("actionBlub_1")
        self.actionBlub_2 = QtGui.QAction(MainWindow)
        self.actionBlub_2.setCheckable(True)
        self.actionBlub_2.setObjectName("actionBlub_2")
        self.actionZoom_In = QtGui.QAction(MainWindow)
        self.actionZoom_In.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/advancedcaching/data/accept.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_In.setIcon(icon)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/advancedcaching/data/asterisk_yellow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_Out.setIcon(icon1)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionSearch_Place = QtGui.QAction(MainWindow)
        self.actionSearch_Place.setObjectName("actionSearch_Place")
        self.actionUpdate_Geocache_Map = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/advancedcaching/data/emoticon_grin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpdate_Geocache_Map.setIcon(icon2)
        self.actionUpdate_Geocache_Map.setObjectName("actionUpdate_Geocache_Map")
        self.actionDownload_Details_for_all_visible_Geocaches = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/advancedcaching/data/comment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDownload_Details_for_all_visible_Geocaches.setIcon(icon3)
        self.actionDownload_Details_for_all_visible_Geocaches.setObjectName("actionDownload_Details_for_all_visible_Geocaches")
        self.menuMap.addAction(self.actionSelect_Map_Style)
        self.menuMap.addAction(self.actionDownload_Map_Tiles)
        self.menuMap.addSeparator()
        self.menuMap.addAction(self.actionUpdate_Geocache_Map)
        self.menuMap.addAction(self.actionDownload_Details_for_all_visible_Geocaches)
        self.menuSearch.addAction(self.actionGeocaches)
        self.menuSearch.addAction(self.actionSearch_Place)
        self.menuAbout_AGTL.addAction(self.actionBlub_1)
        self.menuAbout_AGTL.addAction(self.actionBlub_2)
        self.menuHelp.addAction(self.menuAbout_AGTL.menuAction())
        self.menuTest.addAction(self.actionBlub)
        self.menuTest.addSeparator()
        self.menuTest.addAction(self.actionBla)
        self.menubar.addAction(self.menuMap.menuAction())
        self.menubar.addAction(self.menuSearch.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuTest.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoom_In)
        self.toolBar.addAction(self.actionZoom_Out)
        self.toolBar.addAction(self.actionUpdate_Geocache_Map)
        self.toolBar.addAction(self.actionDownload_Details_for_all_visible_Geocaches)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMap.setTitle(QtGui.QApplication.translate("MainWindow", "Map", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSearch.setTitle(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout_AGTL.setTitle(QtGui.QApplication.translate("MainWindow", "About &AGTL", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTest.setTitle(QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHallo_Welt.setText(QtGui.QApplication.translate("MainWindow", "Hallo Welt!", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTsch_ss_Welt.setText(QtGui.QApplication.translate("MainWindow", "Tschüss Welt!", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_Map_Style.setText(QtGui.QApplication.translate("MainWindow", "Select Map Style", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGeocaches.setText(QtGui.QApplication.translate("MainWindow", "Geocaches", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGeocaches.setStatusTip(QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownload_Map_Tiles.setText(QtGui.QApplication.translate("MainWindow", "Download Map Tiles", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBlub.setText(QtGui.QApplication.translate("MainWindow", "blub", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBla.setText(QtGui.QApplication.translate("MainWindow", "bla", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBlub_1.setText(QtGui.QApplication.translate("MainWindow", "Blub 1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBlub_2.setText(QtGui.QApplication.translate("MainWindow", "Blub 2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_In.setText(QtGui.QApplication.translate("MainWindow", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_In.setToolTip(QtGui.QApplication.translate("MainWindow", "Zooooom!", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_Out.setText(QtGui.QApplication.translate("MainWindow", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch_Place.setText(QtGui.QApplication.translate("MainWindow", "Search Place", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_Geocache_Map.setText(QtGui.QApplication.translate("MainWindow", "Update Geocache Locations", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownload_Details_for_all_visible_Geocaches.setText(QtGui.QApplication.translate("MainWindow", "Download Details for visible Geocaches", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc

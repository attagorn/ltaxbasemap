# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ltax_basemap_dockwidget_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LTaxBasemapDockWidgetBase(object):
    def setupUi(self, LTaxBasemapDockWidgetBase):
        LTaxBasemapDockWidgetBase.setObjectName("LTaxBasemapDockWidgetBase")
        LTaxBasemapDockWidgetBase.resize(298, 190)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(280, 150))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 46, 13))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 241, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setIconSize(QtCore.QSize(32, 32))
        self.comboBox.setObjectName("comboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/ltax_basemap/icons/osm2.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plugins/ltax_basemap/icons/terrain1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/plugins/ltax_basemap/icons/imagery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/plugins/ltax_basemap/icons/map11.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/plugins/ltax_basemap/icons/map7.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/plugins/ltax_basemap/icons/satellite2.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/plugins/ltax_basemap/icons/rtsd2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/plugins/ltax_basemap/icons/satellite.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/plugins/ltax_basemap/icons/ic_launcher.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon8, "")
        self.comboBox.addItem(icon8, "")
        self.comboBox.addItem(icon8, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/plugins/ltax_basemap/icons/spk_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon9, "")
        self.comboBox.addItem(icon9, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/plugins/ltax_basemap/icons/dhanarak.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon10, "")
        self.comboBox.addItem(icon10, "")
        self.comboBox.addItem(icon10, "")
        self.comboBox.addItem(icon10, "")
        self.btnLoad = QtWidgets.QPushButton(self.tab)
        self.btnLoad.setGeometry(QtCore.QRect(10, 70, 241, 31))
        self.btnLoad.setObjectName("btnLoad")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 251, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(70, 90, 131, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        LTaxBasemapDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(LTaxBasemapDockWidgetBase)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LTaxBasemapDockWidgetBase)

    def retranslateUi(self, LTaxBasemapDockWidgetBase):
        _translate = QtCore.QCoreApplication.translate
        LTaxBasemapDockWidgetBase.setWindowTitle(_translate("LTaxBasemapDockWidgetBase", "LTax BaseMap"))
        self.label.setText(_translate("LTaxBasemapDockWidgetBase", "Basemap :"))
        self.comboBox.setItemText(0, _translate("LTaxBasemapDockWidgetBase", "Open Street Map"))
        self.comboBox.setItemText(1, _translate("LTaxBasemapDockWidgetBase", "Google Terrian"))
        self.comboBox.setItemText(2, _translate("LTaxBasemapDockWidgetBase", "Google Satellite Map"))
        self.comboBox.setItemText(3, _translate("LTaxBasemapDockWidgetBase", "Google Hybrid Map"))
        self.comboBox.setItemText(4, _translate("LTaxBasemapDockWidgetBase", "ESRI Topo Map"))
        self.comboBox.setItemText(5, _translate("LTaxBasemapDockWidgetBase", "ESRI Satellite Map"))
        self.comboBox.setItemText(6, _translate("LTaxBasemapDockWidgetBase", "RTSD L7018S"))
        self.comboBox.setItemText(7, _translate("LTaxBasemapDockWidgetBase", "????????????????????????????????????????????? 2560-2562(GSD=2m.)"))
        self.comboBox.setItemText(8, _translate("LTaxBasemapDockWidgetBase", "??????????????????????????????????????? ???????????? (1)"))
        self.comboBox.setItemText(9, _translate("LTaxBasemapDockWidgetBase", "??????????????????????????????????????? ???????????? (2)"))
        self.comboBox.setItemText(10, _translate("LTaxBasemapDockWidgetBase", "??????????????????????????????????????? ???????????? (3)"))
        self.comboBox.setItemText(11, _translate("LTaxBasemapDockWidgetBase", "????????????????????? ???.???.???.4-01 (1)"))
        self.comboBox.setItemText(12, _translate("LTaxBasemapDockWidgetBase", "????????????????????? ???.???.???.4-01 (2)"))
        self.comboBox.setItemText(13, _translate("LTaxBasemapDockWidgetBase", "????????????????????? ???????????????????????? 1"))
        self.comboBox.setItemText(14, _translate("LTaxBasemapDockWidgetBase", "????????????????????? ???????????????????????? 2"))
        self.comboBox.setItemText(15, _translate("LTaxBasemapDockWidgetBase", "????????????????????? ??????????????????????????????"))
        self.comboBox.setItemText(16, _translate("LTaxBasemapDockWidgetBase", "????????????????????? ??????????????????????????????????????????"))
        self.btnLoad.setText(_translate("LTaxBasemapDockWidgetBase", "Load"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("LTaxBasemapDockWidgetBase", "Basemap"))
        self.label_2.setText(_translate("LTaxBasemapDockWidgetBase", "<html><head/><body><p>LTax BaseMap</p></body></html>"))
        self.label_3.setText(_translate("LTaxBasemapDockWidgetBase", "by Attagorn Srinarong (TongzGIS)"))
        self.label_4.setText(_translate("LTaxBasemapDockWidgetBase", "Line ID: attagorn"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("LTaxBasemapDockWidgetBase", "About"))

from .resources import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LTaxBasemapDockWidgetBase = QtWidgets.QDockWidget()
    ui = Ui_LTaxBasemapDockWidgetBase()
    ui.setupUi(LTaxBasemapDockWidgetBase)
    LTaxBasemapDockWidgetBase.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(971, 658)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(28, 0))

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignLeft)

        self.hostSelectorBox = QComboBox(self.centralwidget)
        self.hostSelectorBox.addItem("")
        self.hostSelectorBox.setObjectName(u"hostSelectorBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.hostSelectorBox.sizePolicy().hasHeightForWidth())
        self.hostSelectorBox.setSizePolicy(sizePolicy2)
        self.hostSelectorBox.setEditable(True)

        self.horizontalLayout.addWidget(self.hostSelectorBox)

        self.refreshBtn = QPushButton(self.centralwidget)
        self.refreshBtn.setObjectName(u"refreshBtn")
        icon = QIcon()
        iconThemeName = u"view-refresh"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../.designer/.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        self.refreshBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.refreshBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.containerTab = QWidget()
        self.containerTab.setObjectName(u"containerTab")
        self.verticalLayout_3 = QVBoxLayout(self.containerTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.containerTab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.containerTab)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.widget = QWidget(self.containerTab)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_10 = QHBoxLayout(self.widget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.createContainerBtn = QPushButton(self.widget)
        self.createContainerBtn.setObjectName(u"createContainerBtn")
        icon1 = QIcon()
        iconThemeName = u"document-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"../.designer/.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        self.createContainerBtn.setIcon(icon1)

        self.horizontalLayout_10.addWidget(self.createContainerBtn)

        self.startContainerBtn = QPushButton(self.widget)
        self.startContainerBtn.setObjectName(u"startContainerBtn")
        self.startContainerBtn.setEnabled(False)
        icon2 = QIcon()
        iconThemeName = u"media-playback-start"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"../.designer/.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        self.startContainerBtn.setIcon(icon2)
        self.startContainerBtn.setFlat(False)

        self.horizontalLayout_10.addWidget(self.startContainerBtn)

        self.stopContainerBtn = QPushButton(self.widget)
        self.stopContainerBtn.setObjectName(u"stopContainerBtn")
        self.stopContainerBtn.setEnabled(False)
        icon3 = QIcon()
        iconThemeName = u"media-playback-stop"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u"../.designer/.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        self.stopContainerBtn.setIcon(icon3)
        self.stopContainerBtn.setFlat(False)

        self.horizontalLayout_10.addWidget(self.stopContainerBtn)

        self.commitContainerBtn = QPushButton(self.widget)
        self.commitContainerBtn.setObjectName(u"commitContainerBtn")
        self.commitContainerBtn.setEnabled(False)
        icon4 = QIcon()
        iconThemeName = u"document-save-as"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u"../.designer/.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        self.commitContainerBtn.setIcon(icon4)
        self.commitContainerBtn.setFlat(False)

        self.horizontalLayout_10.addWidget(self.commitContainerBtn)

        self.deleteContainerBtn = QPushButton(self.widget)
        self.deleteContainerBtn.setObjectName(u"deleteContainerBtn")
        self.deleteContainerBtn.setEnabled(False)
        icon5 = QIcon()
        iconThemeName = u"edit-delete"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u"../.designer/.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        self.deleteContainerBtn.setIcon(icon5)
        self.deleteContainerBtn.setFlat(False)

        self.horizontalLayout_10.addWidget(self.deleteContainerBtn)

        self.terminalBtn = QPushButton(self.widget)
        self.terminalBtn.setObjectName(u"terminalBtn")
        self.terminalBtn.setEnabled(False)
        icon6 = QIcon()
        iconThemeName = u"utilities-terminal"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile(u"../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        self.terminalBtn.setIcon(icon6)

        self.horizontalLayout_10.addWidget(self.terminalBtn)

        self.infoContainerBtn = QPushButton(self.widget)
        self.infoContainerBtn.setObjectName(u"infoContainerBtn")
        self.infoContainerBtn.setEnabled(False)
        icon7 = QIcon(QIcon.fromTheme(u"dialog-information"))
        self.infoContainerBtn.setIcon(icon7)

        self.horizontalLayout_10.addWidget(self.infoContainerBtn)


        self.verticalLayout_2.addWidget(self.widget)

        self.containerTableCtn = QTableWidget(self.containerTab)
        if (self.containerTableCtn.columnCount() < 5):
            self.containerTableCtn.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.containerTableCtn.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.containerTableCtn.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.containerTableCtn.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.containerTableCtn.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.containerTableCtn.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.containerTableCtn.setObjectName(u"containerTableCtn")
        self.containerTableCtn.setSelectionMode(QAbstractItemView.SingleSelection)
        self.containerTableCtn.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.containerTableCtn.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.containerTableCtn)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.containerTab, "")
        self.imageTab = QWidget()
        self.imageTab.setObjectName(u"imageTab")
        self.verticalLayout_5 = QVBoxLayout(self.imageTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.imageTab)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.imageTab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.widget_2 = QWidget(self.imageTab)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_8.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_8.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_8.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_8.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_8.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_8.addWidget(self.pushButton_6)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.imageTableCtn = QTableWidget(self.imageTab)
        if (self.imageTableCtn.columnCount() < 2):
            self.imageTableCtn.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.imageTableCtn.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.imageTableCtn.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.imageTableCtn.setObjectName(u"imageTableCtn")
        self.imageTableCtn.setSelectionMode(QAbstractItemView.SingleSelection)
        self.imageTableCtn.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_4.addWidget(self.imageTableCtn)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.imageTab, "")
        self.volumeTab = QWidget()
        self.volumeTab.setObjectName(u"volumeTab")
        self.verticalLayout_7 = QVBoxLayout(self.volumeTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.volumeTab)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.volumeTab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_4.addWidget(self.lineEdit_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.volumeTableCtn = QTableWidget(self.volumeTab)
        self.volumeTableCtn.setObjectName(u"volumeTableCtn")

        self.verticalLayout_6.addWidget(self.volumeTableCtn)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.volumeTab, "")
        self.networkTab = QWidget()
        self.networkTab.setObjectName(u"networkTab")
        self.verticalLayout_9 = QVBoxLayout(self.networkTab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.createNetworkBtn = QPushButton(self.networkTab)
        self.createNetworkBtn.setObjectName(u"createNetworkBtn")
        icon8 = QIcon()
        iconThemeName = u"document-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon8 = QIcon.fromTheme(iconThemeName)
        else:
            icon8.addFile(u"../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        self.createNetworkBtn.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.createNetworkBtn)

        self.removeNetworkBtn = QPushButton(self.networkTab)
        self.removeNetworkBtn.setObjectName(u"removeNetworkBtn")
        icon9 = QIcon()
        iconThemeName = u"edit-delete"
        if QIcon.hasThemeIcon(iconThemeName):
            icon9 = QIcon.fromTheme(iconThemeName)
        else:
            icon9.addFile(u"../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        self.removeNetworkBtn.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.removeNetworkBtn)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.networkTableCtn = QTableWidget(self.networkTab)
        if (self.networkTableCtn.columnCount() < 4):
            self.networkTableCtn.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.networkTableCtn.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.networkTableCtn.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.networkTableCtn.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.networkTableCtn.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.networkTableCtn.setObjectName(u"networkTableCtn")
        self.networkTableCtn.setSelectionMode(QAbstractItemView.SingleSelection)
        self.networkTableCtn.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_8.addWidget(self.networkTableCtn)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.tabWidget.addTab(self.networkTab, "")
        self.infoTab = QWidget()
        self.infoTab.setObjectName(u"infoTab")
        self.tabWidget.addTab(self.infoTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 971, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences...", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.hostSelectorBox.setItemText(0, "")

        self.refreshBtn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.createContainerBtn.setText(QCoreApplication.translate("MainWindow", u"Create...", None))
        self.startContainerBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stopContainerBtn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.commitContainerBtn.setText(QCoreApplication.translate("MainWindow", u"Commit...", None))
        self.deleteContainerBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.terminalBtn.setText(QCoreApplication.translate("MainWindow", u"Open Terminal", None))
        self.infoContainerBtn.setText(QCoreApplication.translate("MainWindow", u"Info...", None))
        ___qtablewidgetitem = self.containerTableCtn.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.containerTableCtn.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Image", None));
        ___qtablewidgetitem2 = self.containerTableCtn.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Created", None));
        ___qtablewidgetitem3 = self.containerTableCtn.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem4 = self.containerTableCtn.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.containerTab), QCoreApplication.translate("MainWindow", u"Containers", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Inspect...", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Pull...", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Push...", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Load...", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Save...", None))
        ___qtablewidgetitem5 = self.imageTableCtn.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem6 = self.imageTableCtn.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Size", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imageTab), QCoreApplication.translate("MainWindow", u"Images", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.volumeTab), QCoreApplication.translate("MainWindow", u"Volumes", None))
        self.createNetworkBtn.setText(QCoreApplication.translate("MainWindow", u"Create...", None))
        self.removeNetworkBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        ___qtablewidgetitem7 = self.networkTableCtn.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem8 = self.networkTableCtn.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Driver", None));
        ___qtablewidgetitem9 = self.networkTableCtn.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Scope", None));
        ___qtablewidgetitem10 = self.networkTableCtn.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.networkTab), QCoreApplication.translate("MainWindow", u"Networks", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.infoTab), QCoreApplication.translate("MainWindow", u"Sys. Info", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


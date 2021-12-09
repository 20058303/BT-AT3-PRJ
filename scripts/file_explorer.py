# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FileExplorerFuWQcp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from scripts import about_dialog


class Ui_FileExplorer(object):
    def setupUi(self, FileExplorer):
        if not FileExplorer.objectName():
            FileExplorer.setObjectName(u"FileExplorer")
        FileExplorer.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"./UI Files/bino-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        FileExplorer.setWindowIcon(icon)
        self.actionDarkTheme = QAction(FileExplorer)
        self.actionDarkTheme.setObjectName(u"actionDarkTheme")
        self.actionDarkTheme.setCheckable(True)
        self.actionAbout = QAction(FileExplorer)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(FileExplorer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addressLineEdit = QLineEdit(self.centralwidget)
        self.addressLineEdit.setObjectName(u"addressLineEdit")

        self.horizontalLayout.addWidget(self.addressLineEdit)

        self.gotoPushButton = QPushButton(self.centralwidget)
        self.gotoPushButton.setObjectName(u"gotoPushButton")

        self.horizontalLayout.addWidget(self.gotoPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.directoryTreeView = QTreeView(self.centralwidget)
        self.directoryTreeView.setObjectName(u"directoryTreeView")
        self.directoryTreeView.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.directoryTreeView)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        FileExplorer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FileExplorer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu_Theme = QMenu(self.menubar)
        self.menu_Theme.setObjectName(u"menu_Theme")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        FileExplorer.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(FileExplorer)
        self.statusBar.setObjectName(u"statusBar")
        FileExplorer.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(FileExplorer)
        self.toolBar.setObjectName(u"toolBar")
        FileExplorer.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_Theme.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menu_Theme.addAction(self.actionDarkTheme)
        self.menuHelp.addAction(self.actionAbout)

        self.toolBar.addAction(self.actionDarkTheme)
        self.toolBar.addAction(self.actionAbout)

        self.retranslateUi(FileExplorer)
        self.directoryTreeView.collapsed.connect(FileExplorer.refreshTreeView)
        self.directoryTreeView.expanded.connect(FileExplorer.refreshTreeView)
        self.directoryTreeView.clicked.connect(FileExplorer.directoryTreeView.expand)
        self.directoryTreeView.doubleClicked.connect(FileExplorer.openFile)
        self.gotoPushButton.clicked.connect(FileExplorer.gotoDirectory)
        self.actionDarkTheme.toggled.connect(FileExplorer.toggleTheme)
        self.actionAbout.triggered.connect(FileExplorer.openAbout)

        QMetaObject.connectSlotsByName(FileExplorer)
    # setupUi

    def initalizeDirectory(self):
        """Sets up the QTreeView widget to display the computer's main directory"""
        self.model.setRootPath(QDir.rootPath())
        self.directoryTreeView.setModel(self.model)
        self.directoryTreeView.setRootIndex(self.model.index(''))
        self.directoryTreeView.setSortingEnabled(True)
        self.directoryTreeView.resizeColumnToContents(0)

    def refreshTreeView(self, index):
        """Resizes the QTreeView columns and updates the navigational text display"""
        self.directoryTreeView.resizeColumnToContents(0)
        indexItem = self.model.index(index.row(), 0, index.parent())
        filePath = self.model.filePath(indexItem)
        self.addressLineEdit.setText(filePath)

    def gotoDirectory(self):
        """Navigates to a directory input through the address bar if it exists"""
        path = str(self.addressLineEdit.text())
        self.directoryTreeView.setCurrentIndex(self.model.index(path))
        self.refreshTreeView(self.model.index(path))

    def openAbout(self):
        """Opens the About Dialog window"""
        aboutDialog = AboutDialog()
        aboutDialog.exec_()

    def retranslateUi(self, FileExplorer):
        FileExplorer.setWindowTitle(QCoreApplication.translate("FileExplorer", u"File Browser", None))
        self.actionDarkTheme.setText(QCoreApplication.translate("FileExplorer", u"Dark Theme", None))
        self.actionAbout.setText(QCoreApplication.translate("FileExplorer", u"About", None))
        self.gotoPushButton.setText(QCoreApplication.translate("FileExplorer", u"Go", None))
        self.menu_Theme.setTitle(QCoreApplication.translate("FileExplorer", u"&Theme", None))
        self.menuHelp.setTitle(QCoreApplication.translate("FileExplorer", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("FileExplorer", u"toolBar", None))
    # retranslateUi


class AboutDialog(about_dialog.Ui_AboutDialog, QDialog):
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.setupUi(self)



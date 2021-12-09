# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageViewerNVUCkD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_ImageViewer(object):
    def setupUi(self, ImageViewer, image):
        if not ImageViewer.objectName():
            ImageViewer.setObjectName(u"ImageViewer")
        ImageViewer.resize(600, 480)
        ImageViewer.setModal(False)
        ImageViewer.setWindowTitle(image)

        self.gridLayout = QGridLayout(ImageViewer)
        self.gridLayout.setObjectName(u"gridLayout")

        pixmap = QPixmap(image)
        self.imageLabel = QLabel(ImageViewer)
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setPixmap(pixmap.scaled(QSize(1280, 720), Qt.KeepAspectRatio))

        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMaximumSize(QSize(1280, 720))
        self.imageLabel.setFrameShape(QFrame.StyledPanel)


        self.gridLayout.addWidget(self.imageLabel, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(428, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonBox = QDialogButtonBox(ImageViewer)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(ImageViewer)
        self.buttonBox.rejected.connect(ImageViewer.reject)
        self.buttonBox.accepted.connect(ImageViewer.accept)

        QMetaObject.connectSlotsByName(ImageViewer)
    # setupUi

    def retranslateUi(self, ImageViewer):
        ImageViewer.setWindowTitle(QCoreApplication.translate("ImageViewer", u"Image Viewer", None))
    # retranslateUi


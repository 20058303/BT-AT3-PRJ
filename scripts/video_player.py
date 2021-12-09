# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoPlayernhKylX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class Ui_VideoPlayer(object):
    def setupUi(self, VideoPlayer, video):
        if not VideoPlayer.objectName():
            VideoPlayer.setObjectName(u"VideoPlayer")
        VideoPlayer.resize(640, 480)
        VideoPlayer.setMinimumSize(QSize(640, 480))
        self.gridLayout = QGridLayout(VideoPlayer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.videoWidget = QVideoWidget(VideoPlayer)
        self.videoWidget.setObjectName(u"videoWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoWidget.sizePolicy().hasHeightForWidth())
        self.videoWidget.setSizePolicy(sizePolicy)
        self.videoWidget.setMaximumSize(QSize(1920, 1080))
        self.videoWidget.setSizeIncrement(QSize(16, 9))

        self.videoPlayer = QMediaPlayer(None, QMediaPlayer.Surface)
        self.videoPlayer.setVideoOutput(self.videoWidget)

        media = QMediaContent(QUrl.fromLocalFile(video))
        self.videoPlayer.setMedia(media)

        self.gridLayout.addWidget(self.videoWidget, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(265, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.playButton = QPushButton(VideoPlayer)
        self.playButton.setObjectName(u"playButton")

        self.gridLayout.addWidget(self.playButton, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(264, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.retranslateUi(VideoPlayer)
        self.playButton.clicked.connect(self.playPause)

        QMetaObject.connectSlotsByName(VideoPlayer)
    # setupUi

    def playPause(self):
        """Plays and pauses the currently playing media"""
        if self.videoPlayer.state() == QMediaPlayer.PlayingState:
            self.videoPlayer.pause()
            self.playButton.setText('Play')
        else:
            self.videoPlayer.play()
            self.playButton.setText('Pause')

    def retranslateUi(self, VideoPlayer):
        VideoPlayer.setWindowTitle(QCoreApplication.translate("VideoPlayer", u"Video Player", None))
        self.playButton.setText(QCoreApplication.translate("VideoPlayer", u"Play", None))
    # retranslateUi


import os

from PyQt5 import QtWidgets
from scripts import file_explorer, image_viewer, video_player, about_dialog
import qdarkstyle


class FileExplorer(file_explorer.Ui_FileExplorer, QtWidgets.QMainWindow):
    def __init__(self):
        super(FileExplorer, self).__init__()
        self.setupUi(self)
        self.model = QtWidgets.QFileSystemModel()
        self.initalizeDirectory()

    def openFile(self):
        """Opens a supported file with internal viewer, otherwise opens through external application"""
        index = self.directoryTreeView.currentIndex()
        file = self.model.filePath(self.model.index(index.row(), 0, index.parent()))

        if file.endswith(('.jpg', '.png', '.jpeg', '.gif')):
            self.statusBar.showMessage(f"Opening {file} with internal image viewer.", 5000)
            imager = ImageViewer(file)
            imager.exec_()
        elif file.endswith('.avi'):
            self.statusBar.showMessage(f"Opening {file} with internal video player.", 5000)
            player = VideoPlayer(file)
            player.exec_()
        else:
            self.statusBar.showMessage(f"Opening {file} with external application.", 5000)
            os.startfile(file)

    def toggleTheme(self):
        """Switches between light and dark themes for the app as a whole"""
        if self.actionDarkTheme.isChecked():
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
            self.statusBar.showMessage("Theme changed to 'Dark Theme'", 5000)
        else:
            app.setStyleSheet("")
            self.statusBar.showMessage("Theme changed to 'Light Theme'", 5000)


class ImageViewer(image_viewer.Ui_ImageViewer, QtWidgets.QDialog):
    def __init__(self, image):
        super(ImageViewer, self).__init__()
        self.setupUi(self, image)


class VideoPlayer(video_player.Ui_VideoPlayer, QtWidgets.QDialog):
    def __init__(self, video):
        super(VideoPlayer, self).__init__()
        self.setupUi(self, video)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    fe = FileExplorer()
    fe.show()
    app.exec_()

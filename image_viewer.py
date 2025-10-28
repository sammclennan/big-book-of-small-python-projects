# A very basic PySide6 image viewer

import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget
)
from PySide6.QtGui import QAction, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        minWidth, minHeight = 400, 300
        openWidth, openHeight = 800, 600
        self.setWindowTitle("Image Viewer")
        self.setMinimumSize(minWidth, minHeight)

        # Layouts
        mainLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()

        # Image container
        self.imageContainer = QLabel()
        self.imageContainer.setAlignment(Qt.AlignCenter)
        self.imageContainer.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.pixmap = None
        mainLayout.addWidget(self.imageContainer)

        # Control buttons
        self.prevButton = QPushButton("Previous Image")
        self.prevButton.clicked.connect(lambda: self.changeImage(forward=False))
        self.prevButton.setEnabled(False)
        buttonLayout.addWidget(self.prevButton)
        self.nextButton = QPushButton("Next Image")
        self.nextButton.clicked.connect(lambda: self.changeImage(forward=True))
        self.nextButton.setEnabled(False)
        buttonLayout.addWidget(self.nextButton)
        mainLayout.addLayout(buttonLayout)

        # Actions
        openFileAction = QAction("Open File", self)
        openFileAction.triggered.connect(self.openFile)
        openFolderAction = QAction("Open Folder", self)
        openFolderAction.triggered.connect(self.openFolder)
        
        # Menu
        menu = self.menuBar()
        fileMenu = menu.addMenu("File")
        fileMenu.addAction(openFileAction)
        fileMenu.addAction(openFolderAction)

        # Central widget
        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

        self.resize(openWidth, openHeight)

        self.filesList = []
        self.fileIndex = 0

    
    def resizeEvent(self, event):
        """Overrides resizeEvent to rescale image when window is resized."""
        if self.pixmap:
            imgSize = self.pixmap.size()
            holderSize = self.imageContainer.size()

            pixmap = self.pixmap.scaled(
                min(holderSize.width(), imgSize.width()),
                min(holderSize.height(), imgSize.height()),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            self.imageContainer.setPixmap(pixmap)

        super().resizeEvent(event)

    
    def setImage(self):
        """Sets image container to display current image file or clears image if no files selected."""
        if self.filesList:
            imgFile = self.filesList[self.fileIndex]
            pixmap = QPixmap(imgFile)

            if pixmap.isNull():
                self.imageContainer.setText(f"Failed to load {imgFile}")
                return
            else:
                self.pixmap = pixmap
                self.imageContainer.setPixmap(self.pixmap)
                self.resizeEvent(None)

        else:
            self.pixmap = None
            self.imageContainer.clear()


    def changeImage(self, forward=True):
        """Switches image file to next or previous in list."""
        if len(self.filesList) > 1:
            if forward:
                self.fileIndex += 1
            else:
                self.fileIndex -= 1

            self.fileIndex %= len(self.filesList)
            self.setImage()
            
    
    def openFile(self):
        """Open file dialog."""
        filenames, _ = QFileDialog.getOpenFileNames(
            self,
            "Open Image",
            "",
            "Image Files (*.png *.jpg *.bmp)",
        )
        if filenames:
            self.filesList = filenames
            self.fileIndex = 0
            self.setButtons(self.filesList)
            self.setImage()


    def openFolder(self):
        """Open directory dialog."""
        extensions = (".jpg", ".png", ".bmp")
        directory = QFileDialog.getExistingDirectory(
            self,
            "Open Directory"
            )
        if directory:
            self.filesList = [os.path.join(directory, file) for file in os.listdir(directory) if file.lower().endswith(extensions)]
            self.fileIndex = 0
            self.setButtons(self.filesList)
            self.setImage()

    
    def setButtons(self, filesList):
        """Enable control buttons if there are multiple images to display."""
        enabled = len(filesList) > 1
        self.prevButton.setEnabled(enabled)
        self.nextButton.setEnabled(enabled)
     

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
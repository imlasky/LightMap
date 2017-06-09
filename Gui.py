'''
    Class: COP4331C (Summer 2017)
    Group: G13
    Graphical User Interface for LightMap
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

#Leverage an object-oriented approach to create the GUI.
class MainWindow(QMainWindow):
    #Load the GUI.
    def __init__(self):
        super().__init__()

        #Define the application.
        self.title = "LightMap"
        self.windowIcon = QIcon("LightMap.png")
        
        #Define the dimensions of the main GUI window.
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480

        self.initUI()
    
    #Fill the GUI.
    def initUI(self):
        #Set the title, window icon, and dimensions of the main window.
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.windowIcon)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Create the menu.
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        viewMenu = mainMenu.addMenu("View")
        settingsMenu = mainMenu.addMenu("Settings")
        helpMenu = mainMenu.addMenu("Help")

        #Display the name of the application.
        appNameLabel = QLabel(self)
        appNameLabel.move(120, 25)
        appNameLogo = QPixmap("LightMap.png")
        appNameLabel.setPixmap(appNameLogo)
        appNameLabel.resize(396, 141)

        #Add an open image option.
        openImageOption = QAction("Open Image", self)
        openImageOption.setShortcut("CTRL+O")
        openImageOption.setStatusTip("Open image")
        openImageOption.triggered.connect(self.openFile)
        fileMenu.addAction(openImageOption)

        #Add an exit option.
        exitOption = QAction("Exit", self)
        exitOption.setShortcut("CTRL+Q")
        exitOption.setStatusTip("Exit application")
        exitOption.triggered.connect(self.close)
        fileMenu.addAction(exitOption)

        #Add a setting to configure hardware positions.
        configPositionsOption = QAction("Configure Hardware Positions", self)
        settingsMenu.addAction(configPositionsOption)

        #Add a button to open an image file.
        openImageButt = QPushButton("Open Image", self)
        openImageButt.move(250, 200)
        fileChosen = openImageButt.clicked.connect(self.openFile)

        #Display the directory path of the file chosen.
        fileName = "No File Selected"
        labelFileName = QLabel(fileName, self)
        labelFileName.move(265, 250)

        #Tell the user to start the program.
        textStartMapping = "Once you have selected an image, start mapping!"
        labelStartMapping = QLabel(textStartMapping, self)
        labelStartMapping.move(200, 300)
        labelStartMapping.resize(350, 20)

        #Add a button to start the main program to map the chosen image onto a ball.
        mapImageButt = QPushButton("Start Mapping", self)
        mapImageButt.move(250, 350)

        #Show the main window.
        self.show()

    #Open an image file.
    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileChosen, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
            "JPEG (*.JPEG *.jpeg *.JPG *.jpg *.JPE *.jpe *JFIF *.jfif);; PNG (*.PNG *.png)", options=options)
        print(self.fileChosen)

    #Return the image file name to the back end.
    def returnFile(self):
        #Check if the user has selected an image before sending the file path to the main program.
        if not self.fileChosen:
            QMessagebox.showinfo(self, "No File Selected", "Please select a valid image file before mapping!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

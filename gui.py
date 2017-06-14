'''
    Class: COP4331C (Summer 2017)
    Group: G13
    Graphical User Interface for LightMap
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

#Leverage an object-oriented approach to create the GUI.
class LightMap(QMainWindow):
    #Load the GUI.
    def __init__(self):
        super().__init__()

        self.window_icon = QIcon("LightMap.png")

        self.init_ui()
    
    #Fill the GUI.
    def init_ui(self):
        #Set the window icon.
        self.setWindowIcon(self.window_icon)

        uic.loadUi("mainwindow.ui", self)

        #Show the main window.
        self.show()


    #Cascade options for the File menu.
    def cascade_file_menu(self, file_menu):
        #Add an open image option.
        open_image_option = QAction("Open Image", self)
        open_image_option.setShortcut("CTRL+O")
        open_image_option.setStatusTip("Open image")
        open_image_option.triggered.connect(self.open_file)
        file_menu.addAction(open_image_option)

        #Add an exit option.
        exit_option = QAction("Exit", self)
        exit_option.setShortcut("CTRL+Q")
        exit_option.setStatusTip("Exit application")
        exit_option.triggered.connect(self.close)
        file_menu.addAction(exit_option)

    def cascade_view_menu(self, view_menu):
        pass

    def cascade_settings_menu(self, settings_menu):
        pass

    def cascade_help_menu(self, help_menu):
        pass

    #Open an image file.
    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.file_chosen, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
            "JPEG (*.JPEG *.jpeg *.JPG *.jpg *.JPE *.jpe *JFIF *.jfif);; PNG (*.PNG *.png)", options=options)
        print(self.fileChosen)

    #Return the image file name to the back end.
    def return_file(self):
        #Check if the user has selected an image before sending the file path to the main program.
        if not self.file_chosen:
            QMessagebox.showinfo(self, "No File Selected", "Please select a valid image file before mapping!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LightMap()
    sys.exit(app.exec_())

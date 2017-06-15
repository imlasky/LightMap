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

        #Set the window icon.
        self.window_icon = QIcon("LightMap.png")

        self.init_ui()
    
    #Fill the GUI.
    def init_ui(self):
        #Set the window icon.
        self.setWindowIcon(self.window_icon)

        #Load the UI file.
        main_window = uic.loadUi("mainwindow.ui", self)

        #Add commands for actions under the submenus.
        self.command_file_menu(main_window)
        self.command_settings_menu(main_window)
        self.command_help_menu(main_window)

        #

        #Show the main window.
        self.show()

    #Add commands for actions under the File menu.
    def command_file_menu(self, main_window):
        #Back-end logic for Open Image.
        main_window.action_open_image.setShortcut("CTRL+O")
        main_window.action_open_image.setStatusTip("Open Image")
        main_window.action_open_image.triggered.connect(self.open_file)

        #Back-end logic for Record Video.
        main_window.action_record_video.setShortcut("CTRL+R")
        main_window.action_record_video.setStatusTip("Record Video")

        #Back-end logic for Quit.
        main_window.action_quit.setShortcut("CTRL+Q")
        main_window.action_quit.setStatusTip("Quit")
        main_window.action_quit.triggered.connect(self.close)

    #Add commands for actions under the Settings menu.
    def command_settings_menu(self, main_window):
        #Back-end logic for Preferences.
        main_window.action_preferences.setShortcut("CTRL+P")
        main_window.action_preferences.setStatusTip("Preferences")

    #Add commands for actions sunder the Help menu.
    def command_help_menu(self, main_window):
        #Back-end logic for LightMap Help.
        main_window.action_LightMap_Help.setShortcut("CTRL+H")
        main_window.action_LightMap_Help.setStatusTip("LightMap Help")

        #Back-end logic for About LightMap.
        main_window.action_About_LightMap.setStatusTip("About LightMap")

    #Open an image file.
    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.file_chosen, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
            "Bitmap Files (*.BMP *.bmp *.DIB *.dib);; JPEG (*.JPEG *.jpeg *.JPG *.jpg *.JPE *.jpe *JFIF *.jfif);; PNG (*.PNG *.png);; GIF (*.GIF *.gif);; TIFF (*.TIF *.tif *.TIFF *.tiff);; ICO (*.ICO *.ico)", options=options)
        print(self.file_chosen)

    #Return the image file name to the back end.
    def return_file(self):
        #Check if the user has selected an image before sending the file path to the main program.
        if not self.file_chosen:
            QMessagebox.showinfo(self, "No File Selected", "Please select a valid image file before mapping!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LightMap()
    sys.exit(app.exec_())

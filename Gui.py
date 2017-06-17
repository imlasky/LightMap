'''
    Class: COP4331C (Summer 2017)
    Group: G13
    Graphical User Interface for LightMap
'''

#Standard imports.
import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *

#Leverage an object-oriented approach to create the GUI.
class GUI(QMainWindow):
    #Load the GUI.
    def __init__(self):
        super().__init__()

        #Define the window icon.
        self.window_icon = QIcon("LightMap.png")

        #Make the UI.
        self.init_ui()
    
    #Fill the GUI.
    def init_ui(self):
        #Load the UI file.
        main_window = uic.loadUi("mainwindow.ui", self)

        #Set the window icon.
        self.setWindowIcon(self.window_icon)

        #Add commands for actions under the submenus.
        self.command_file_menu(main_window)
        self.command_settings_menu(main_window)
        self.command_help_menu(main_window)

        #Handle the case that the user clicks on the "Open Image" button.
        main_window.button_open_image.setStatusTip("Open Image")
        main_window.button_open_image.clicked.connect(lambda: self.open_file(main_window))

        #Make sure this variable has been declared so that we can click "Start Mapping" at any time.
        self.file_chosen = None

        #Handle the case that the user clicks on the "Start Mapping" button.
        main_window.button_start_mapping.setStatusTip("Start Mapping")
        main_window.button_start_mapping.clicked.connect(self.start_mapping)

        #Show the main window.
        self.show()

    def start_mapping(self):
        #Check if the user has selected an image before sending the file path to the main program.
        if not self.file_chosen:
            QMessageBox.about(self, "No File Selected", "Please select a valid image file before mapping!")
        else:
            return self.file_chosen

    #Add commands for actions under the File menu.
    def command_file_menu(self, main_window):
        #Back-end logic for Open Image.
        main_window.action_open_image.setShortcut("CTRL+O")
        main_window.action_open_image.setStatusTip("Open Image")
        main_window.action_open_image.triggered.connect(lambda: self.open_file(main_window))

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
    def open_file(self, main_window):
        #Open the file dialog to select an image file.
        self.file_chosen, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
            "JPEG (*.JPEG *.jpeg *.JPG *.jpg *.JPE *.jpe *JFIF *.jfif);; PNG (*.PNG *.png);; GIF (*.GIF *.gif);; Bitmap Files (*.BMP *.bmp *.DIB *.dib);; TIFF (*.TIF *.tif *.TIFF *.tiff);; ICO (*.ICO *.ico)")
        
        #Show the path of the file chosen.
        if self.file_chosen:
            main_window.label_file_name.setText(self.file_chosen)
        else:
            main_window.label_file_name.setText("No image was selected. Please select an image.")

#DEBUG: DELETE LATER
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())

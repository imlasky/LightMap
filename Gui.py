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

        #Set status tips for all clickable widgets from the main window except for the menu.
        self.display_status(main_window)

        #Add commands for actions under the submenus.
        self.command_file_menu(main_window)
        self.command_settings_menu(main_window)
        self.command_help_menu(main_window)

        #Handle the case that the user clicks on the "Open Image" button.
        main_window.button_open_image.clicked.connect(lambda: self.open_file(main_window))

        #Make sure this variable has been declared so that we can click on "Start Mapping" at any time.
        self.file_chosen = None

        #Handle the case that the user clicks on the "Start Mapping" button.
        main_window.button_start_mapping.clicked.connect(lambda: self.start_mapping(main_window))

        #Show the main window.
        self.show()

    def start_mapping(self, main_window):
        #Check if the user has selected an image before sending the file path to the main program.
        if not self.file_chosen:
            QMessageBox.about(self, "No File Selected", "Please select a valid image file before mapping!")

        #Check if the user has entered valid input for the hardware position specifications.
        elif main_window.double_spin_box_projector_height.value() == 0:
            QMessageBox.about(self, "Invalid Projector Height", "Please enter a number greater than 0 for the height of the projector.")

        elif main_window.double_spin_box_projector_to_screen.value() == 0:
            QMessageBox.about(self, "Invalid Projector to Screen Distance", "Please enter a number greater than 0 for the distance from the projector to the screen.")

        elif main_window.double_spin_box_camera_height.value() == 0:
            QMessageBox.about(self, "Invalid Camera Height", "Please enter a number greater than 0 for the height of the camera.")

        elif main_window.double_spin_box_camera_to_screen.value() == 0:
            QMessageBox.about(self, "Invalid Camera Height", "Please enter a number greater than 0 for the distance from the camera to the screen.")

        #Everything is good to go! Send the data to the rest of the program.
        else:
            #Index 0 stores the projector's height. Index 1 stores the distance from the projector to the screen.
            #Index 2 stores the camera's height. Index 3 stores the distance from the camera to the screen.
            hardware_positions = [None] * 4

            #Convert the user input for hardware distance measurements to meters.
            hardware_positions[0] = self.convert_to_meters(main_window.double_spin_box_projector_height.value(), main_window.combo_box_projector_height.currentIndex())
            hardware_positions[1] = self.convert_to_meters(main_window.double_spin_box_projector_to_screen.value(), main_window.combo_box_projector_to_screen.currentIndex())
            hardware_positions[2] = self.convert_to_meters(main_window.double_spin_box_camera_height.value(), main_window.combo_box_camera_height.currentIndex())
            hardware_positions[3] = self.convert_to_meters(main_window.double_spin_box_camera_to_screen.value(), main_window.combo_box_camera_to_screen.currentIndex())

            #Pass the array containing the hardware distance measurements.
            print(hardware_positions)

            #Pass the file path of the image chosen.
            print(self.file_chosen)

            #If the user has chosen to record a video, call the video recording function.
            if main_window.check_box_record_video.isChecked() is True:
                print("Record Video")


    #Open an image file.
    def open_file(self, main_window):
        #Open the file dialog to select an image file.
        self.file_chosen, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
            "JPEG (*.JPEG *.jpeg *.JPG *.jpg *.JPE *.jpe *JFIF *.jfif);; PNG (*.PNG *.png);; GIF (*.GIF *.gif);; Bitmap Files (*.BMP *.bmp *.DIB *.dib);; TIFF (*.TIF *.tif *.TIFF *.tiff);; ICO (*.ICO *.ico)")
        
        #Show the path of the file chosen.
        if self.file_chosen:
            #Find the length of the file path's string.
            str_len = len(self.file_chosen)

            #If the length is longer than 41 characters, shorten the string of the file path to be displayed.
            if str_len > 41:
                #Show the first 22 characters, separate with an ellipsis, and append the last 16 characters.
                file_name = ""

                for c in range(0, 22):
                    file_name += self.file_chosen[c]

                file_name += "..."

                for c in range(str_len-16, str_len):
                    file_name += self.file_chosen[c]

                #Display the abbreviated string on the label.
                main_window.label_file_name.setText(file_name)

            #Else the length of the file path string is not too long, so print the file path as is.
            else:
                main_window.label_file_name.setText(self.file_chosen)

        #Inform the user that no image file was chosen.
        else:
            main_window.label_file_name.setText("No image was selected. Please select an image.")

    #Convert unit to meters.
    def convert_to_meters(self, value, unit):
        #If the unit is meters, there is no need to convert the unit.
        if unit == 0: return value

        #Convert from feet to inches to meters.
        elif unit == 1: return value * 12 * 0.0254

        #Convert from yards to feet to inches to meters.
        elif unit == 2: return value * 3 * 12 * 0.0254

        #Convert from inches to meters.
        elif unit == 3: return value * 0.0254

        #Convert from centimeters to meters.
        else: return value * 0.0100

    #Add commands for actions under the File menu.
    def command_file_menu(self, main_window):
        #Back-end logic for Open Image.
        main_window.action_open_image.setShortcut("CTRL+O")
        main_window.action_open_image.setStatusTip("Open Image")
        main_window.action_open_image.triggered.connect(lambda: self.open_file(main_window))

        #Back-end logic for Record Video.
        main_window.action_record_video.setShortcut("CTRL+R")
        main_window.action_record_video.setStatusTip("Record Video")
        main_window.action_record_video.triggered.connect(lambda: main_window.check_box_record_video.setChecked(True))
        
        #Back-end logic for Stop Recording.
        main_window.action_stop_recording.setShortcut("CTRL+SHIFT+R")
        main_window.action_stop_recording.setStatusTip("Stop Recording")
        main_window.action_stop_recording.triggered.connect(lambda: main_window.check_box_record_video.setChecked(False))

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

    #Display status tips for all clickable widgets from the main window except for the menu.
    def display_status(self, main_window):
        main_window.button_open_image.setStatusTip("Open Image")
        main_window.check_box_record_video.setStatusTip("Record Video")
        main_window.button_start_mapping.setStatusTip("Enter Mapping")

        main_window.button_default_image1.setStatusTip("Select default image: ")
        main_window.button_default_image2.setStatusTip("Select default image: ")
        main_window.button_default_image3.setStatusTip("Select default image: ")
        main_window.button_default_image4.setStatusTip("Select default image: ")

        main_window.double_spin_box_projector_height.setStatusTip("Enter height of projector")
        main_window.combo_box_projector_height.setStatusTip("Choose measurement unit for height of projector")

        main_window.double_spin_box_projector_to_screen.setStatusTip("Enter distance from projector to screen")
        main_window.combo_box_projector_to_screen.setStatusTip("Choose measurement unit for distance from projector to screen")

        main_window.double_spin_box_camera_height.setStatusTip("Enter height of camera")
        main_window.combo_box_camera_height.setStatusTip("Choose measurement unit for height of camera")

        main_window.double_spin_box_camera_to_screen.setStatusTip("Enter distance from camera to screen")
        main_window.combo_box_camera_to_screen.setStatusTip("Choose measurement unit for distance from camera to screen")

#DEBUG: DELETE LATER
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())

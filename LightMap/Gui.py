'''
    Class: COP4331C (Summer 2017)
    Group: G13
    Graphical User Interface for LightMap
'''

#Standard imports.
import os
import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

#Code to run Gui.py as a standalone.
if __name__ != '__main__':
    import InputValues as iv
    import LightMap as lm


#Leverage an object-oriented approach to create the GUI.
class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        #Code to run Gui.py as a standalone.
        if __name__ != "__main__":
            self.user_input = iv.InputValues()
            self.light_map = lm.LightMap()

        self.window_icon = QIcon("../Images/LightMap.png")
        self.width = 715
        self.height = 435

        #Make the main window.
        self.init_main_window()

    #Make the main window.
    def init_main_window(self):
        main_window = uic.loadUi("mainwindow.ui", self)
        self.setWindowIcon(self.window_icon)
        main_window.setFixedSize(self.width, self.height)

        #Set status tips for all clickable widgets from the main window except for the menu.
        self.display_status(main_window)

        #Add commands for actions under the submenus.
        self.command_file_menu(main_window)
        self.command_settings_menu(main_window)
        self.command_help_menu(main_window)

        #Launch saved user preferences.
        main_window

        #Handle the case that the user clicks on the "Open Image" button.
        main_window.button_open_image.clicked.connect(lambda: self.open_image_file(main_window))

        #Handle the case that the user selects one of the default images.
        self.init_default_image(main_window)

        #Handle the case that the user clicks on the "Record Video" checkbox.
        main_window.check_box_record_video.toggled.connect(lambda: self.set_record_action(main_window, "checkbox"))

        #Make sure this variable has been declared so that we can click on "Start Mapping" at any time.
        self.image_file_chosen = None

        #Handle the case that the user clicks on the "Start Mapping" button.
        main_window.button_mapping.clicked.connect(lambda: self.start_mapping(main_window))

        #Show the main window.
        self.show()

    #Map the image to the ball.
    def start_mapping(self, main_window):
        #Check if the user has selected an image before sending the file path to the main program.
        if not self.image_file_chosen:
            QMessageBox.about(self, "No File Selected", "Please select a valid image file before mapping!")

        #Check if the image file exists before sending the image file path to the main program.
        elif not os.path.exists(self.image_file_chosen):
            QMessageBox.about(self, "File Not Found", "The image file could not be found! Please select another image file!")

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

            print(self.image_file_chosen)
            print(hardware_positions)
            print(self.video_file_path)

            #Code for Gui.py to run as a standalone.
            if __name__ != "__main__":
                self.user_input.update_values(hardware_positions, self.image_file_chosen, self.video_file_path)
                self.light_map.launch_app(self.user_input)

    #Close the application when the main window is closed.
    def closeEvent(self, event):
        sys.exit()

    #Add commands for actions under the File menu.
    def command_file_menu(self, main_window):
        main_window.action_open_image.setShortcut("CTRL+O")
        main_window.action_open_image.setStatusTip("Open Image")
        main_window.action_open_image.triggered.connect(lambda: self.open_image_file(main_window))

        #Initialize this command to "Record Video". This command will change to "Stop Recording" later.
        main_window.action_record_video.setShortcut("CTRL+R")
        main_window.action_record_video.setStatusTip("Record Video")
        main_window.action_record_video.triggered.connect(lambda: self.set_record_action(main_window, "menu"))

        main_window.action_start_mapping.setShortcut("F5")
        main_window.action_start_mapping.setStatusTip("Start Mapping")
        main_window.action_start_mapping.triggered.connect(lambda: self.start_mapping(main_window))

        #Disable this command when the GUI is first initialized.
        main_window.action_stop_mapping.setDisabled(True)
        main_window.action_stop_mapping.setShortcut("F6")
        main_window.action_stop_mapping.setStatusTip("Stop Mapping")
        main_window.action_stop_mapping.triggered.connect(lambda: self.stop_mapping(main_window))

        main_window.action_quit.setShortcut("CTRL+Q")
        main_window.action_quit.setStatusTip("Quit")
        main_window.action_quit.triggered.connect(self.close)

    #Add commands for actions under the Settings menu.
    def command_settings_menu(self, main_window):
        main_window.action_preferences.setShortcut("CTRL+P")
        main_window.action_preferences.setStatusTip("Preferences")
        main_window.action_preferences.triggered.connect(lambda: self.init_preferences_window(main_window))

    #Add commands for actions sunder the Help menu.
    def command_help_menu(self, main_window):
        #Back-end logic for LightMap Help.
        main_window.action_LightMap_Help.setShortcut("CTRL+H")
        main_window.action_LightMap_Help.setStatusTip("LightMap Help")

        #Back-end logic for About LightMap.
        main_window.action_About_LightMap.setStatusTip("About LightMap")

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

    #Display the file path of the chosen file, or indicate that no file was chosen.
    def display_file_path(self, source, label, source_string):
        #Determine if this method is relevant to the image file or video file.
        if source is self.image_file_chosen:
            max_len = 42
            a = 23
            b = 16

        elif source is self.video_file_path:
            max_len = 34
            a = 17
            b = 14

        #Show the path of the file chosen.
        if source:
            #Find the length of the file path's string.
            str_len = len(source)

            #If the length is longer than max_len characters, shorten the string of the file path to be displayed.
            if str_len > max_len:
                #Show the first a characters, separate with an ellipsis, and append the last b characters.
                file_name = ""

                for c in range(0, a):
                    file_name += source[c]

                file_name += "..."

                for c in range(str_len-b, str_len):
                    file_name += source[c]

                #Display the abbreviated string on the label.
                label.setText(file_name)

                #Set the tooltip on the label to display the full file path.
                label.setToolTip(source)

            #Else the length of the file path string is not too long, so display the file path as is.
            else:
                label.setText(source)

        #Inform the user that a file could not be chosen.
        else:
            if source_string is "image":
                label.setText("No image was selected. Please select an image.")

            elif source_string is "video":
                label.setText("The folder or file name was not specified.")

    #Display status tips for all clickable widgets from the main window except for the menu.
    def display_status(self, main_window):
        main_window.button_open_image.setStatusTip("Open Image")
        main_window.check_box_record_video.setStatusTip("Record Video")
        main_window.button_mapping.setStatusTip("Start Mapping")

        main_window.button_default_image1.setStatusTip("Earth")
        main_window.button_default_image2.setStatusTip("Moon")
        main_window.button_default_image3.setStatusTip("Smiley Face")
        main_window.button_default_image4.setStatusTip("Pizza")
        main_window.button_default_image5.setStatusTip("Kappa")
        main_window.button_default_image6.setStatusTip("Mystery Image")

        main_window.double_spin_box_projector_height.setStatusTip("Enter height of projector")
        main_window.combo_box_projector_height.setStatusTip("Choose measurement unit for height of projector")

        main_window.double_spin_box_projector_to_screen.setStatusTip("Enter distance from projector to screen")
        main_window.combo_box_projector_to_screen.setStatusTip("Choose measurement unit for distance from projector to screen")

        main_window.double_spin_box_camera_height.setStatusTip("Enter height of camera")
        main_window.combo_box_camera_height.setStatusTip("Choose measurement unit for height of camera")

        main_window.double_spin_box_camera_to_screen.setStatusTip("Enter distance from camera to screen")
        main_window.combo_box_camera_to_screen.setStatusTip("Choose measurement unit for distance from camera to screen")

   	#Allow the user to select or deselect a default image.
    def init_default_image(self, main_window):
    	main_window.button_default_image1.clicked.connect(lambda: self.select_default_image(main_window, main_window.button_default_image1))
    	main_window.button_default_image2.clicked.connect(lambda: self.select_default_image(main_window, main_window.button_default_image2))
    	main_window.button_default_image3.clicked.connect(lambda: self.select_default_image(main_window, main_window.button_default_image3))
    	main_window.button_default_image4.clicked.connect(lambda: self.select_default_image(main_window, main_window.button_default_image4))

   	#Make the preferences window.
    def init_preferences_window(self, main_window):
        preferences_window = PreferencesWindow()
        preferences_window.exec()

    #Open an image file.
    def open_image_file(self, window):
        #Open the file dialog to select an image file.
        self.image_file_chosen, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
            "JPEG (*.JPEG *.jpeg *.JPG *.jpg *.JPE *.jpe *JFIF *.jfif);; PNG (*.PNG *.png);; GIF (*.GIF *.gif);; Bitmap Files (*.BMP *.bmp *.DIB *.dib);; TIFF (*.TIF *.tif *.TIFF *.tiff);; ICO (*.ICO *.ico)")
        
        #Display the file path of the chosen image file, or indicate that no file was chosen.
        GUI.display_file_path(self, self.image_file_chosen, window.label_image_file_name, "image")

    #Select the default image that was chosen by the user.
    def select_default_image(self, main_window, button_default):
        #Identify the name of the image chosen.
        if button_default is main_window.button_default_image1:
            file_name = "Earth.jpg"
        elif button_default is main_window.button_default_image2:
            file_name = "Moon.gif"
        elif button_default is main_window.button_default_image3:
            file_name = "Smiley.jpg"
        elif button_default is main_window.button_default_image4:
            file_name = "Pizza.jpg"
        elif button_default is main_window.button_default_image5:
            file_name = "Kappa.jpg"
        elif button_default is main_window.button_default_image6:
            file_name = "Mystery_Image.jpg"

        #Show the image file name.
        main_window.label_image_file_name.setText(file_name)

        #Provide relative pathing to send back to the main program. All images are in the Images folder.
        if button_default is not main_window.button_default_image6:
            self.image_file_chosen = "../Images/"
            self.image_file_chosen += file_name
        else:
            self.image_file_chosen = "../Images/Mystery_Man.jpg"


    #Link the record option from the menu to the record checkbox on the main window.
    def set_record_action(self, main_window, event_source):
        #Handle the case that the user selected from the menu.
        if event_source == "menu":
            if main_window.check_box_record_video.isChecked() == True:
                main_window.check_box_record_video.setChecked(False)
                main_window.check_box_record_video.setStatusTip("Record Video")
                main_window.action_record_video.setText("Record Video")
                main_window.action_record_video.setStatusTip("Record Video")
                main_window.label_video_file_path.setText("Video recording has been canceled.")
                self.video_file_path = None
            else:
                main_window.check_box_record_video.setChecked(True)
                main_window.check_box_record_video.setStatusTip("Stop Recording")
                main_window.action_record_video.setText("Stop Recording")
                main_window.action_record_video.setStatusTip("Stop Recording")

        #Handle the case that the user directly clicked on the checkbox. Note that the status of the checkbox is assessed after
        #the checkbox has been manually toggled, so everything below here is the inverse of the above.
        elif event_source == "checkbox":
            if main_window.check_box_record_video.isChecked() == True:
                main_window.check_box_record_video.setStatusTip("Stop Recording")
                main_window.action_record_video.setText("Stop Recording")
                main_window.action_record_video.setStatusTip("Stop Recording")
            else:
                main_window.check_box_record_video.setStatusTip("Record Video")
                main_window.action_record_video.setText("Record Video")
                main_window.action_record_video.setStatusTip("Record Video")
                main_window.label_video_file_path.setText("Video recording has been canceled.")
                self.video_file_path = None

        #------------------------------------------------------------------------

        #If the string stays None, then the user chose not to record a video.
        self.video_file_path = None

        #If the user has chosen to record a video, then ask the user to determine the name of the video file as well as the target directory.
        if main_window.check_box_record_video.isChecked() is True:
            self.video_file_path, _ = QFileDialog.getSaveFileName(self, "Save Video", "*.avi", "AVI (*.avi *.AVI)")

            #If the user did not choose to save a video, then uncheck the "Record Video" checkbox and update the menu option.
            if not self.video_file_path:
                main_window.check_box_record_video.setChecked(False)
                main_window.check_box_record_video.setStatusTip("Record Video")
                main_window.action_record_video.setText("Record Video")
                main_window.action_record_video.setStatusTip("Record Video")

            else:
                main_window.check_box_record_video.setStatusTip("Stop Recording")
                main_window.action_record_video.setText("Stop Recording")
                main_window.action_record_video.setStatusTip("Stop Recording")


            #On the GUI, indicate whether the user has determined the target directory and name of the video file.
            self.display_file_path(self.video_file_path, main_window.label_video_file_path, "video")


class PreferencesWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.window_icon = QIcon("../Images/LightMap.png")
        self.width = 385
        self.height = 450

        self.init_preferences_window()

    def init_preferences_window(self):
        preferences_window = uic.loadUi("preferences.ui", self)
        self.setWindowIcon(self.window_icon)
        preferences_window.setFixedSize(self.width, self.height)

        #Handle the case that the user clicks on the "Open Image" button.
        preferences_window.button_open_image.clicked.connect(lambda: GUI.open_image_file(self, preferences_window))

        #Handle the case that the user clicks on the "Always record video" checkbox.

        #Handle the case that the user clicks on the "Save" button.
        preferences_window.button_box.buttons()[0].clicked.connect(lambda: self.save_preferences(preferences_window))

        #Handle the case that the user clicks on the "Discard" button.
        preferences_window.button_box.buttons()[1].clicked.connect(self.close)

        #Show the preferences window.
        self.show()

    #Save user preferences.
    def save_preferences(self, preferences_window):
    	pass


#DEBUG: DELETE LATER
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec_())

'''
    Class: COP4331C (Summer 2017)
    Group: G13
    Graphical User Interface for LightMap

    NAME OF DEVELOPERS, YEAR, PURPOSE, VISION
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

        #Make the main window.
        self.window_icon = QIcon("../Images/LightMap.png")
        self.width = 365
        self.height = 540
        self.init_main_window()

    #Make the main window.
    def init_main_window(self):
        main_window = uic.loadUi("mainwindow.ui", self)
        self.setWindowIcon(self.window_icon)
        main_window.setFixedSize(self.width, self.height)

        #Add commands for actions under the submenus.
        self.command_file_menu(main_window)
        self.command_help_menu(main_window)

        #Set status tips for all clickable widgets from the main window except for the menu.
        self.display_status(main_window)

        #Add functionality to all widgets on the main window.
        self.add_main_functionality(main_window)

        #Show the main window.
        self.show()

    #Add functionality to widgets on the main window.
    def add_main_functionality(self, main_window):
        #Initialize to indicate that no default images have been chosen.
        self.button_default = None

        #Make sure this variable has been declared so that we can click on "Start Mapping" at any time.
        self.image_file_chosen = None

        #If the string stays None, then the user chose not to record a video.
        self.video_file_path = None

        #If this boolean is true, check the status of the video recording checkbox whenever it changes.
        #self.check_status_vr_check_box = True

        #Handle the case that the user clicks on the "Open Image" button.
        main_window.button_open_image.clicked.connect(lambda: self.open_image_file(main_window))

        #Handle the case that the user selects one of the default images.
        self.init_default_image(main_window)

        #Handle the case that the user clicks on the "Record Video" checkbox.
        #main_window.check_box_record_video.toggled.connect(lambda: self.set_record_action(main_window, "checkbox"))

        #Handle the case that the user clicks on the "Start Mapping" button.
        main_window.button_mapping.clicked.connect(lambda: self.start_mapping(main_window))

    #Close the application when the main window is closed.
    def closeEvent(self, event):
        sys.exit()

    #Add commands for actions under the File menu.
    def command_file_menu(self, main_window):
        #Action: Open Image
        main_window.action_open_image.setShortcut("CTRL+O")
        main_window.action_open_image.setStatusTip("Open Image")
        main_window.action_open_image.triggered.connect(lambda: self.open_image_file(main_window))

        #Initialize this command to "Record Video". This command will change to "Stop Recording" later.
        #main_window.action_record_video.setShortcut("CTRL+R")
        #main_window.action_record_video.setStatusTip("Record Video")
        #main_window.action_record_video.triggered.connect(lambda: self.set_record_action(main_window, "menu"))

        #Action: Start Mapping
        main_window.action_start_mapping.setShortcut("F5")
        main_window.action_start_mapping.setStatusTip("Start Mapping")
        main_window.action_start_mapping.triggered.connect(lambda: self.start_mapping(main_window))

        #Action: Stop Mapping. Disable this command when the GUI is first initialized.
        main_window.action_stop_mapping.setDisabled(True)
        main_window.action_stop_mapping.setShortcut("F6")
        main_window.action_stop_mapping.setStatusTip("Stop Mapping")
        main_window.action_stop_mapping.triggered.connect(lambda: self.stop_mapping(main_window))

        #Action: Quit
        main_window.action_quit.setShortcut("CTRL+Q")
        main_window.action_quit.setStatusTip("Quit")
        main_window.action_quit.triggered.connect(self.close)

    #Add commands for actions under the Help menu.
    def command_help_menu(self, main_window):
        #Action: LightMap Help
        main_window.action_LightMap_Help.setShortcut("CTRL+H")
        main_window.action_LightMap_Help.setStatusTip("LightMap Help")
        main_window.action_LightMap_Help.triggered.connect(self.init_help_window)

        #Action: About LightMap.
        main_window.action_About_LightMap.setStatusTip("About LightMap")
        main_window.action_About_LightMap.triggered.connect(self.init_about_window)

    #Display the file path of the chosen file, or indicate that no file was chosen.
    def display_file_path(self, source, label, source_string):
        #Determine if this method is relevant to the image file or video file.
        if source is self.image_file_chosen:
            max_len = 35
            a = 18
            b = 13

        # elif source is self.video_file_path:
        #     max_len = 44
        #     a = 22
        #     b = 19

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
                label.setText("No image was selected.")

            # elif source_string is "video":
            #     label.setText("The folder or file name was not specified.")

    #Display status tips for all clickable widgets from the main window except for the menu.
    def display_status(self, main_window):
        main_window.button_open_image.setStatusTip("Open Image")
#main_window.check_box_record_video.setStatusTip("Record Video")
        main_window.button_mapping.setStatusTip("Start Mapping")

        main_window.button_default_image1.setStatusTip("Earth")
        main_window.button_default_image2.setStatusTip("Moon")
        main_window.button_default_image3.setStatusTip("Smiley Face")
        main_window.button_default_image4.setStatusTip("Pizza")
        main_window.button_default_image5.setStatusTip("Kappa")
        main_window.button_default_image6.setStatusTip("Mystery Image")

    #Make the About LightMap window.
    def init_about_window(self):
        about_window = AboutWindow()
        about_window.exec()

   	#Allow the user to select or deselect a default image.
    def init_default_image(self, main_window):
        main_window.button_default_image1.clicked.connect(lambda: self.select_default_image(main_window, main_window.button_default_image1))
        main_window.button_default_image2.clicked.connect(lambda: self.select_default_image(main_window, main_window.button_default_image2))
        main_window.button_default_image3.clicked.connect(lambda: self.select_default_image(main_window, main_window.button_default_image3))
        main_window.button_default_image4.clicked.connect(lambda: self.select_default_image(main_window, main_window.button_default_image4))
        main_window.button_default_image5.clicked.connect(lambda: self.select_default_image(main_window, main_window.button_default_image5))
        main_window.button_default_image6.clicked.connect(lambda: self.select_default_image(main_window, main_window.button_default_image6))

    #Make the LightMap Help window.
    def init_help_window(self):
        help_window = HelpWindow()
        help_window.exec()

    #Open an image file.
    def open_image_file(self, main_window):
        #If a default image was previous selected, unselect the default image.
        if self.button_default:
            self.button_default.setAutoExclusive(False)
            self.button_default.setChecked(False)
            self.button_default.setAutoExclusive(True)

        #Open the file dialog to select an image file.
        self.image_file_chosen, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
            "JPEG (*.JPEG *.jpeg *.JPG *.jpg *.JPE *.jpe *JFIF *.jfif);; PNG (*.PNG *.png);; GIF (*.GIF *.gif);; Bitmap Files (*.BMP *.bmp *.DIB *.dib);; TIFF (*.TIF *.tif *.TIFF *.tiff);; ICO (*.ICO *.ico)")
        
        #Display the file path of the chosen image file, or indicate that no file was chosen.
        GUI.display_file_path(self, self.image_file_chosen, main_window.label_image_file_name, "image")

    #Select the default image that was chosen by the user.
    def select_default_image(self, main_window, button_default):
        #This variable keeps track of the selected default image so we can reference it in other methods.
        self.button_default = button_default

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
            self.image_file_chosen = "../Images/Mystery.jpg"

    # #Link the record option from the menu to the record checkbox on the main window.
    # def set_record_action(self, main_window, source):
    #     #Handle the case that the user directly clicked on the checkbox. Note that the status of the checkbox is assessed after
    #     #the checkbox has been manually toggled.
    #     if source == "checkbox" and self.check_status_vr_check_box == True:
    #         #If the checkbox was marked true...
    #         if main_window.check_box_record_video.isChecked() == True:
    #             main_window.check_box_record_video.setStatusTip("Stop Recording")
    #             main_window.action_record_video.setText("Stop Recording")
    #             main_window.action_record_video.setStatusTip("Stop Recording")

    #             #Open the file dialog, and handle the case that the user decides not to save their video.
    #             if self.save_video(main_window) == False:
    #                 main_window.check_box_record_video.setChecked(False)
    #                 main_window.check_box_record_video.setStatusTip("Record Video")
    #                 main_window.action_record_video.setText("Record Video")
    #                 main_window.action_record_video.setStatusTip("Record Video")

    #         #Else, the box was marked false, and then the program checks for the false condition.
    #         else:
    #             main_window.check_box_record_video.setStatusTip("Record Video")
    #             main_window.action_record_video.setText("Record Video")
    #             main_window.action_record_video.setStatusTip("Record Video")
    #             main_window.label_video_file_path.setText("Video recording has been canceled.")
    #             self.video_file_path = None

    #     #Handle the case that the user chose to record or stop recording through the file menu. Note that the status of the
    #     #checkbox is assessed as is, so everything below here here is the inverse of the above.
    #     elif source == "menu":
    #         #The checkbox is currently true, so we have to unmark it.
    #         if main_window.check_box_record_video.isChecked() == True:
    #             main_window.check_box_record_video.setChecked(False)
    #             main_window.check_box_record_video.setStatusTip("Record Video")
    #             main_window.action_record_video.setText("Record Video")
    #             main_window.action_record_video.setStatusTip("Record Video")
    #             main_window.label_video_file_path.setText("Video recording has been canceled.")
    #             self.video_file_path = None

    #         #Else the box was currently marked false, so we have to mark it true.
    #         else:
    #             self.check_status_vr_check_box = False
    #             main_window.check_box_record_video.setChecked(True)
    #             main_window.check_box_record_video.setStatusTip("Stop Recording")
    #             main_window.action_record_video.setText("Stop Recording")
    #             main_window.action_record_video.setStatusTip("Stop Recording")
                
    #             #Open the file dialog, and handle the case that the user decides not to save their video.
    #             if self.save_video(main_window) == False:
    #                 main_window.check_box_record_video.setChecked(False)
    #                 main_window.check_box_record_video.setStatusTip("Record Video")
    #                 main_window.action_record_video.setText("Record Video")
    #                 main_window.action_record_video.setStatusTip("Record Video")

    #             #Reset this variable to true so that we can click on the checkbox later.
    #             self.check_status_vr_check_box = True
                

    # #Save the video file.
    # def save_video(self, main_window):
    #     #If the user has chosen to record a video...
    #     if main_window.check_box_record_video.isChecked() == True:
    #         #Then ask the user to determine the name of the video file as well as the target directory.
    #         self.video_file_path, _ = QFileDialog.getSaveFileName(self, "Save Video", "*.avi", "AVI (*.avi *.AVI)")

    #         #On the GUI, indicate whether the user has determined the target directory and name of the video file.
    #         self.display_file_path(self.video_file_path, main_window.label_video_file_path, "video")

    #         #Return true if the user chose a file name. Otherwise, return false.
    #         return True if self.video_file_path else False

    #Map the image to the ball.
    def start_mapping(self, main_window):
        #Check if the user has selected an image before sending the file path to the main program.
        if not self.image_file_chosen:
            QMessageBox.about(self, "No File Selected", "Please select a valid image file before mapping!")

        #Check if the image file exists before sending the image file path to the main program.
        elif not os.path.exists(self.image_file_chosen):
            QMessageBox.about(self, "File Not Found", "The image file could not be found! Please select another image file!")

        #Everything is good to go! Send the data to the rest of the program.
        else:
            #Code for Gui.py to run as a standalone.
            if __name__ != "__main__":
                self.user_input.update_values(self.image_file_chosen, self.video_file_path)
                self.light_map.launch_app(self.user_input)


#Make the About LightMap dialog window.
class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.window_icon = QIcon("../Images/LightMap.png")
        self.width = 295
        self.height = 260
        self.init_about_window()

    def init_about_window(self):
        about_window = uic.loadUi("about.ui", self)
        self.setWindowIcon(self.window_icon)
        about_window.setFixedSize(self.width, self.height)
        
        #Handle the case that the user clicks on the "Close" button.
        about_window.button_box.buttons()[0].clicked.connect(self.close)

        #Show the About LightMap window.
        self.show()


#Make the LightMap Help window.
class HelpWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.window_icon = QIcon("../Images/LightMap.png")
        self.width = 400
        self.height = 300
        self.init_help_window()

    def init_help_window(self):
        help_window = uic.loadUi("help.ui", self)
        self.setWindowIcon(self.window_icon)
        help_window.setFixedSize(self.width, self.height)

        #Handle the case that the user clicks on the "Close" button.
        help_window.button_box.buttons()[0].clicked.connect(self.close)

        #Show the LightMap Help window.
        self.show()

#DEBUG: DELETE LATER
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec_())

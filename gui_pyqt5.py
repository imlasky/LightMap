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
        self.window_icon = QIcon("LightMap.png")
        
        #Define the dimensions of the main GUI window.
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480

        self.init_ui()
    
    #Fill the GUI.
    def init_ui(self):
        #Set the title, window icon, and dimensions of the main window.
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.window_icon)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Display the name of the application.
        app_name_label = QLabel(self)
        app_name_label.move(120, 25)
        app_name_logo = QPixmap("LightMap.png")
        app_name_label.setPixmap(app_name_logo)
        app_name_label.resize(396, 141)

        #Create the menu.
        self.make_menu()

        #Add a button to open an image file.
        open_image_butt = QPushButton("Open Image", self)
        open_image_butt.move(250, 200)
        fileChosen = open_image_butt.clicked.connect(self.open_file)
        #Display the directory path of the file chosen.
        file_name = "No File Selected"
        label_file_name = QLabel(file_name, self)
        label_file_name.move(265, 250)

        #Tell the user to start the program.
        text_start_mapping = "Once you have selected an image, start mapping!"
        label_start_mapping = QLabel(text_start_mapping, self)
        label_start_mapping.move(200, 300)
        label_start_mapping.resize(350, 20)

        #Add a button to start the main program to map the chosen image onto a ball.
        map_image_butt = QPushButton("Start Mapping", self)
        map_image_butt.move(250, 350)

        #Show the main window.
        self.show()

    #Make the menu.
    def make_menu(self):
        #Create a menu bar at the top of the window.
        main_menu = self.menuBar()

        #Create some submenus.
        file_menu = main_menu.addMenu("File")
        view_menu = main_menu.addMenu("View")
        settings_menu = main_menu.addMenu("Settings")
        help_menu = main_menu.addMenu("Help")

        #Add options to the submenus.
        self.cascade_file_menu(file_menu)
        self.cascade_view_menu(view_menu)
        self.cascade_settings_menu(settings_menu)
        self.cascade_help_menu(help_menu)



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
        #Add a setting to configure hardware positions.
        config_positions_option = QAction("Configure Hardware Positions", self)
        settings_menu.addAction(config_positions_option)

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
    ex = MainWindow()
    sys.exit(app.exec_())

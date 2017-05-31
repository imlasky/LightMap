'''
    Class: COP4331C (Summer 2017)
    Group: G13
    Graphical User Interface for LightMap
'''

import tkinter
from tkinter import filedialog
from tkinter import messagebox

#Leverage an object-oriented approach to create the GUI.
class GUI:
    #Structure the GUI.
    def __init__(self, root):
        frameRoot = Frame(root)
        frameRoot.pack()
        
        #Display the name of the application.
        self.appName = Label(frameRoot, text="LightMap", fg="yellow", bg="black")
        self.appName.grid(row=0, column=1)
        
        #Tell the user to open an image file to map onto the ball.
        self.labelOpenFile = Label(frameRoot, text="Choose an image file to map onto the ball.")
        self.labelOpenFile.grid(row=1, column=1)
        
        #Make a button to open the image file.
        self.fileChosen = None #Prevent the user from mapping without first selecting an image.
        self.buttonFile = Button(frameRoot, text="Open Image...", command=self.openFile)
        self.buttonFile.grid(row=2, column=1)
        
        #Display the directory path of the file chosen.
        self.fileName = StringVar()
        self.fileName.set("No File Selected")
        self.labelFileName = Label(frameRoot, textvariable=self.fileName, fg="red")
        self.labelFileName.grid(row=3, column=1)
        
        #Tell the user to start the program.
        self.labelStart = Label(frameRoot, text="Once you have selected an image, start mapping!")
        self.labelStart.grid(row=4, column=1)
        
        #Make a button to start the program and return the file path to the main program.
        self.buttonStart = Button(frameRoot, text="Start Mapping", command=self.returnFile)
        self.buttonStart.grid(row=5, column=1)
    
    #Open the image file.
    def openFile(self):
        #Only accept the following file types.
        self.fileChosen = filedialog.askopenfilename(filetypes=[("Bitmap Files", "*.BMP *.bmp *.DIB *.dib"),
                                                              ("JPEG", "*.JPEG *.jpeg *.JPG *.jpg *.JPE *.jpe *JFIF *.jfif"),
                                                              ("PNG", "*.PNG *.png"),
                                                              ("GIF", "*.GIF *.gif"),
                                                              ("TIFF", "*.TIF *.tif *.TIFF *.tiff"),
                                                              ("ICO", "*.ICO *.ico")
                                                             ])
        #If a file was selected, show the file path. Else, inform the user.
        if self.fileChosen:
            self.fileName.set(self.fileChosen)
        else:
            self.fileName.set("No image was selected. Please select an image.")
    
    
    #Start the program.
    def returnFile(self):
        #Check if the user has selected an image before sending the file path to the main program.
        if not self.fileChosen:
            tkinter.messagebox.showinfo("No File Selected", "Please select a valid image file before mapping!")
        else:
            return self.fileChosen

#Create a blank window.
root = Tk()

#Create an object to access the class.
g = GUI(root)

#Keep the window open.
root.mainloop()
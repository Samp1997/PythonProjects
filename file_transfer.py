import tkinter as tk

import os
import shutil
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Creates buttton to tranfer files
        self.transfer_btn = Button(text="Tranfer Files", width=20, command=self.transferFiles)
        #Positions file transfer button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0,15))
        def destDir(self):
                selectSourceDir = tkinter.filedialog.askdirectory()
                #The .delete(0, END) will clear the content that is inserted in the Entry widget,
                #this allows the path to br inserted into the Entry widget properly.
                self.source_dir.delete(0, END)
                #The .insert method will insert the user selection to the source_dir Entry
                self.source_dir.insert(0, selectSourceDir)
                #sets title of GUI window
                self.master.title("File Transfer")
        def tranferFiles(self):
                #Gets source directory
                source = self.source_dir.get()
                #Gets destination directory
                destination = self.destination_dir.get()
                #Gets a list of the files in the source directory
                source_files = os.listdir(source)
                #Runs through each file in the source directory
                for i in source_files:
                    #moves each file from the source to the destination
                    shutil.move(source + '/' + i, destination)
                    print(i + ' was successfully tranferred.')
#time
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#Creates button to select files from source directory
self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
#Positions source button in GUI using tkinter grid()
self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30,0))

#Creates entry for source directory selection
self.source_dir = Entry(width=75)
#Positions entry in GUI using tkinter grid() padx and pady are the same as
#the button to ensure they will line up
self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30,0))


#Creates button to select destination of files from destination directory
self.destDir_btn = Button(text="Select Destination", width=20)
#Positions destinationbutton in GUI using tkinter grid()
#on the next row under the source button
self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

#Creates entry for destination directory selection
self.destination_dir = Entry(width=75)
#Positions entry in GUI using tkinter grid() padx and pady are the same as
#the button to ensure they will line up
self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))


#Creates function to exit program
def exit_program(self):
    #root is the main GUI window, the Tkinter destroy method
    #tells python to terminate root.mainloop and all the widgets inside the GUI window
    root.destroy()

#Creates an Exit button
self.exit_btn = Button(text = "Exit", width=20, command=self.exit_program)
#position
self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0,15))
    











if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

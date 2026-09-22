

import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Sets title of GUI window
        self.master.title("File Transfer")

        #creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))
        
        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #creates button to select destination of files from destination directory
        self.desDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Positions destination button in GUI using tkinter grid()
        #on the next row under the source button
        self.desDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #creates button to transfer files
        self.transfer_btn = Button(text= "Transfer Files", width=20, command=self.transferFiles)
        #Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #creates an exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #positions the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))
        
    #creates function to select source directory.
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly.
        self.source_dir.delete(0, END)
        #the .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

    #creates function to select destination directory.
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly
        self.destination_dir.delete(0, END)
        #the .insert method will insert the user selection to the destination_dir entry widget
        self.destination_dir.insert(0, selectDestDir)
        
    #creates function to transfer files from one directory to another
    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()
        #gets destination directory
        destination = self.destination_dir.get()

        #gets current date and time
        current_time = datetime.now()
        #subtracts 24 hours from the current time
        #this gives us the cutoff time
        cutoff_time = current_time - timedelta(hours=24)
        
        #gets a list of files in the source directory
        source_files = os.listdir(source)
        #Runs through each file in the source directory
        for i in source_files:

            #creates the complete filepath for current file
            file_path = os.path.join(source, i)

            #gets the last modified timestamp of the file
            file_timestamp = os.path.getmtime(file_path)

            #converts timestamp into a readable datetime
            file_time = datetime.fromtimestamp(file_timestamp)

            #shows the file and its modified time
            print("File:", i)
            print("Modified:", file_time)

            #checks if the file was modified within the last 24 hours
            if file_time >= cutoff_time:
                #moves the file from source directory to destination directory
                shutil.move(file_path, destination)

                #prints a message showing the file was transferred
                print(i + 'was successfully transferred.')
            else:
                print("RESULT: Older than 24 hours - Not transferred.")

    #creates function to exit program
    def exit_program(self):
        #root is the main GUI window, the tkinter destory method
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()
    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

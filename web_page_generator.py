

import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #sets the title of the GUI window
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0, padx=(10,10), pady=(10,10))

        #creates a label that tells user what to do
        self.label = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        #creates an entry widget where user can type custom text
        self.customText = Entry(self.master, width=100)
        self.customText.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        #creates the button for custom HTML page
        self.customBtn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.customBtn.grid(row=2, column=1, padx=10, pady=10)

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


    def customHTML(self):
        #gets the text that the user entered into the entry widget
        htmlText = self.customText.get()
        #create or overwites the index.html file
        htmlFile = open("index.html", "w")
        #creates html content using user's custom text
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        #write the html content into the file
        htmlFile.write(htmlContent)
        #close the html file
        htmlFile.close()
        #open the html page in a new browser tab
        webbrowser.open_new_tab("index.html")
        









if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

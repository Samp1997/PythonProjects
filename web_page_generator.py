import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.labeltext = Label(text = "Enter Custom text or default HTML page button")
        self.labeltext.grid(row=0, column=0, padx=20, pady=(20, 0))
        self.textentry = Entry(self.master)
        self.textentry.grid(row=1, column=0, padx=(30, 15), pady=(10, 10), columnspan=3, sticky=W+E)
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=1, padx=(0,10), pady=(0, 10))
        self.btn2 = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btn2.grid(row=2, column=2, padx=(0,10), pady=(0, 10))
        
        

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n<html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        htmlText = self.textentry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n<html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()



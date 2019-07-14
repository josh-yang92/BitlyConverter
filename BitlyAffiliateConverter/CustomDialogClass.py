from tkinter import *
import pyperclip


#   Window showing the shortened link with the name of the product
class CustomDialog:
    def __init__(self, parent, title=None, text=None):
        self.data = text
        #   initialise the window
        top = self.top = Toplevel(parent)
        Label(top, text=title).pack()

        #   display the product name with the shortened link
        self.e = Text(top, width=100, height=4)
        self.e.insert("1.0", self.data)
        self.e.pack(padx=5)

        #   initialise the buttons for copying for closing
        self.b = Button(top, text="Copy", width=10, command=self.clipBoardCopy)
        self.b.pack(padx=5, pady=5)
        self.c = Button(top, text="Close", width=10, command=self.close)
        self.c.pack(padx=5, pady=5)

    #   function to close the window
    def close(self):
        self.top.destroy()

    #   function to copy the name and the link to the local clipboard and closing the window automatically
    def clipBoardCopy(self):
        pyperclip.copy(self.e.get('1.0', END).strip())
        Label(self.top, text='copied!').pack()
        self.top.after(500, lambda: self.top.destroy())
import tkinter as tk

from .CustomDialogClass import CustomDialog
from .RequestingFunctions import getItemName
from .RequestingFunctions import getShortLink


class Run:
    def __init__(self, root, keys):
        self.root = root
        self.keys = keys
        self.affLink = None
        self.longLink = None

    #   combine the shortened link and the product name, display it in a window
    def showDialog(self, shortenedURL, itemName):
        inputText = itemName + ': ' + shortenedURL
        CustomDialog(self.root, title="Link", text=inputText)

    #   combine the affiliate link to the site url, get the item names and display it all
    def convert(self):
        combinedLink = self.affLink.get('1.0', tk.END).strip() + '/' + self.longLink.get('1.0', tk.END).strip()
        itemName = getItemName(self.longLink.get('1.0', tk.END).strip())
        self.showDialog(getShortLink(self.keys['APIUser'], self.keys['APIKey'], combinedLink), itemName)

    def runApp(self):
        canvas1 = tk.Canvas(self.root, width=300, height=150)
        canvas1.grid()

        tk.Label(self.root, text='Affiliate Link').grid(row=0)
        tk.Label(self.root, text='Long URL').grid(row=1)

        self.affLink = tk.Text(self.root, width=100, height=5)
        self.longLink = tk.Text(self.root, width=100, height=5)

        self.affLink.insert("end", self.keys['AffLink'])

        self.affLink.grid(row=0, column=1)
        self.longLink.grid(row=1, column=1)

        button1 = tk.Button(text='Convert!', command=self.convert, bg='brown', fg='white').grid(row=3)
        canvas1.create_window(150, 150, window=button1)

        self.root.mainloop()

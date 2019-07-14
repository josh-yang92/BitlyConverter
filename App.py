import tkinter as tk
import os

from BitlyAffiliateConverter import getKeys
from BitlyAffiliateConverter import Run

if __name__ == '__main__':
    folderDir = os.path.abspath('..')
    keysDir = os.path.join(folderDir, 'Keys')
    keys = getKeys(keysDir)

    root = tk.Tk()
    Run(root, keys).runApp()


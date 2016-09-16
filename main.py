#!usr/bin/python

import gui
from Tkinter import *


def main():
    root = Tk()
    graphical_interface = gui.UserInterface(root)
    root.destroy()

if __name__ == '__main__':
    main()

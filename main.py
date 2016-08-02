#!usr/bin/python
import pomodoro
import gui
from Tkinter import *

def main():
    root = Tk()
    timer = pomodoro.PomodoroTimer(0.2, 0.05, 0.3, 4)
    graphical_interface = gui.UserInterface(root, timer)
    root.destroy()

if __name__ == '__main__':
    main()
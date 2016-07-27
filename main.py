#!usr/bin/python
import pomodoro
import gui
from Tkinter import *

def user_interface():
    timer = pomodoro.PomodoroTimer(0.2, 0.05, 0.3, 4)
    print("Action:")
    print("1 - Start working")
    print("2 - Cancel timers and exit program")
    print("What's your decision: ")
    chosen_option= input()

    if str(chosen_option) == "1":
        print("starting timer")
        timer.start()
    elif str(chosen_option) == "2":
        print("option 2")
        # Threads have to be saved in some structure to enable its canceling
        print("Goodbye")
    else:
        print("option 3")
        print("Goodbye")

def main():
    #user_interface()
    root = Tk()
    graphical_interface = gui.UserInterface(root)
    root.mainloop()
    root.destroy()

if __name__ == '__main__':
    main()
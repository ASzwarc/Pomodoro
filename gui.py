from Tkinter import *

class UserInterface:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.create_widgets()

    def create_widgets(self):
        self.quit_button = Button(self.frame, text="QUIT", fg="red", command=self.frame.quit)
        self.quit_button.pack()

from Tkinter import *
import threading


class UserInterface(Frame):

    def __init__(self, master):
        #self.timer_application = timer_application
        self.application_thread = threading.Thread(target=self.start_application)
        self.initialize_master(master)
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.mainloop()

    def initialize_master(self, master):
        master.title("Pomodoro timer")
        master.geometry("300x200")

    def create_widgets(self):
        self.quit_button = Button(self, text="QUIT", fg="red", command=self.stop_application)
        self.start_button = Button(self, text="Start", fg="green", command=self.application_thread.start)
        self.start_button.grid()
        self.quit_button.grid()

    def start_application(self):
        #self.timer_application.start()
        pass

    def stop_application(self):
        #self.timer_application.stop()
        self.application_thread.join()
        self.quit()

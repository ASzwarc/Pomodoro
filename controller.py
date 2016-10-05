from PyQt5 import QtWidgets, QtCore
import main_window
import time
import dialog
import stepfinished_dialog
import settings_dialog

class PomodoroSteps:
    Idle, Work, ShortBreak, LongBreak = range(0, 4)

class Controller():
    def __init__(self):
        self.start_time = time.time()
        self.work_time = 5
        self.short_break_time = 10
        self.long_break_time = 20
        self.unit_size = 4
        self.step = PomodoroSteps.Idle
        self.wasStarted = False
        self.step_time = 0
        self.units_counter = 0
        self.initialize_ui()
        self.timer = QtCore.QTimer(self.mainWindow)
        self.timer.timeout.connect(self.handle_timeout)
    
    def initialize_ui(self):
        self.mainWindow = main_window.MainWindow(self.handle_start_button, 
            self.handle_stop_button, self.handle_reset_button, self.handle_settings_button, 
            lambda: self.handle_default("Statistics"))     
        self.dialogWindow = dialog.Dialog()
        self.stepFinishedDialog = stepfinished_dialog.StepFinishedDialog(
            self.dialog_window_ok_callback, self.dialog_window_cancel_callback)
        self.settingsWindow = settings_dialog.SettingsDialog(self.settings_window_ok_callback, 
            self.settings_window_cancel_callback)
        self.update_status_labels()
        self.mainWindow.show()

    def settings_window_ok_callback(self):
        pass

    def settings_window_cancel_callback(self):
        pass

    def dialog_window_ok_callback(self):
        self.set_next_step()
        self.update_status_labels()
        self.start_time = time.time()
        self.timer.start(1000)

    def dialog_window_cancel_callback(self):
        print("Cancel clicked - stop")

    def handle_settings_button(self):
        self.settingsWindow.show()

    def handle_default(self, button_name):
        self.dialogWindow.set_information(button_name)
        self.dialogWindow.show()

    def handle_start_button(self):
        if self.wasStarted == False:
            self.wasStarted = True
            self.set_next_step()
            self.update_status_labels()
            self.start_time = time.time()
            self.timer.start(1000)
        else:
            print("Illegal action, program is already running")

    def handle_stop_button(self):
        self.timer.stop()
    
    def handle_reset_button(self):
        self.timer.stop()
        self.mainWindow.update_elapsed_time_label("00:00")
        self.step = PomodoroSteps.Idle
        self.wasStarted = False
        self.units_counter = 0
        self.update_status_labels()

    def handle_timeout(self):
        elapsed_time_float = time.time() - self.start_time
        elapsed_time = time.strftime("%M:%S", time.gmtime(elapsed_time_float))
        self.mainWindow.update_elapsed_time_label(elapsed_time)
        if elapsed_time_float >= self.step_time:
            self.timer.stop()
            if self.step == PomodoroSteps.Work:
                self.units_counter += 1
            self.show_notification()
        else:
            self.timer.start()
    
    def show_notification(self):
        text_to_display = ""
        if self.step == PomodoroSteps.Work:
            text_to_display = "Work "
        elif self.step == PomodoroSteps.ShortBreak:
            text_to_display = "Short break "
        elif self.step == PomodoroSteps.LongBreak:
            text_to_display = "Long break "
        else:
            print("Illegal action, this shouldn't happen")
            #raise exception
        text_to_display += "has been finished"
        self.stepFinishedDialog.set_information(text_to_display)
        self.stepFinishedDialog.show()
    
    def update_status_labels(self):
        phase_name = ""
        if self.step == PomodoroSteps.Work:
            phase_name = "Work"
        elif self.step == PomodoroSteps.ShortBreak:
            phase_name = "Short break"
        elif self.step == PomodoroSteps.LongBreak:
            phase_name = "Long break"
        elif self.step == PomodoroSteps.Idle:
            phase_name = "Idle"
        self.mainWindow.update_phase_label(phase_name)
        self.mainWindow.update_unit_no_label(str(self.units_counter))

    def set_next_step(self):
        if self.step == PomodoroSteps.Work:
            self.step = PomodoroSteps.ShortBreak
            self.step_time = self.short_break_time
        elif (self.step == PomodoroSteps.ShortBreak) and (self.units_counter < self.unit_size):
            self.step = PomodoroSteps.Work
            self.step_time = self.work_time
        elif (self.step == PomodoroSteps.ShortBreak) and (self.units_counter >= self.unit_size):
            self.step = PomodoroSteps.LongBreak
            self.step_time = self.long_break_time
        elif self.step == PomodoroSteps.LongBreak:
            self.step = PomodoroSteps.Work
            self.step_time = self.work_time
        elif self.setp == PomodoroSteps.Idle:
            self.step = PomodoroSteps.Work
            self.step_time = self.work_time
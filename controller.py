from PyQt5 import QtWidgets, QtCore
import design
import time
import dialog
import stepfinished_dialog

class PomodoroSteps:
    Idle, Work, ShortBreak, LongBreak = range(0, 4)

class Controller(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.initialize_ui()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.handle_timeout)
        self.start_time = time.time()
        self.work_time = 5
        self.short_break_time = 10
        self.long_break_time = 20
        self.unit_size = 4
        self.step = PomodoroSteps.Idle
        self.wasStarted = False
        self.step_time = 0
        self.units_counter = 0
    
    def initialize_ui(self):
        self.setupUi(self)
        self.dialogWindow = dialog.Dialog()
        self.stepFinishedDialog = stepfinished_dialog.StepFinishedDialog(
            self.dialog_window_ok_callback, self.dialog_window_cancel_callback)
        self.startButton.clicked.connect(self.handle_start_button)
        self.stopButton.clicked.connect(self.handle_stop_button)
        self.resetButton.clicked.connect(self.handle_reset_button)
        self.settingsButton.clicked.connect(lambda: self.handle_default("Settings"))
        self.statisticsButton.clicked.connect(lambda: self.handle_default("Statistic"))
        self.elapsedTimeLabel.setText("00:00")

    def dialog_window_ok_callback(self):
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
        else:
            pass

        print("OK clicked - continue")
        self.start_time = time.time()
        self.timer.start(1000)

    def dialog_window_cancel_callback(self):
        print("Cancel clicked - stop")

    def handle_default(self, button_name):
        self.dialogWindow.set_information(button_name)
        self.dialogWindow.show()

    def handle_start_button(self):
        if self.wasStarted == False:
            self.step_time = self.work_time
            self.wasStarted = True
            self.step = PomodoroSteps.Work
            self.start_time = time.time()
            self.timer.start(1000)
        else:
            print("Illegal action, program is already running")

    def handle_stop_button(self):
        self.timer.stop()
    
    def handle_reset_button(self):
        self.timer.stop()
        self.elapsedTimeLabel.setText("00:00")
        self.step = PomodoroSteps.Idle
        self.wasStarted = False
        self.units_counter = 0

    def handle_timeout(self):
        elapsed_time_float = time.time() - self.start_time
        elapsed_time = time.strftime("%M:%S", time.gmtime(elapsed_time_float))
        self.elapsedTimeLabel.setText(elapsed_time)
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
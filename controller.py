from PyQt5 import QtWidgets, QtCore
import design
import time
import dialog
import stepfinished_dialog

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
        print("OK clicked - continue")

    def dialog_window_cancel_callback(self):
        print("Cancle clicked - stop")

    def handle_default(self, button_name):
        self.dialogWindow.set_information(button_name)
        self.dialogWindow.show()

    def handle_start_button(self):
        self.start_time = time.time()
        self.timer.start(1000)

    def handle_stop_button(self):
        self.timer.stop()
    
    def handle_reset_button(self):
        self.timer.stop()
        self.elapsedTimeLabel.setText("00:00")

    def handle_timeout(self):
        elapsed_time_float = time.time() - self.start_time
        elapsed_time = time.strftime("%M:%S", time.gmtime(time.time() - self.start_time))
        self.elapsedTimeLabel.setText(elapsed_time)
        if elapsed_time_float >= self.work_time:
            self.timer.stop()
            self.stepFinishedDialog.set_information("Work has been finished")
            self.stepFinishedDialog.show()
        else:
            self.timer.start()
from PyQt5 import QtWidgets
from design.settings_dialog_design import Ui_SettingsWindow


class SettingsDialog(QtWidgets.QDialog, Ui_SettingsWindow):
    def __init__(self, accept_callback, reject_callback):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(
            lambda: self.handle_accept(accept_callback))
        self.buttonBox.rejected.connect(
            lambda: self.handle_reject(reject_callback))

    def handle_accept(self, accept_callback):
        accept_callback()
        self.accept

    def handle_reject(self, reject_callback):
        reject_callback()
        self.reject

    def set_current_values(self, work_time, short_break_time,
                           long_break_time, no_of_units):
        self.shortBreakTimeEdit.setText(short_break_time)
        self.longBreakTimeEdit.setText(long_break_time)
        self.workTimeEdit.setText(work_time)
        self.noOfUnitsEdit.setText(no_of_units)

    def get_work_time(self):
        return self.workTimeEdit.text()

    def get_short_break_time(self):
        return self.shortBreakTimeEdit.text()

    def get_long_break_time(self):
        return self.longBreakTimeEdit.text()

    def get_no_of_units(self):
        return self.noOfUnitsEdit.text()

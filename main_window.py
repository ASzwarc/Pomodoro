from PyQt5 import QtWidgets, QtCore
from design.main_window_design import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, action_on_start_button, action_on_stop_button,
                 action_on_reset_button, action_on_settings_button,
                 action_on_statistics_button):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.startButton.clicked.connect(action_on_start_button)
        self.stopButton.clicked.connect(action_on_stop_button)
        self.resetButton.clicked.connect(action_on_reset_button)
        self.settingsButton.clicked.connect(action_on_settings_button)
        self.statisticsButton.clicked.connect(action_on_statistics_button)
        self.elapsedTimeLabel.setText("00:00")

    def update_elapsed_time_label(self, text):
        self.elapsedTimeLabel.setText(text)

    def update_phase_label(self, text):
        self.phaseLabel.setText(text)

    def update_unit_no_label(self, text):
        self.unitNoLabel.setText(text)

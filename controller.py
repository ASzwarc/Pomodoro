from PyQt5 import QtWidgets, QtCore
import design
import time

class Controller(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.initialize_ui()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.handle_timeout)
        self.start_time = time.time()
    
    def initialize_ui(self):
        self.setupUi(self)
        self.startButton.clicked.connect(self.handle_start_button)
        self.stopButton.clicked.connect(self.handle_stop_button)
        self.resetButton.clicked.connect(self.handle_reset_button)
        self.elapsedTimeLabel.setText("00:00")

    def handle_start_button(self):
        self.start_time = time.time()
        self.timer.start(1000)

    def handle_stop_button(self):
        self.timer.stop()
    
    def handle_reset_button(self):
        self.timer.stop()
        self.elapsedTimeLabel.setText("00:00")

    def handle_timeout(self):
        elapsed_time = time.strftime("%M:%S", time.gmtime(time.time() - self.start_time))
        self.elapsedTimeLabel.setText(elapsed_time)
        self.timer.start()
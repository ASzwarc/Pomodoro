from PyQt5 import QtWidgets, QtCore
import design

class Controller(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.startButton.clicked.connect(self.start_timer)
        self.stopButton.clicked.connect(self.stop_timer)
        self.resetButton.clicked.connect(self.reset_timer)
    
    def start_timer(self):
        pass
    
    def stop_timer(self):
        pass
    
    def reset_timer(self):
        pass
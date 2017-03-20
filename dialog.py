from PyQt5 import QtWidgets
from design import dialog_design


class Dialog(QtWidgets.QDialog, dialog_design.Ui_dialogWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

    def set_information(self, button_name):
        self.label.setText(button_name + " button not implemented yet !")

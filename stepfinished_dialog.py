from PyQt5 import QtWidgets
import stepfinished_dialog_design

class StepFinishedDialog(QtWidgets.QDialog, stepfinished_dialog_design.Ui_StepFinishedDialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.handle_accept)
        self.buttonBox.rejected.connect(self.handle_reject)

    def handle_accept(self):
        print("Accept was clicked")
        self.accept

    def handle_reject(self):
        print("Cancel was clicked")
        self.reject

    def set_information(self, text_to_display):
        self.notificationLabel.setText(text_to_display)
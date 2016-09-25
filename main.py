#!usr/bin/python

import controller
import sys
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    gui_controller = controller.Controller()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

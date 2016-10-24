#!usr/bin/python

import sys
from PyQt5.QtWidgets import QApplication
import controller


def main():
    app = QApplication(sys.argv)
    controller.Controller()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

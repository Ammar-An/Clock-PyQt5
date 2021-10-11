# PyQt5 import
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import os
from os import path
import sys

from time import strftime
import time


FORM_Class,_ = loadUiType(path.join(path.dirname(__file__), "Clock-Design.ui"))     # The Name of the design

class MainApp(QMainWindow, FORM_Class):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.time_fun()

    def time_fun(self):
        while True:
            string = strftime("%I:%M:%S  %p")
            self.label.setText(string)
            # self.label.after(1000, string)
            time.sleep(1)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()         # Infinity loop

if __name__ == '__main__':
    main()

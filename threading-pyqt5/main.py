# -*- coding: utf-8 -*-
from threading import currentThread
import time

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys
from PyQt5.QtCore import pyqtSignal, QThread, pyqtSlot


class SubWindow(QWidget):
    def __init__(self, parent=None):
        super(SubWindow, self).__init__(parent)
        self.resize(400, 400)
        self.button = QPushButton(self)
        self.button.setText('push me to print ***')
        self.button.move(200, 200)
        self.button.clicked.connect(self.print_)
    
    @pyqtSlot()
    def print_(self):
        print('hello from subwindow')


class SignalStore(QThread):
    print_func = pyqtSignal(str)

    def __init__(self):
        super(SignalStore, self).__init__()

    def run(self):
        time.sleep(1) # fake working...
        self.print_func.emit("hello from thread")


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(400, 400)
        self.subwin = SubWindow()
        self.button = QPushButton(self)
        self.button.setText('push me to get subwindow')
        self.button.move(200, 200)

        self.button.clicked.connect(self.send_signal)

        self.med_signal = SignalStore()
        self.med_signal.print_func.connect(self.print_from_main)
        
    def send_signal(self):
        self.subwin.show()
        self.med_signal.start()

    @pyqtSlot(str)
    def print_from_main(self, string: str):
        print(string)
        self.subwin.print_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import *
from numpy.random import randint
import sys
from PyQt5.QtCore import QThread, pyqtSignal
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime

start = datetime.now()


def random():
    return randint(10000, size=1000)


class MplFigure(object):
    def __init__(self, parent):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)


class plotThread(QThread):
    finished = pyqtSignal()

    def __init__(self, main_figure, ax1):
        super(plotThread, self).__init__()
        self.main_figure = main_figure
        self.ax1 = ax1

    def run(self):
        x = randint(10000, size=300)
        y = randint(10000, size=300)
        self.ax1.scatter(x, y)

        self.main_figure.canvas.draw()
        self.finished.emit()


# Create Window
class Window(QWidget):
    def __init__(self):
        super().__init__()

        # get left list name from random
        self.leftlist_name = random()

        # Create tabs
        tabs = QTabWidget()
        tabs.addTab(self.tab1_func(), 'Tab1')
        tabs.addTab(self.tab2_func(), 'Tab2')

        # Create a button to refresh Tab1
        refresh_btn = QPushButton('Refresh Interface')
        refresh_btn.clicked.connect(self.refresh_func)

        # vboxlayout
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(refresh_btn)
        self.vbox.addWidget(tabs)

        # set layout
        self.setLayout(self.vbox)

    # seet tab1 function
    def tab1_func(self):
        tab1 = QWidget()
        self.hbox = QHBoxLayout()  # if refresh delete widget in this layout

        leftlist = QListWidget()
        leftlist.setFixedWidth(150)
        Stack = QStackedWidget()
        # create widget in Stack with each leftlist name
        self.stack = {}
        for n in range(len(self.leftlist_name)):
            leftlist.insertItem(n, str(self.leftlist_name[n]))
            self.stack[n] = QWidget()
            Stack.addWidget(self.stack[n])

        # connect leftlist and Stack
        leftlist.currentRowChanged.connect(Stack.setCurrentIndex)

        # add widget in layout
        self.hbox.addWidget(leftlist)
        self.hbox.addWidget(Stack)

        # set tab1 layout
        tab1.setLayout(self.hbox)

        # go to set each leftlist name widget
        for n in range(len(self.leftlist_name)):
            self.stack_ui(n)

        return tab1

    # set each leftlist name ui
    def stack_ui(self, n):
        # create fig from MplFigure and add ax1
        self.main_fig = MplFigure(self)
        self.ax1 = self.main_fig.figure.add_subplot(111)

        # put fig to layout
        self.sbox = QHBoxLayout()
        self.sbox.addWidget(self.main_fig.canvas)

        # QThread part
        self.worker = plotThread(self.main_fig, self.ax1)
        self.worker.start()

        # set layout to each stack
        self.stack[n].setLayout(self.sbox)

    def tab2_func(self):
        tab2 = QWidget()
        return tab2

    def refresh_func(self):
        self.start = datetime.now()
        self.vbox.takeAt(1).widget().deleteLater()
        tabs = QTabWidget()
        tabs.addTab(self.tab1_func(), 'Tab1')
        tabs.addTab(self.tab2_func(), 'Tab2')

        self.vbox.addWidget(tabs)

        self.end = datetime.now()
        print(f"Refresh used time: {self.end - self.start}")
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.showMaximized()

    end = datetime.now()
    print(f"Time used: {end - start}")

    sys.exit(app.exec_())
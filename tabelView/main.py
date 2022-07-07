from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5 import QtWidgets as qt
import sys

class Main(qt.QMainWindow):
    def __init__(self):
        super().__init__()
        frame = qt.QFrame()
        self.setCentralWidget(frame)
        laymb = qt.QVBoxLayout(frame)
        model = QStandardItemModel()
        tabmb = TableViewClick()
        tabmb.setModel(model)
        tabmb.setGridStyle(Qt.PenStyle(0))
        tabmb.setSelectionMode(qt.QTableView.SelectionMode(1))
        tabmb.setSelectionBehavior(tabmb.SelectionBehavior(1))
        laymb.addWidget(tabmb)
        subj = [QStandardItem('Testing...') for _ in range(10)]
        model.appendColumn(subj)
        tabmb.signal.connect(self.tabled_clicked)

    def tabled_clicked(self):
        table = self.sender()
        indexes = table.selectedIndexes()
        print(indexes)


class TableViewClick(qt.QTableView):
    signal = pyqtSignal()

    def mousePressEvent(self, event):
        qt.QTableView.mousePressEvent(self, event)
        self.signal.emit()
        
app = qt.QApplication(sys.argv)
main_gui = Main()
main_gui.show()
sys.exit(app.exec())

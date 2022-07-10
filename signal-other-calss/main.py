import sys
from PySide6 import QtGui
from PySide6.QtWidgets import *
from PySide6.QtCore import Signal

class QCustomQWidget(QWidget):
    ask_set_new_text = Signal()
    def __init__(self, parent=None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQVBoxLayout = QVBoxLayout()
        self.textUpQLabel = QLabel()
        self.textDownQLabel = QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout = QHBoxLayout()
        self.iconQLabel = QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

        self.openButton = QPushButton()
        # self.openButton.setText("open")
        self.allQHBoxLayout.addWidget(self.openButton, 1)

    def setButton(self, index):
        self.openButton.setText(index)

    def connectButton(self): # <-----
        self.openButton.clicked.connect(lambda: self.ask_set_new_text.emit())

    def setTextUp(self, text):
        self.textUpQLabel.setText(text)

    def setTextDown(self, text):
        self.textDownQLabel.setText(text)

    def setIcon(self, imagePath):
        self.iconQLabel.setPixmap(QtGui.QPixmap(imagePath))


class exampleQMainWindow(QMainWindow):
    def __init__(self):
        super(exampleQMainWindow, self).__init__()

        # Create QListWidget
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.setCentralWidget(self.table)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setRowCount(6)
        for index, name, icon, btname in [
            (1, 'text1', 'g:\downloads\coffee-icon.png', "alpha"),
            (2, 'text2', 'g:\downloads\coffee-icon.png', "beta"),
            (3, 'text3', 'g:\downloads\coffee-icon.png', "gamma"),
            (4, 'text4', 'g:\downloads\coffee-icon.png', "delta")
            ]:
            # Create QCustomQWidget
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp(str(index))
            myQCustomQWidget.setTextDown(name)
            myQCustomQWidget.ask_set_new_text.connect(self.setNewText)
            #myQCustomQWidget.setIcon(icon) #just image can be ignored
            myQCustomQWidget.setButton(str(btname))
            myQCustomQWidget.button_row = index

            myQCustomQWidget.connectButton()# how to connect it to setNewText ?

            self.table.setCellWidget(index, 1, myQCustomQWidget)
            self.table.setRowHeight(index,90)

    def setNewText(self): # <----------
        print("test") 



app = QApplication(sys.argv)
window = exampleQMainWindow()
window.resize(800,512)
window.show()
sys.exit(app.exec())


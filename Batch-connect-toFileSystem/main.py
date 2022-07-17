from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QFileDialog,
    QFrame,
    QGridLayout,
    QLineEdit,
)
from PyQt5.QtCore import pyqtSlot
import sys
from functools import partial

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        top_frame = QFrame(self)
        self.setCentralWidget(top_frame)
        self.grid = QGridLayout(top_frame)
        for i in range(10):
            btn = QPushButton(top_frame)
            le = QLineEdit(top_frame)
            btn.clicked.connect(partial(self.open_dialog, le))
            btn.setText("open file system dialog")
            self.grid.addWidget(btn, i, 0)
            self.grid.addWidget(le, i, 1)

    @pyqtSlot(QLineEdit)
    def open_dialog(self, le: QLineEdit):
        file_name = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "${HOME}",
            "All Files (*)"
        )
        le.setText(file_name[0])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_gui = Main()
    main_gui.show()
    sys.exit(app.exec())

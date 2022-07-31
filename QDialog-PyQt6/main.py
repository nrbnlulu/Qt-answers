import sys

from PyQt6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton(self)
        btn.setText("Open file dialog")
        self.setCentralWidget(btn)
        btn.clicked.connect(lambda: self.open_dialog())

    def open_dialog(self):
        fname = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "${HOME}",
            "All Files (*);; Python Files (*.py);; PNG Files (*.png)",
        )
        print(fname)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_gui = Main()
    main_gui.show()
    sys.exit(app.exec())

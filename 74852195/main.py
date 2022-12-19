import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ExampleApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Example'
        self.left = 0
        self.top = 0
        self.width = 1000
        self.height = 800
        self.setMaximumWidth(1000)
        self.setMaximumHeight(800)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

        data = ["./mokey.png"] * 100

        self.picture_window = PictureWindow(self, data=data)
        self.setCentralWidget(self.picture_window)
        self.picture_window.show()


class PictureWindow(QWidget):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.n_columns = 5
        self.data = data

        self.gridLayout = QGridLayout()
        for i, filename in enumerate(self.data):
            self.render_picture(filename=filename, pos=i)

        self.setLayout(self.gridLayout)

    def render_picture(self, filename, pos):
        image_widget = QLabelClickable(pos)
        image_widget.setGeometry(15, 15, 118, 130)
        image_widget.setToolTip(filename)
        image_widget.setCursor(Qt.PointingHandCursor)

        self.pixmapImagen = QPixmap(filename).scaled(375, 375, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image_widget.setPixmap(self.pixmapImagen)
        image_widget.setAlignment(Qt.AlignCenter)

        cell_layout = QVBoxLayout()
        cell_layout.setAlignment(Qt.AlignHCenter)
        cell_layout.addWidget(image_widget)
        self.gridLayout.addLayout(cell_layout, int(pos / self.n_columns), pos % self.n_columns)


class QLabelClickable(QLabel):
    clicked = pyqtSignal(str)

    def __init__(self, id, parent=None):
        super(QLabelClickable, self).__init__(parent)
        self.id = id

    def mousePressEvent(self, event):
        self.ultimo = "Click"

    def mouseReleaseEvent(self, event):
        if self.ultimo == "Click":
            QTimer.singleShot(QApplication.instance().doubleClickInterval(),
                              self.performSingleClickAction)
        else:
            self.clicked.emit(self.ultimo + "-" + str(self.id))

    def mouseDoubleClickEvent(self, event):
        self.ultimo = "Double Click"

    def performSingleClickAction(self):
        if self.ultimo == "Click":
            self.clicked.emit(self.ultimo + "-" + str(self.id))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExampleApp()
    sys.exit(app.exec_())

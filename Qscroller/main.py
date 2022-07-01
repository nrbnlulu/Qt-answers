import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from pdf2image import convert_from_path
from pathlib import Path
import tempfile

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.scroll_area = QScrollArea()
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignCenter)
        self.main_widget.setLayout(self.main_layout)
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.showFullScreen()
        self.inner = QFrame()
        self.inner.setLayout(self.layout)
        self.scroll_area.setWidget(self.inner)
        self.main_layout.addWidget(self.scroll_area)
        self.setCentralWidget(self.main_widget)
        width = self.size().width()
        with tempfile.TemporaryDirectory() as path:
            pages = convert_from_path(str(Path(__file__).parent / 'ma_snake_guide.pdf'), 500, fmt="jpeg", output_folder=str(path), size=width*15)
            pages = pages[1:4]
            for page in pages:
                label = QLabel(self)
                pixmap = QPixmap(page.filename)
                label.setPixmap(pixmap)
                self.layout.addWidget(label)
        # Scroll Area Properties
        self.scroll_area.horizontalScrollBar().setEnabled(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroller = QScroller.scroller(self.scroll_area.viewport())
        self.scroller.grabGesture(self.scroll_area.viewport(), QScroller.LeftMouseButtonGesture)
        props = self.scroller.scrollerProperties()
        props.setScrollMetric(QScrollerProperties.FrameRate, QScrollerProperties.Fps60)
        props.setScrollMetric(QScrollerProperties.DecelerationFactor, 1)
        props.setScrollMetric(QScrollerProperties.DragVelocitySmoothingFactor, 0.4)
        props.setScrollMetric(QScrollerProperties.OvershootScrollTime, 0.4)
        props.setScrollMetric(QScrollerProperties.MaximumClickThroughVelocity, 0)
        props.setScrollMetric(QScrollerProperties.MinimumVelocity, 0.15)
        props.setScrollMetric(QScrollerProperties.MaximumVelocity, 0.6)
        props.setScrollMetric(QScrollerProperties.AcceleratingFlickMaximumTime, 0.3)
        self.scroller.setScrollerProperties(props)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    window = MainWindow()
    # Run the main Qt loop
    sys.exit(app.exec_())
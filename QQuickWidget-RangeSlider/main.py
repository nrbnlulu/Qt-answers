from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QFrame,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
)
from PyQt5.QtQuickWidgets import QQuickWidget
import sys
from PyQt5.QtCore import QUrl, pyqtSlot
from pathlib import Path


class Main(QMainWindow):
    @pyqtSlot(float)
    def set_from(self, from_: float):
        self.from_le.setText(str(from_))

    @pyqtSlot(float)
    def set_to(self, to: float):
        self.to_le.setText(str(to))

    def __init__(self):
        super().__init__()
        self.setFixedWidth(500)
        self.setFixedHeight(350)
        self.top_frame = QFrame(self)
        self.setCentralWidget(self.top_frame)
        self.top_layout = QVBoxLayout(self.top_frame)
        # Qt Widgets ...
        self.widgets = QFrame(self.top_frame)
        self.top_layout.addWidget(self.widgets)
        self.form = QFormLayout(self.widgets)
        self.from_le = QLineEdit()
        self.to_le = QLineEdit()
        self.form.addRow("From", self.from_le)
        self.form.addRow("To", self.to_le)
        # Qt Quick...
        self.qquick_widget = QQuickWidget(self.top_frame)
        self.top_layout.addWidget(self.qquick_widget)
        self.qquick_widget.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)
        self.qquick_widget.engine().rootContext().setContextProperty(
            "SomeNameForPythonBridge", self
        )
        self.qquick_widget.setSource(QUrl(str(Path(__file__).parent / "main.qml")))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_gui = Main()
    main_gui.show()
    sys.exit(app.exec())

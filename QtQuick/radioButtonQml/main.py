import sys
from os.path import abspath, dirname, join

from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine


class App(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_rb_text = ""

    @pyqtSlot(str)
    def set_current_rb_text(self, text: str):
        self.current_rb_text = text

    @pyqtSlot()
    def on_execute(self):
        print(self.current_rb_text)


app = QGuiApplication(sys.argv)
if __name__ == "__main__":
    # Reading the qml file
    engine = QQmlApplicationEngine()
    context = engine.rootContext()
    bridge = App()
    context.setContextProperty("App", bridge)
    qmlFile = join(dirname(__file__), "main.qml")
    engine.load(abspath(qmlFile))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())

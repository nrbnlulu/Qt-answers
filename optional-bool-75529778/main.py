import dataclasses
import random
import sys

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Signal

class Foo(QObject):
    tripleBoolChanged = Signal()
    def __init__(self):
        super().__init__(None)
        self._triple_bool: tuple[bool | None, bool | None, bool | None] = (None, None, None)
        self.tripleBoolChanged.connect(self.something_that_needs_triple_bool)

    def set_triple_bool(self, a: bool | None = None, b: bool | None = None, c: bool | None = None):
        self._triple_bool = a, b, c
        self.tripleBoolChanged.emit()
    def triple_bool(self):
        return self._triple_bool
    def something_that_needs_triple_bool(self):
       print(self.triple_bool())

class FooAlternative(QObject):
    @dataclasses.dataclass
    class TripleBool:
        a: bool | None = None
        b: bool | None = True
        c: bool | None = False


    tripleBoolChanged = Signal(TripleBool)

    def __init__(self):
        super().__init__(None)
        self.tripleBoolChanged.connect(self.something_that_needs_triple_bool)

    def emit_triple_bool(self, a: bool | None = None, b: bool | None = None, c: bool | None = None):
        tb = self.TripleBool(a, b, c)
        self.tripleBoolChanged.emit(tb)
    def something_that_needs_triple_bool(self, tb: TripleBool):

       print("foo alternative:", tb)



class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.foo = Foo()
        self.foo_alternative = FooAlternative()

        btn = QPushButton(self)
        btn.setText("Open file dialog")
        self.setCentralWidget(btn)
        btn.clicked.connect(lambda: self.foo.set_triple_bool(None, True, False))
        btn.clicked.connect(lambda: self.foo_alternative.emit_triple_bool(True, False, None))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_gui = Main()
    main_gui.show()
    sys.exit(app.exec())

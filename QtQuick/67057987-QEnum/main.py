import sys
from enum import Enum
from pathlib import Path

from PySide6.QtCore import Property, QEnum, QObject
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import (
    QmlElement,
    QQmlApplicationEngine,
    qmlRegisterSingletonInstance,
)

QML_IMPORT_NAME = "com.example.app"
QML_IMPORT_MAJOR_VERSION = 1


class Status(Enum):
    Connected, Disconnected, Stale = range(3)


@QmlElement
class Enums(QObject):
    QEnum(Status)


class App(QObject):
    def __init__(self):
        super().__init__(None)

    @Property(int, constant=True)
    def enumValue(self):
        return Status.Connected.value


if __name__ == "__main__":
    loop = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    app = App()
    qmlRegisterSingletonInstance(QObject, "com.example.app", 1, 0, "App", app)
    qml_file = Path(__file__).parent / "main.qml"
    engine.load(str(qml_file))

    sys.exit(loop.exec())

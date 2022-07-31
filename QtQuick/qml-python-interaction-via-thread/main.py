import random
import sys
from pathlib import Path

import cv2
import numpy as np
from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot
from PySide6.QtGui import QGuiApplication, QImage
from PySide6.QtQml import QmlElement, QQmlApplicationEngine
from pyzbar import pyzbar

QML_IMPORT_NAME = "com.myapp.components"
QML_IMPORT_MAJOR_VERSION = 1


class Worker(QRunnable):
    def __init__(self, emiter: Signal, image: QImage):
        super().__init__(None)
        self.image = image
        self.emiter = emiter

    def qimage_to_array(self, image: QImage) -> np.ndarray:
        """Converts a QImage into an opencv MAT format"""
        image = image.convertToFormat(QImage.Format.Format_RGBA8888)
        width = image.width()
        height = image.height()

        ptr = image.constBits()
        return np.array(ptr).reshape(height, width, 4)

    def run(self):
        arr = self.qimage_to_array(self.image)
        gray = cv2.cvtColor(arr, cv2.COLOR_BGR2GRAY)
        barcodes = pyzbar.decode(gray)
        # logic here.
        # returning now random boolean
        self.emiter.emit(random.choice([True, False]))


@QmlElement
class Cv2Capture(QObject):
    imageAnalayized = Signal(bool)

    @Slot(int, QImage)
    def receive(self, req_id, image: QImage):
        worker = Worker(self.imageAnalayized, image)
        QThreadPool.globalInstance().start(worker)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).parent / "main.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())

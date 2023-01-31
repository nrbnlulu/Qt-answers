import signal
import sys
from pathlib import Path

from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine, qmlRegisterSingletonInstance


class InstalledPkgsModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
        return None

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        try:
            return len(self._data[0])
        # If there are no installed mods in the prefix
        except IndexError:
            return 1


if __name__ == "__main__":
    # Make app respond to Ctrl-C
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    # engine.quit.connect(app.quit)  # type: ignore

    # Populate manage table view installed packages
    data = [
        ["git", "null", "common", "1.0"],
        ["distutils", "null", "common", "1.0"],
        ["bsa", "null", "common", "0.4"],
        ["nexus", "null", "common", "1.0"],
        ["fallout_4", " null", "common", "0.1"],
    ]
    installed_pkgs_model = InstalledPkgsModel(data)
    qmlRegisterSingletonInstance(
        "com.example.model", 1, 0, "InstalledPkgsModel", installed_pkgs_model
    )
    qml_file = Path(__file__).parent / "main.qml"
    engine.load(str(qml_file))

    sys.exit(app.exec())

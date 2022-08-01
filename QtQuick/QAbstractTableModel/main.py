import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QAbstractTableModel, Qt

class Model(QAbstractTableModel):
    def __init__(self):
        super().__init__(None)
        self._data = [
            [1,2,3,4,5,6,7,8,9,0],
            [1,2,3,4,5,6,7,8,9,0],
            [1,2,3,4,5,6,7,8,9,0],
            [1,2,3,4,5,6,7,8,9,0],
            [1,2,3,4,5,6,7,8,9,0],
            [1,2,3,4,5,6,7,8,9,0],
        ]

        self.header_labels = ["Name", "Use Flags", "Category", "Version"]
        
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]


    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        try:
            return len(self._data[0])
        # If there are no installed mods in the prefix
        except IndexError:
            return 1

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if (
            role == Qt.ItemDataRole.DisplayRole
            and orientation == Qt.Orientation.Horizontal
        ):
            return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)




if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    model = Model()
    engine.rootContext().setContextProperty('PyModel', model)
    qml_file = Path(__file__).parent / "main.qml"
    engine.load(qml_file)

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
    
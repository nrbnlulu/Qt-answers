import sys
from pathlib import Path

from PyQt5.QtCore import (
    QAbstractListModel,
    QModelIndex,
    QObject,
    Qt,
    pyqtProperty,
    pyqtSignal,
    pyqtSlot,
)
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine


class Backend(QObject):
    modelChanged = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._model = MyListModel()

    @pyqtProperty(QObject, constant=False, notify=modelChanged)
    def model(self):
        return self._model


class MyListModel(QAbstractListModel):
    NameRole = Qt.UserRole + 1000
    CollapsedRole = Qt.UserRole + 1001
    SubItemsRole = Qt.UserRole + 1002

    def __init__(self, parent=None):
        super().__init__()
        self.itemNames = []
        self.roles = {
            MyListModel.NameRole: b"assetName",
            MyListModel.SubItemsRole: b"subItems",
            MyListModel.CollapsedRole: b"isCollapsed",
        }

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.itemNames)

    def data(self, index, role=Qt.DisplayRole):
        if 0 <= index.row() < self.rowCount() and index.isValid():
            item = self.itemNames[index.row()]

            if role == MyListModel.NameRole:
                return item["assetName"]
            elif role == MyListModel.SubItemsRole:
                return item["subItems"]
            elif role == MyListModel.CollapsedRole:
                return item["isCollapsed"]
        return None

    def roleNames(self):

        return self.roles

    @pyqtSlot(str, bool)
    def appendRow(self, name, isCollapsed):
        self.subItem = MySubListModel()
        self.subItem.addRow()
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.itemNames.append(
            {"assetName": name, "subItems": self.subItem, "isCollapsed": isCollapsed}
        )
        self.endInsertRows()
        print(self.itemNames)
        print(self.subItem.subItemParams)

    @pyqtSlot(int, str)
    def collapseEditInputsMenu(self, index, modelIndexName):
        self.layoutAboutToBeChanged.emit()
        self.itemNames[index][modelIndexName] = not self.itemNames[index][
            modelIndexName
        ]
        print(f"From Backend: {self.itemNames}")
        self.layoutChanged.emit()


class MySubListModel(QAbstractListModel):
    CellSizeRole = Qt.UserRole + 1004

    def __init__(self, parent=None):
        super().__init__()
        self.subItemParams = []

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.subItemParams)

    def data(self, index, role=Qt.DisplayRole):
        if 0 <= index.row() < self.rowCount() and index.isValid():
            item = self.subItemParams[index.row()]

            if role == MySubListModel.CellSizeRole:
                return item["cellSize"]
        return None

    def roleNames(self):
        return {MySubListModel.CellSizeRole: b"cellSize"}

    def addRow(self):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.subItemParams.append({"cellSize": "888"})
        self.endInsertRows()


class MainWindow:
    def __init__(self):
        app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.engine.quit.connect(app.quit)
        self.engine.load(f"{str(Path(__file__).parent)}/main.qml")

        app_backend = Backend()
        self.engine.rootContext().setContextProperty("backendObjectInQML", app_backend)
        # self.engine.rootObjects()[0].setProperty("backendObjectInQML", app_backend)

        sys.exit(app.exec())


def main():
    MainWindow()


if __name__ == "__main__":
    main()

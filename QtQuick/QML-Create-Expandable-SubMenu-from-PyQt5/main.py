import sys
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import (
    QTimer,
    QObject,
    pyqtSignal,
    pyqtSlot,
    QAbstractListModel,
    QModelIndex,
    Qt,
    pyqtProperty,
)
from pathlib import Path


class Backend(QObject):
    modelChanged = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._model = MyListModel()

    ##~~Expose model as a property of our backend~~##
    @pyqtProperty(QObject, constant=False, notify=modelChanged)
    def model(self):
        return self._model


class MyListModel(QAbstractListModel):
    ##~~My Custom UserRoles~~##
    NameRole = Qt.UserRole + 1000
    CollapsedRole = Qt.UserRole + 1001
    SubItemsRole = Qt.UserRole + 1002

    def __init__(self, parent=None):
        super().__init__()
        self.itemNames = []

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

    def roleNames(self):
        roles = dict()
        roles[MyListModel.NameRole] = b"assetName"
        roles[MyListModel.SubItemsRole] = b"subItems"
        roles[MyListModel.CollapsedRole] = b"isCollapsed"
        return roles

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
    ##~~My Custom UserRole For SubItem ListModel~~##
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

    def roleNames(self):
        roles = dict()
        roles[MySubListModel.CellSizeRole] = b"cellSize"
        return roles

    def addRow(self):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.subItemParams.append({"cellSize": "888"})
        self.endInsertRows()


class MainWindow:
    def __init__(self):
        app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.engine.quit.connect(app.quit)
        self.engine.load(
            f"{str(Path(__file__).parent)}/main.qml"
        )

        app_backend = Backend()
        self.engine.rootContext().setContextProperty("backendObjectInQML", app_backend)
        # self.engine.rootObjects()[0].setProperty("backendObjectInQML", app_backend)

        sys.exit(app.exec())


def main():
    window = MainWindow()


if __name__ == "__main__":
    main()



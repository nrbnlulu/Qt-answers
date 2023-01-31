from tempfile import TemporaryDirectory

import pandas as pd
import requests
from PyQt5 import QtCore, QtWidgets

excel = requests.get(
    r"https://exinfm.com/excel%20files/capbudg.xls", allow_redirects=True
)
with TemporaryDirectory() as dir:
    with open(f"{dir}/excelFile.xlsx", "wb") as fh:
        fh.write(excel.content)

    class DataFrameModel(QtCore.QAbstractTableModel):
        DtypeRole = QtCore.Qt.UserRole + 1000
        ValueRole = QtCore.Qt.UserRole + 1001

        def __init__(self, df=pd.DataFrame(), parent=None):
            super().__init__(parent)
            self._dataframe = df

        def setDataFrame(self, dataframe):
            self.beginResetModel()
            self._dataframe = dataframe.copy()
            self.endResetModel()

        def dataFrame(self):
            return self._dataframe

        dataFrame = QtCore.pyqtProperty(pd.DataFrame, fget=dataFrame, fset=setDataFrame)

        @QtCore.pyqtSlot(int, QtCore.Qt.Orientation, result=str)
        def headerData(
            self,
            section: int,
            orientation: QtCore.Qt.Orientation,
            role: int = QtCore.Qt.DisplayRole,
        ):
            if role == QtCore.Qt.DisplayRole:
                if orientation == QtCore.Qt.Horizontal:
                    return self._dataframe.columns[section]
                else:
                    return str(self._dataframe.index[section])
            return QtCore.QVariant()

        def rowCount(self, parent=QtCore.QModelIndex()):
            if parent.isValid():
                return 0
            return len(self._dataframe.index)

        def columnCount(self, parent=QtCore.QModelIndex()):
            if parent.isValid():
                return 0
            return self._dataframe.columns.size

        def data(self, index, role=QtCore.Qt.DisplayRole):
            if not index.isValid() or not (
                0 <= index.row() < self.rowCount()
                and 0 <= index.column() < self.columnCount()
            ):
                return QtCore.QVariant()
            row = self._dataframe.index[index.row()]
            col = self._dataframe.columns[index.column()]
            dt = self._dataframe[col].dtype

            val = self._dataframe.iloc[row][col]
            if role == QtCore.Qt.DisplayRole:
                return str(val)
            elif role == DataFrameModel.ValueRole:
                return val
            if role == DataFrameModel.DtypeRole:
                return dt
            return QtCore.QVariant()

        def roleNames(self):
            roles = {
                QtCore.Qt.DisplayRole: b"display",
                DataFrameModel.DtypeRole: b"dtype",
                DataFrameModel.ValueRole: b"value",
            }
            return roles

    class Ui_MainWindow:
        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(662, 512)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.verticalLayout = QtWidgets.QVBoxLayout()
            self.verticalLayout.setObjectName("verticalLayout")
            self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit.setText(f"{dir}/excelFile.xlsx")
            self.lineEdit.setObjectName("lineEdit")
            self.verticalLayout.addWidget(self.lineEdit)
            self.tableView = QtWidgets.QTableView(self.centralwidget)
            self.tableView.setObjectName("tableView")
            self.verticalLayout.addWidget(self.tableView)
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setObjectName("pushButton")
            self.verticalLayout.addWidget(self.pushButton)
            self.horizontalLayout.addLayout(self.verticalLayout)
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 21))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.pushButton.setText(_translate("MainWindow", "PushButton"))

            self.pushButton.clicked.connect(self.btn_clk)

            MainWindow.show()

        def btn_clk(self):
            path = self.lineEdit.text()  # noqa
            df = pd.read_excel(f"{dir}/excelFile.xlsx")
            model = DataFrameModel(df)
            self.tableView.setModel(model)

    if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

connection = sqlite3.connect("main.db")
cu = connection.cursor()


def loadui():
    return None


class mainapp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadui("main.ui", self)
        self.pages.setCurrentIndex(0)
        self.labelShow.setWordWrap(True)

        self.menuFrame.move(1100, 0)
        self.menuFrame_2.move(1100, 0)
        self.show_items()

    def show_items(self):
        cu.execute("SELECT * FROM notes ")
        all = cu.fetchall()
        count = 1
        height = 0
        for i in all:
            main_height = height + 120
            # print(i)
            print(type(i[0]))
            exec("nameInfo" + (str(count)) + " =" + "(str(i[0]))" + "")
            # print(eval("nameInfo"+(str(count))))
            exec("self.pushButton = QtWidgets.QPushButton(self.infoFrame)")
            eval("self.pushButton.setGeometry(QtCore.QRect(10, height, 655, 110))")
            eval("self.pushButton.setMinimumSize(QtCore.QSize(655, 110))")
            eval("self.pushButton.setMaximumSize(QtCore.QSize(200, 110))")
            eval("self.pushButton.setStyleSheet(push_style)")
            eval("self.pushButton.setText(nameInfo" + (str(count)) + ")")
            exec(
                "self.pushButton.clicked.connect(lambda: self.show_Id(nameInfo"
                + "(str(count))"
                + "))"
            )
            self.pushButton.setObjectName("pushButton")

            # self.verticalLayout.addWidget(self.infoFrame)
            height = height + 130
            print(height)
            count = count + 1
        # self.infoFrame.setMaximumHeight(main_height)
        self.infoFrame.setMinimumHeight(main_height)

    def show_Id(self, name):
        print(name)


app = QApplication(sys.argv)
calculator_app = mainapp()
calculator_app.show()

sys.exit(app.exec_())

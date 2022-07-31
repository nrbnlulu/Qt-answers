import sys

from gql import Client, gql
from gql.transport.websockets import WebsocketsTransport
from graphql import subscribe
from PySide6 import QtCore as qtc
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class SendQueryWorker(qtc.QRunnable):
    """
    sends requests to the server
    and returns result as dict
    to the notifier supplied
    flags will modify the data as necessary
    """

    def __init__(self, signal: qtc.Signal):
        super().__init__()
        self.signal = signal

    def run(self):
        print("Subscribing...")
        transport = WebsocketsTransport(url="ws://127.0.0.1:8000/graphql")
        client = Client(
            transport=transport,
            fetch_schema_from_transport=False,
        )

        query = gql(
            """
            subscription MySubscription {
            alerts {
                name
                isMuted
                units{
                unitType
                }
            }

            }
        """
        )

        for result in client.subscribe(query):
            self.signal.emit(result)


class Main(QMainWindow):
    test = qtc.Signal(dict)

    def __init__(self):
        super().__init__()
        btn = QPushButton(self)
        btn.setText("Open file dialog")
        self.setCentralWidget(btn)
        btn.clicked.connect(lambda: subscribe(self.test))
        self.test.connect(self.recevier)

    @qtc.Slot(dict)
    def recevier(self, res: dict):
        print(res)


def subscribe(signal: qtc.Signal) -> None:
    """sends query and returns a dict|df to receiver"""
    worker = SendQueryWorker(signal)
    qtc.QThreadPool.globalInstance().start(worker)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec()

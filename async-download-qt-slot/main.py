import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Slot, QThreadPool, QObject, Signal, QRunnable

import concurrent.futures
import urllib.request




URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',]

async def work():
    # Retrieve a single page and report the URL and contents
    def load_url(url, timeout):
        with urllib.request.urlopen(url, timeout=timeout) as conn:
            return conn.read()

    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.start_btn = QPushButton("Start")
        self.start_btn.pressed.connect(self.startLog)
        self.setCentralWidget(self.start_btn)

    def startLog(self):
        work()

    @Slot(int, str)
    def updateLogData(self, loop: int, delta: str):
        print(loop, delta)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
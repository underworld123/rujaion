import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Many of source is copied from https://qiita.com/montblanc18/items/88d0b639de86b7cac613


class CustomWebEngineView(QWebEngineView):
    def contextMenuEvent(self, a0: QtGui.QContextMenuEvent) -> None:
        menu = QtWidgets.QMenu()
        menu.addAction(u"Download This Task", self.parent().download_task)
        menu.exec(a0.globalPos())


class WebViewWindow(QtWidgets.QWidget):
    def __init__(self, parent=None, *args):
        super().__init__(parent, *args)
        self.url = ""
        self.browser = CustomWebEngineView(self)
        self.browser.resize(1000, 600)
        self.browser.setWindowTitle("Task")
        self.url_edit = QtWidgets.QLineEdit()
        self.url_edit.returnPressed.connect(self.loadPage)

        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.url_edit, 0, 0, 1, 15)
        grid.addWidget(self.browser, 1, 0, 5, 15)
        self.setLayout(grid)
        self.resize(500, 800)

    def download_task(self):
        self.url_edit.setText(self.browser.url().toString())
        self.parent().parent().download(self.url)

    def loadPage(self):
        if self.url_edit.text():
            self.browser.load(QUrl(self.url_edit.text()))

    def changePage(self, url):
        self.url_edit.setText(url)
        self.loadPage()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = WebViewWindow()
    sys.exit(app.exec_())

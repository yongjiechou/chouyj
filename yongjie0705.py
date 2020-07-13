import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel("標籤怎麼居中顯示", self)
        dsk = app.desktop()
        print(dsk.width(), dsk.height(), self.width())
        # lbl.resize(200, 300)
        self.move((dsk.width() / 2 - self.width() / 2), 50)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mc = MyClass()
    sys.exit(app.exec_())

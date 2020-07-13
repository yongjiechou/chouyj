import sys
from PyQt5.QtWidgets import QApplication, QWidget
# 空白視窗建立

class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mc = MyClass()
    sys.exit(app.exec_())

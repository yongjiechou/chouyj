import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("第一個視窗")
        self.setGeometry(30, 40, 300, 200)

        btn = QPushButton("第一個按鈕", self)
        btn.move(50, 50)
        # 點按鈕關閉視窗
        btn.clicked.connect(self.close)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mc = MyClass()
    sys.exit(app.exec_())

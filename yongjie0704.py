import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("第一個視窗")
        self.setGeometry(300, 200, 300, 200)

        btn = QPushButton("關閉視窗", self)
        btn.move(50, 50)
        # 點按鈕提示視窗
        # 詢問是否執行關閉視窗
        btn.clicked.connect(self.close)

        self.show()

    def closeEvent(self, event):
        result = QMessageBox.question(self, "QQ@@:", "real close?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            QMessageBox.information(self, "info", "thx go on")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mc = MyClass()
    sys.exit(app.exec_())

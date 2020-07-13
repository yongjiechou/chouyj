import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


# 註冊視窗
class ResultClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("result")
        self.size(300, 200)
        lbltest = QLabel("OK", self)

        self.show()


class MyClass(QWidget):
    def __init__(self):
        super(MyClass, self).__init__()
        # self.rc = 0
        self.initUI()


    def initUI(self):
        self.setWindowTitle("hihi")
        self.resize(400, 200)

        wlbl = QLabel("歡迎光臨", self)

        vlo = QVBoxLayout(self)
        vlo.addWidget(wlbl, 0, Qt.AlignCenter)
        vlo.setAlignment(Qt.AlignTop)

        frm1 = QFormLayout(self)

        lblf = QLabel("手機號碼", self)
        letel = QLineEdit(self)
        frm1.addRow(lblf, letel)

        lblpwd = QLabel("密碼", self)
        lepwd = QLineEdit(self)
        lepwd.setEchoMode(QLineEdit.Password)
        frm1.addRow(lblpwd, lepwd)
        vlo.addLayout(frm1)

        btn = QPushButton("註冊", self)
        btn.clicked.connect(self.btn_click)
        vlo.addWidget(btn)
        self.show()

    def btn_click(self):
        rc = ResultClass()
        list1.append(rc)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mc = MyClass()
    list1 = []
    sys.exit(app.exec_())

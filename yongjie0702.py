import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont

if __name__ == "__main__":
    app = QApplication(sys.argv)

    QToolTip.setFont(QFont('', 20))

    w = QWidget()
    w.setWindowTitle("周雍傑")
    w.setWindowIcon(QIcon(r'C:\ATM\sun.png'))
    w.setToolTip("show something")

    btn = QPushButton("HI! hit me", w)
    btn.move(50, 50)
    btn.setToolTip("hi")

    w.show()
    sys.exit(app.exec_())

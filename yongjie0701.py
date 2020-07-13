import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)
app.setWindowIcon(QIcon(r"C:\ATM\cross.png"))
w = QWidget()
w.setWindowTitle("周雍傑sun")
w.setWindowIcon(QIcon(r"C:\ATM\sun.png"))
w.show()
w1 = QWidget()
w1.setWindowTitle("周雍傑fun")
w1.setWindowIcon(QIcon(r"C:\ATM\fun.png"))
w1.show()
w2 = QWidget()
w2.setWindowTitle("周雍傑all")
w2.show()

app.exec_()

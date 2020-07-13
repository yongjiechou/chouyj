import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from functools import partial #import partial

def window():
   app = QApplication(sys.argv)
   win = QWidget()
   grid = QGridLayout()
   dict =[]

   for i in range(0,9):
      for j in range(0,9):
         k = QPushButton(str(i+1)+"*"+str(j+1))
         grid.addWidget(k,i,j)
         print(k)
         k.clicked.connect(partial(showMessage,i,j)) #呼叫showMessage 並帶入i, j


   win.setLayout(grid)
   win.setWindowTitle("PyQt Grid Example")
   win.setGeometry(50,50,200,200)
   win.show()
   sys.exit(app.exec_())

def showMessage(i,j):
    x=(i+1)*(j+1)
    msgBox = QMessageBox()

    msgBox.setText("{} * {}= {}".format(str(i+1),str(j+1),str(x)))
    msgBox.setWindowTitle("Signal & Slot ")
    msgBox.setStandardButtons(QMessageBox.Ok)
    # msgBox.buttonClicked.connect(msgButtonClick)
    msgBox.exec()
    msgBox.show()


if __name__ == '__main__':
   window()
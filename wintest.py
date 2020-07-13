#-*- coding = utf-8 -*-
#@Time : 2020/7/13 上午 09:48
#@Author: YJ
#@File : wintest.py
#@Software:PyCharm
import sys
from  UI.test import Ui_MainWindow
from PyQt5 import QtCore,QtGui,Qt,QtWidgets

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    mywindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(mywindow)
    mywindow.show()
    sys.exit(app.exec_())
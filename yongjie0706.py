import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDoubleSpinBox, QSpinBox, QHBoxLayout
from PyQt5.QtCore import Qt

'''
建立視窗
'''


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("hihi")
        self.resize(400, 200)
        hlo = QHBoxLayout(self)
        sb = QSpinBox(self)
        sb.setRange(-10, 10)
        sb.setPrefix("物品 ")
        sb.setSuffix(" 件")

        hlo.addWidget(sb)
        dsb = QDoubleSpinBox(self)
        dsb.setRange(0, 10)
        dsb.setPrefix("單價 ")
        dsb.setSuffix(" 元")
        # spin step setting=0.05,只能設定為整數
        dsb.setSingleStep(0.05)
        hlo.addWidget(dsb)
        hlo.setAlignment(Qt.AlignTop)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mc = MyClass()
    sys.exit(app.exec_())

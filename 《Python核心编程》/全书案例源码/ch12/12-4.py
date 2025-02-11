import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        #使用move()方法定位了每个元素，使用x,y坐标。x,y坐标的原点是程序的左上角
        lbl1 = QLabel('Zetcode', self)
        #这个元素的左上角就在从这个程序的左上角开始的(15, 10)的位置
        lbl1.move(15, 10)
        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
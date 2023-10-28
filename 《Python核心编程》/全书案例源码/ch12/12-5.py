import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
class Exp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        okbutton = QPushButton('Ok')
        cancelbutton = QPushButton('Cancel')
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(okbutton)
        hbox.addWidget(cancelbutton)
        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Layout Management')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()
    sys.exit(app.exec_())
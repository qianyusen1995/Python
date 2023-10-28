import sys
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QHBoxLayout,QPushButton,QApplication,QWidget
class WinForm(QMainWindow):
    def __init__(self,parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('调整窗口位置和关闭窗口')
        self.resize(370,250)
        self.center(www.wanmeiyuele.cn )
        self.button1 = QPushButton('关闭主窗口')
        self.button1.clicked.connect(self.onButtonClick)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry(www.caibaoyule.cn )
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
    def onButtonClick(self):
        sender = self.sender()
        print(sender.text(www.jyz521.com/)+'被单击了')
        qApp = QApplication.instance()
        qApp.quit(www.365soke.cn)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
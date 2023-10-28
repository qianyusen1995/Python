self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.pushButton = QtWidgets.QPushButton(self.centralwidget)
    self.pushButton.setGeometry(QtCore.QRect(610, 440, 131, 71))
#对“开始作诗”按钮进行设置
    self.pushButton.setObjectName("pushButton")
    self.label = QtWidgets.QLabel(self.centralwidget)
    self.label.setGeometry(QtCore.QRect(100, 20, 91, 61))
#对输入古诗标题标签进行设置
    self.label.setObjectName("label")
    self.label_2 = QtWidgets.QLabel(self.centralwidget)
    self.label_2.setGeometry(QtCore.QRect(110, 150, 91, 61))
#对五言绝句标签进行设置
    self.label_2.setObjectName("label_2")
    self.label_3 = QtWidgets.QLabel(self.centralwidget)
    self.label_3.setGeometry(QtCore.QRect(110, 310, 121, 41))
#对七言绝句标签进行设置
    self.label_3.setObjectName("label_3")
    self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
    self.textEdit.setGeometry(QtCore.QRect(230, 20, 271, 51))
#对古诗标题输入框进行设置
    self.textEdit.setObjectName("textEdit")
    self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
    self.textEdit_2.setGeometry(QtCore.QRect(230, 120, 291, 111))
#对五言绝句输出框进行设置
    self.textEdit_2.setObjectName("textEdit_2")
    self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
    self.textEdit_3.setGeometry(QtCore.QRect(230, 290, 301, 111))
#对七言绝句输出框进行设置
    self.textEdit_3.setObjectName("textEdit_3")
    MainWindow.setCentralWidget(self.centralwidget)
    self.menubar = QtWidgets.QMenuBar(MainWindow)
    self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
#自动生成的函数，用来设置窗体中控件的默认值
def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    #设置窗体标题
    MainWindow.setWindowTitle(_translate("MainWindow", "python下的智能写诗"))
    self.pushButton.setText(_translate("MainWindow", "开始作诗"))
    self.label.setText(_translate("MainWindow", "输入古诗标题"))
    self.label_2.setText(_translate("MainWindow", "五言绝句"))
    self.label_3.setText(_translate("MainWindow", "七言绝句"))
from PyQt5 import QtCore, QtGui, QtWidgets
import mrz, unidecode

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 360)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 2, 1, 1)

        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 6, 2, 1, 1)

        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 6, 1, 1, 1)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 7, 1, 1, 1)

        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setMaximum(99999)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        # ADD ở Đây
        self.soke = QtWidgets.QLabel(self.groupBox)
        self.soke.setText('4 số kế')
        self.soke.setObjectName("4soke")
        self.horizontalLayout.addWidget(self.soke)
        self.spinBox_22 = QtWidgets.QLineEdit(self.groupBox)
        intValidator = QtGui.QIntValidator(0, 999999999, self)
        self.spinBox_22.setValidator(intValidator)
        self.spinBox_22.setPlaceholderText('4 số kế')
        self.spinBox_22.setObjectName("spinBox_22")
        self.horizontalLayout.addWidget(self.spinBox_22)
        self.spinBox_22.setMinimumSize(100, 50)
        # Đến Đây
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setMaximum(999999999)
        self.spinBox_2.setProperty("value", 8888)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout.addWidget(self.spinBox_2)
        self.spinBox_2.setMinimumSize(200, 50)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 3, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 4, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 5, 2, 1, 1)

        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 7, 2, 1, 1)


        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setStyleSheet(".QPushButton{background-color: rgb(0, 170, 255); width: 200px; height: 35px}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 9, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setStyleSheet(".QPushButton{background-color: rgb(255, 255, 127); width: 200px; height: 35px}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setStyleSheet(".QPushButton{background-color: rgb(85, 170, 127); width: 200px; height: 35px}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MRZ "))
        self.groupBox.setTitle(_translate("MainWindow", "Single"))
        self.label.setText(_translate("MainWindow", "Tên đầy đủ:"))
        self.pushButton_5.setText(_translate("MainWindow", "Copy"))
        self.pushButton_11.setText(_translate("MainWindow", "Copy"))
        self.label_11.setText(_translate("MainWindow", "Tên:"))
        self.pushButton_6.setText(_translate("MainWindow", "Copy"))
        self.label_2.setText(_translate("MainWindow", "Mã:"))
        self.label_5.setText(_translate("MainWindow", "3 số đầu"))
        self.label_7.setText(_translate("MainWindow", "Số thứ 4"))
        self.label_12.setText(_translate("MainWindow", "số còn lại"))
        self.pushButton_7.setText(_translate("MainWindow", "Copy"))
        self.label_3.setText(_translate("MainWindow", "Ngày sinh:"))
        self.pushButton_8.setText(_translate("MainWindow", "Copy"))
        self.label_4.setText(_translate("MainWindow", "Ngày hết hạn:"))
        self.pushButton_9.setText(_translate("MainWindow", "Copy"))
        self.label_6.setText(_translate("MainWindow", "Giới tính (Sex):"))
        self.label_8.setText(_translate("MainWindow", "Quê quán:"))
        self.label_9.setText(_translate("MainWindow", "Thường trú:"))
        self.pushButton.setText(_translate("MainWindow", "Nam"))
        self.pushButton_10.setText(_translate("MainWindow", "Copy"))
        self.pushButton_12.setText(_translate("MainWindow", "Copy"))
        self.pushButton_4.setText(_translate("MainWindow", "Get"))
        self.pushButton_2.setText(_translate("MainWindow", "Copy thông tin mặt trước"))
        self.pushButton_3.setText(_translate("MainWindow", "Copy thông tin mặt sau"))
        #############################################################################
        self.pushButton.clicked.connect(lambda _: self.pushButton.setText('Nữ' if self.pushButton.text()=='Nam' else 'Nam'))
        self.lineEdit.textChanged.connect(lambda _: self.lineEdit_2.setText(unidecode.unidecode(self.lineEdit.text())))
        self.dateEdit.dateChanged.connect(lambda _: self.dateEdit_2.setDate(QtCore.QDate(self.dateEdit_2.date().year(), self.dateEdit.date().month(), self.dateEdit.date().day())))
        self.Main=Main(self)
        self.Main.Show.connect(self.Show)
        self.pushButton_4.clicked.connect(self.Single_Get)
        self.spinBox_2.valueChanged.connect(self.updateDate)
        self.previousValue=self.spinBox_2.value()
        self.pushButton_2.clicked.connect(self.CreateCccd)
        self.pushButton_3.clicked.connect(self._Copy)
        self.pushButton_5.clicked.connect(lambda _: QtWidgets.QApplication.clipboard().setText(self.lineEdit.text()))
        self.pushButton_6.clicked.connect(lambda _: QtWidgets.QApplication.clipboard().setText(self.lineEdit_2.text()))
        self.pushButton_11.clicked.connect(lambda _: QtWidgets.QApplication.clipboard().setText(self.lineEdit_4.text()))
        self.pushButton_12.clicked.connect(lambda _: QtWidgets.QApplication.clipboard().setText(self.lineEdit_5.text()))
        self.pushButton_7.clicked.connect(lambda _: QtWidgets.QApplication.clipboard().setText(f'{self.lineEdit_3.text()}{self.spinBox.value()}{self.spinBox_22.text()}{self.spinBox_2.value()}'))
        self.pushButton_8.clicked.connect(lambda _: QtWidgets.QApplication.clipboard().setText(self.dateEdit.date().toPyDate().strftime(r'%d/%m/%Y')))
        self.pushButton_9.clicked.connect(lambda _: QtWidgets.QApplication.clipboard().setText(self.dateEdit_2.date().toPyDate().strftime(r'%d/%m/%Y')))
        self.pushButton_10.clicked.connect(lambda _: QtWidgets.QApplication.clipboard().setText(self.pushButton.text()))
    def updateDate(self, value):
        current_date=self.dateEdit.date()
        delta = QtCore.QDate(current_date)
        if value>self.previousValue:
            delta=delta.addDays(1)
        elif value<self.previousValue:
            delta=delta.addDays(-1)
        self.dateEdit.setDate(delta)
        self.previousValue=value
    def Copy(self):
        QtWidgets.QApplication.clipboard().setText('{}\n\n{}\n\n{}\n\n{}\n\n{}'.format(f'{self.lineEdit_3.text()}{self.spinBox.value()}{self.spinBox_22.text()}{self.spinBox_2.value()}', self.lineEdit.text(), self.dateEdit.date().toPyDate().strftime(r'%d/%m/%Y'), self.pushButton.text(), self.dateEdit_2.date().toPyDate().strftime(r'%d/%m/%Y')))
    def _Copy(self):
        QtWidgets.QApplication.clipboard().setText(self.plainTextEdit.toPlainText())
    def Show(self, text):
        self.plainTextEdit.setPlainText(text)
    def Single_Get(self):
        self.Main.mode='Single'
        self.Main.start()
    def CreateCccd(self):
        res = '{}\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}'.format(f'{self.lineEdit_3.text()}{self.spinBox.value()}{self.spinBox_22.text()}{self.spinBox_2.value()}', self.lineEdit.text(), self.dateEdit.date().toPyDate().strftime(r'%d/%m/%Y'), self.pushButton.text(), self.dateEdit_2.date().toPyDate().strftime(r'%d/%m/%Y'), self.lineEdit_4.text(), self.lineEdit_5.text(), self.plainTextEdit.toPlainText())
        
        data = res.split('\n\n')
        
        import test
        test.createCCcd("./rotated_image.jpg", "./mat_sau.jpg", data)


        # print(data)

class Main(QtCore.QThread):
    Show=QtCore.pyqtSignal(str)
    def __init__(self, all) -> None:
        super().__init__()
        self.all=all
        self.mode='Single'
        self.Datas=[]
    def run(self):
        if self.mode=='Single':
            ma, ten, ngay_sinh, ngay_het_han, gioi_tinh=f'{self.all.lineEdit_3.text()}{self.all.spinBox.value()}{self.all.spinBox_22.text()}{self.all.spinBox_2.value()}', self.all.lineEdit_2.text(), self.all.dateEdit.date().toPyDate().strftime(r'%d/%m/%Y'), self.all.dateEdit_2.date().toPyDate().strftime(r'%d/%m/%Y'), self.all.pushButton.text()
            text='{}\n'.format(mrz.generate_mrz_string(ma, ten, ngay_sinh, ngay_het_han, gioi_tinh))
            self.Show.emit(text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

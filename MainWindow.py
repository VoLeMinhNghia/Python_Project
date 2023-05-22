# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from functools import partial

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.KhoaBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.KhoaBtn.setGeometry(QtCore.QRect(90, 300, 151, 81))
        self.KhoaBtn.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"selection-background-color: rgb(209, 209, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.KhoaBtn.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Vietnamese, QtCore.QLocale.Country.Vietnam))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/khoa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.KhoaBtn.setIcon(icon)
        self.KhoaBtn.setIconSize(QtCore.QSize(50, 50))
        self.KhoaBtn.setObjectName("KhoaBtn")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 271))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/banner.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.NganhBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.NganhBtn.setGeometry(QtCore.QRect(320, 300, 151, 81))
        self.NganhBtn.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"selection-background-color: rgb(0, 116, 170);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.NganhBtn.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Vietnamese, QtCore.QLocale.Country.Vietnam))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/nghanh.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.NganhBtn.setIcon(icon1)
        self.NganhBtn.setIconSize(QtCore.QSize(50, 50))
        self.NganhBtn.setObjectName("NganhBtn")
        self.LopBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.LopBtn.setGeometry(QtCore.QRect(560, 300, 151, 81))
        self.LopBtn.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"selection-background-color: rgb(135, 68, 203);\n"
"font: 10pt \"Segoe UI\";")
        self.LopBtn.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Vietnamese, QtCore.QLocale.Country.Vietnam))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/lop.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.LopBtn.setIcon(icon2)
        self.LopBtn.setIconSize(QtCore.QSize(50, 50))
        self.LopBtn.setObjectName("LopBtn")
        self.NienKhoaBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.NienKhoaBtn.setGeometry(QtCore.QRect(90, 420, 151, 81))
        self.NienKhoaBtn.setStyleSheet("background-color: rgb(202, 135, 202);\n"
"selection-background-color: rgb(211, 141, 211);\n"
"font: 10pt \"Segoe UI\";")
        self.NienKhoaBtn.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Vietnamese, QtCore.QLocale.Country.Vietnam))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/nienkhoa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.NienKhoaBtn.setIcon(icon3)
        self.NienKhoaBtn.setIconSize(QtCore.QSize(50, 50))
        self.NienKhoaBtn.setObjectName("NienKhoaBtn")
        self.HocKyBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.HocKyBtn.setGeometry(QtCore.QRect(320, 420, 151, 81))
        self.HocKyBtn.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"selection-background-color: rgb(207, 138, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.HocKyBtn.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Vietnamese, QtCore.QLocale.Country.Vietnam))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/hocky.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.HocKyBtn.setIcon(icon4)
        self.HocKyBtn.setIconSize(QtCore.QSize(50, 50))
        self.HocKyBtn.setObjectName("HocKyBtn")
        self.MonHocBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.MonHocBtn.setGeometry(QtCore.QRect(560, 420, 151, 81))
        self.MonHocBtn.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"selection-background-color: rgb(108, 216, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.MonHocBtn.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Vietnamese, QtCore.QLocale.Country.Vietnam))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/mon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.MonHocBtn.setIcon(icon5)
        self.MonHocBtn.setIconSize(QtCore.QSize(50, 50))
        self.MonHocBtn.setObjectName("MonHocBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.KhoaBtn.clicked.connect(partial(self.showQuanLyKhoa, MainWindow))
        self.NganhBtn.clicked.connect(partial(self.showQuanLyNghanh, MainWindow))
        self.LopBtn.clicked.connect(partial(self.showQuanLyLop, MainWindow))
        self.NienKhoaBtn.clicked.connect(partial(self.showQuanLyNienKhoa, MainWindow))
        self.HocKyBtn.clicked.connect(partial(self.showQuanLyHocKy, MainWindow))
        self.MonHocBtn.clicked.connect(partial(self.showQuanLyMon, MainWindow))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showQuanLyKhoa(self, MainWindow):
        from QuanLyKhoa import Ui_QuanLyKhoa as Ui_QuanLyKhoa
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_QuanLyKhoa()
        self.ui.setupUi(self.window)
        MainWindow.close()
        self.window.show()

    def showQuanLyNghanh(self, MainWindow):
        from QuanLyNghanh import Ui_QuanLyNghanh as Ui_QuanLyNghanh
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_QuanLyNghanh()
        self.ui.setupUi(self.window)
        MainWindow.close()
        self.window.show()

    def showQuanLyLop(self, MainWindow):
        from QuanLyLop import Ui_MainWindow as Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.close()
        self.window.show()

    def showQuanLyNienKhoa(self, MainWindow):
        from QuanLyNienKhoa import Ui_MainWindow as Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.close()
        self.window.show()

    def showQuanLyHocKy(self, MainWindow):
        from QuanLyHocKy import Ui_MainWindow as Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.close()
        self.window.show()

    def showQuanLyMon(self, MainWindow):
        from QuanLyMon import Ui_MainWindow as Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.close()
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ứng Dụng Quản Lý"))
        self.KhoaBtn.setText(_translate("MainWindow", "Quản Lý Khoa"))
        self.NganhBtn.setText(_translate("MainWindow", "Quản Lý Nghành"))
        self.LopBtn.setText(_translate("MainWindow", "Quản Lý\nSinh Viên"))
        self.NienKhoaBtn.setText(_translate("MainWindow", "Niên Khóa"))
        self.HocKyBtn.setText(_translate("MainWindow", "Học Kỳ"))
        self.MonHocBtn.setText(_translate("MainWindow", "Môn Học"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
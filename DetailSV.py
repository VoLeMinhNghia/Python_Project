# Form implementation generated from reading ui file 'DetailSV.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 308)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.label.setStyleSheet("font: 700 12pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 40, 49, 16))
        self.label_2.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label_3.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_3.setObjectName("label_3")
        self.detailIDSV = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.detailIDSV.setGeometry(QtCore.QRect(110, 40, 101, 22))
        self.detailIDSV.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.detailIDSV.setReadOnly(True)
        self.detailIDSV.setObjectName("detailIDSV")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 51, 16))
        self.label_4.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_4.setObjectName("label_4")
        self.detailNameSV = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.detailNameSV.setGeometry(QtCore.QRect(110, 80, 131, 22))
        self.detailNameSV.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.detailNameSV.setReadOnly(False)
        self.detailNameSV.setObjectName("detailNameSV")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 80, 71, 21))
        self.label_5.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_5.setObjectName("label_5")
        self.dateOfB = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateOfB.setGeometry(QtCore.QRect(340, 80, 131, 22))
        self.dateOfB.setReadOnly(False)
        self.dateOfB.setObjectName("dateOfB")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 51, 16))
        self.label_6.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_6.setObjectName("label_6")
        self.cbBoxSex = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbBoxSex.setGeometry(QtCore.QRect(110, 120, 69, 22))
        self.cbBoxSex.setObjectName("cbBoxSex")
        self.cbBoxSex.addItem("")
        self.cbBoxSex.addItem("")
        self.cbBoxSex.addItem("")
        self.fontComboBox = QtWidgets.QFontComboBox(parent=self.centralwidget)
        self.fontComboBox.setGeometry(QtCore.QRect(40, 300, 209, 22))
        self.fontComboBox.setObjectName("fontComboBox")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(270, 120, 51, 16))
        self.label_7.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_7.setObjectName("label_7")
        self.detailDanToc = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.detailDanToc.setGeometry(QtCore.QRect(340, 120, 131, 22))
        self.detailDanToc.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.detailDanToc.setReadOnly(False)
        self.detailDanToc.setObjectName("detailDanToc")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 160, 51, 16))
        self.label_8.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_8.setObjectName("label_8")
        self.plainTextEditDiaChi = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEditDiaChi.setGeometry(QtCore.QRect(110, 160, 131, 101))
        self.plainTextEditDiaChi.setReadOnly(False)
        self.plainTextEditDiaChi.setObjectName("plainTextEditDiaChi")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(270, 160, 51, 16))
        self.label_9.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_9.setObjectName("label_9")
        self.detailSDT = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.detailSDT.setGeometry(QtCore.QRect(340, 160, 131, 22))
        self.detailSDT.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.detailSDT.setReadOnly(False)
        self.detailSDT.setObjectName("detailSDT")
        self.btnEdit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnEdit.setGeometry(QtCore.QRect(270, 240, 61, 24))
        self.btnEdit.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btnEdit.setObjectName("btnEdit")
        self.btnClose = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(360, 240, 61, 24))
        self.btnClose.setStyleSheet("")
        self.btnClose.setObjectName("btnClose")
        self.detailIDLop = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.detailIDLop.setGeometry(QtCore.QRect(340, 40, 101, 22))
        self.detailIDLop.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.detailIDLop.setReadOnly(True)
        self.detailIDLop.setObjectName("detailIDLop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chi Tiết Thông Tin Sinh Viên"))
        self.label.setText(_translate("MainWindow", "THÔNG TIN SINH VIÊN"))
        self.label_2.setText(_translate("MainWindow", "Mã Lớp"))
        self.label_3.setText(_translate("MainWindow", "Mã Sinh Viên"))
        self.label_4.setText(_translate("MainWindow", "Họ Tên"))
        self.label_5.setText(_translate("MainWindow", "Ngày Sinh"))
        self.label_6.setText(_translate("MainWindow", "Giới Tính"))
        self.cbBoxSex.setItemText(0, _translate("MainWindow", "Nam"))
        self.cbBoxSex.setItemText(1, _translate("MainWindow", "Nữ"))
        self.cbBoxSex.setItemText(2, _translate("MainWindow", "Khác"))
        self.label_7.setText(_translate("MainWindow", "Dân Tộc"))
        self.label_8.setText(_translate("MainWindow", "Địa Chỉ"))
        self.label_9.setText(_translate("MainWindow", "Liên Hệ"))
        self.btnEdit.setText(_translate("MainWindow", "Sửa"))
        self.btnClose.setText(_translate("MainWindow", "Đóng"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

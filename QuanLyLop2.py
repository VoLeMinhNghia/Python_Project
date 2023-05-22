# Form implementation generated from reading ui file 'QuanLyLop.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabQuanLy = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabQuanLy.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.tabQuanLy.setObjectName("tabQuanLy")
        self.tabQLLop = QtWidgets.QWidget()
        self.tabQLLop.setObjectName("tabQLLop")
        self.btnSort = QtWidgets.QPushButton(parent=self.tabQLLop)
        self.btnSort.setGeometry(QtCore.QRect(90, 10, 81, 31))
        self.btnSort.setStyleSheet("background-color: rgb(255, 182, 153);\n"
"font: 10pt \"Segoe UI\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/ic/icsort.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSort.setIcon(icon)
        self.btnSort.setIconSize(QtCore.QSize(20, 20))
        self.btnSort.setObjectName("btnSort")
        self.btnAddLop = QtWidgets.QPushButton(parent=self.tabQLLop)
        self.btnAddLop.setGeometry(QtCore.QRect(340, 10, 91, 31))
        self.btnAddLop.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 10pt \"Segoe UI\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/ic/icadd.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnAddLop.setIcon(icon1)
        self.btnAddLop.setIconSize(QtCore.QSize(20, 20))
        self.btnAddLop.setObjectName("btnAddLop")
        self.btnHome = QtWidgets.QPushButton(parent=self.tabQLLop)
        self.btnHome.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.btnHome.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 127);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/ic/icHome.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnHome.setIcon(icon2)
        self.btnHome.setIconSize(QtCore.QSize(20, 20))
        self.btnHome.setObjectName("btnHome")
        self.tableLop = QtWidgets.QTableWidget(parent=self.tabQLLop)
        self.tableLop.setGeometry(QtCore.QRect(10, 60, 781, 471))
        self.tableLop.setRowCount(5)
        self.tableLop.setColumnCount(4)
        self.tableLop.setObjectName("tableLop")
        item = QtWidgets.QTableWidgetItem()
        self.tableLop.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLop.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLop.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLop.setHorizontalHeaderItem(3, item)
        self.btnDetailLop = QtWidgets.QPushButton(parent=self.tabQLLop)
        self.btnDetailLop.setGeometry(QtCore.QRect(700, 10, 91, 31))
        self.btnDetailLop.setStyleSheet("background-color: rgb(218, 145, 0);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btnDetailLop.setIconSize(QtCore.QSize(20, 20))
        self.btnDetailLop.setObjectName("btnDetailLop")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.tabQLLop)
        self.groupBox_3.setGeometry(QtCore.QRect(450, 0, 241, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.maLop_2 = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.maLop_2.setGeometry(QtCore.QRect(10, 20, 131, 22))
        self.maLop_2.setReadOnly(True)
        self.maLop_2.setObjectName("maLop_2")
        self.btnDeleteLop = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btnDeleteLop.setGeometry(QtCore.QRect(160, 10, 71, 31))
        self.btnDeleteLop.setStyleSheet("background-color: rgb(209, 0, 0);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btnDeleteLop.setIconSize(QtCore.QSize(20, 20))
        self.btnDeleteLop.setObjectName("btnDeleteLop")
        self.btnReloadLop = QtWidgets.QPushButton(parent=self.tabQLLop)
        self.btnReloadLop.setGeometry(QtCore.QRect(180, 10, 91, 31))
        self.btnReloadLop.setStyleSheet("background-color: rgb(16, 16, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/ic/icreload.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnReloadLop.setIcon(icon3)
        self.btnReloadLop.setIconSize(QtCore.QSize(20, 20))
        self.btnReloadLop.setObjectName("btnReloadLop")
        self.tabQuanLy.addTab(self.tabQLLop, "")
        self.tabQLSV = QtWidgets.QWidget()
        self.tabQLSV.setObjectName("tabQLSV")
        self.btnFindSV = QtWidgets.QPushButton(parent=self.tabQLSV)
        self.btnFindSV.setGeometry(QtCore.QRect(190, 50, 51, 31))
        self.btnFindSV.setObjectName("btnFindSV")
        self.lineEditFindSV = QtWidgets.QLineEdit(parent=self.tabQLSV)
        self.lineEditFindSV.setGeometry(QtCore.QRect(70, 50, 121, 31))
        self.lineEditFindSV.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.lineEditFindSV.setObjectName("lineEditFindSV")
        self.btnAddSV = QtWidgets.QPushButton(parent=self.tabQLSV)
        self.btnAddSV.setGeometry(QtCore.QRect(280, 10, 121, 31))
        self.btnAddSV.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 10pt \"Segoe UI\";")
        self.btnAddSV.setIcon(icon1)
        self.btnAddSV.setIconSize(QtCore.QSize(20, 20))
        self.btnAddSV.setObjectName("btnAddSV")
        self.label_3 = QtWidgets.QLabel(parent=self.tabQLSV)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_3.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.tabQLSV)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 31, 16))
        self.label_4.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_4.setObjectName("label_4")
        self.cbBoxLop = QtWidgets.QComboBox(parent=self.tabQLSV)
        self.cbBoxLop.setGeometry(QtCore.QRect(50, 10, 101, 22))
        self.cbBoxLop.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.cbBoxLop.setObjectName("cbBoxLop")
        self.btnPrintAllSV = QtWidgets.QPushButton(parent=self.tabQLSV)
        self.btnPrintAllSV.setGeometry(QtCore.QRect(730, 70, 61, 31))
        self.btnPrintAllSV.setStyleSheet("font: 10pt \"Segoe UI\";")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/ic/icprint.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnPrintAllSV.setIcon(icon4)
        self.btnPrintAllSV.setIconSize(QtCore.QSize(20, 20))
        self.btnPrintAllSV.setObjectName("btnPrintAllSV")
        self.tableSinhVien = QtWidgets.QTableWidget(parent=self.tabQLSV)
        self.tableSinhVien.setGeometry(QtCore.QRect(0, 110, 801, 441))
        self.tableSinhVien.setStyleSheet("font: 8pt \"Segoe UI\";")
        self.tableSinhVien.setRowCount(5)
        self.tableSinhVien.setColumnCount(8)
        self.tableSinhVien.setObjectName("tableSinhVien")
        item = QtWidgets.QTableWidgetItem()
        self.tableSinhVien.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSinhVien.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSinhVien.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSinhVien.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSinhVien.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSinhVien.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSinhVien.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSinhVien.setHorizontalHeaderItem(7, item)
        self.btnDetailSV = QtWidgets.QPushButton(parent=self.tabQLSV)
        self.btnDetailSV.setGeometry(QtCore.QRect(660, 10, 91, 31))
        self.btnDetailSV.setStyleSheet("background-color: rgb(218, 145, 0);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btnDetailSV.setIconSize(QtCore.QSize(20, 20))
        self.btnDetailSV.setObjectName("btnDetailSV")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tabQLSV)
        self.groupBox_2.setGeometry(QtCore.QRect(410, 0, 241, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnDeleteSV = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btnDeleteSV.setGeometry(QtCore.QRect(170, 60, 61, 31))
        self.btnDeleteSV.setStyleSheet("background-color: rgb(209, 0, 0);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btnDeleteSV.setIconSize(QtCore.QSize(20, 20))
        self.btnDeleteSV.setObjectName("btnDeleteSV")
        self.maSinhVien = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.maSinhVien.setGeometry(QtCore.QRect(10, 20, 91, 22))
        self.maSinhVien.setReadOnly(True)
        self.maSinhVien.setObjectName("maSinhVien")
        self.maLop = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.maLop.setGeometry(QtCore.QRect(130, 20, 91, 22))
        self.maLop.setReadOnly(True)
        self.maLop.setObjectName("maLop")
        self.hoTen = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.hoTen.setGeometry(QtCore.QRect(10, 70, 141, 22))
        self.hoTen.setReadOnly(True)
        self.hoTen.setObjectName("hoTen")
        self.btnCancalFind = QtWidgets.QPushButton(parent=self.tabQLSV)
        self.btnCancalFind.setGeometry(QtCore.QRect(240, 50, 51, 31))
        self.btnCancalFind.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.btnCancalFind.setObjectName("btnCancalFind")
        self.btnSortSV = QtWidgets.QPushButton(parent=self.tabQLSV)
        self.btnSortSV.setGeometry(QtCore.QRect(310, 50, 91, 31))
        self.btnSortSV.setStyleSheet("background-color: rgb(255, 182, 153);\n"
"font: 10pt \"Segoe UI\";")
        self.btnSortSV.setIcon(icon)
        self.btnSortSV.setIconSize(QtCore.QSize(20, 20))
        self.btnSortSV.setObjectName("btnSortSV")
        self.btnReloadSV = QtWidgets.QPushButton(parent=self.tabQLSV)
        self.btnReloadSV.setGeometry(QtCore.QRect(170, 10, 91, 31))
        self.btnReloadSV.setStyleSheet("background-color: rgb(16, 16, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btnReloadSV.setIcon(icon3)
        self.btnReloadSV.setIconSize(QtCore.QSize(20, 20))
        self.btnReloadSV.setObjectName("btnReloadSV")
        self.tabQuanLy.addTab(self.tabQLSV, "")
        self.tabQLDiem = QtWidgets.QWidget()
        self.tabQLDiem.setObjectName("tabQLDiem")
        self.label_6 = QtWidgets.QLabel(parent=self.tabQLDiem)
        self.label_6.setGeometry(QtCore.QRect(160, 20, 61, 16))
        self.label_6.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.tabQLDiem)
        self.label_7.setGeometry(QtCore.QRect(340, 20, 51, 16))
        self.label_7.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_7.setObjectName("label_7")
        self.cbBoxMon_2 = QtWidgets.QComboBox(parent=self.tabQLDiem)
        self.cbBoxMon_2.setGeometry(QtCore.QRect(220, 20, 101, 22))
        self.cbBoxMon_2.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.cbBoxMon_2.setObjectName("cbBoxMon_2")
        self.cbBoxHocKy = QtWidgets.QComboBox(parent=self.tabQLDiem)
        self.cbBoxHocKy.setGeometry(QtCore.QRect(390, 20, 101, 22))
        self.cbBoxHocKy.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.cbBoxHocKy.setObjectName("cbBoxHocKy")
        self.label = QtWidgets.QLabel(parent=self.tabQLDiem)
        self.label.setGeometry(QtCore.QRect(10, 20, 141, 16))
        self.label.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"font: 700 9pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.btnAddDiem = QtWidgets.QPushButton(parent=self.tabQLDiem)
        self.btnAddDiem.setGeometry(QtCore.QRect(560, 10, 131, 31))
        self.btnAddDiem.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 10pt \"Segoe UI\";")
        self.btnAddDiem.setIcon(icon1)
        self.btnAddDiem.setIconSize(QtCore.QSize(20, 20))
        self.btnAddDiem.setObjectName("btnAddDiem")
        self.tableDiem = QtWidgets.QTableWidget(parent=self.tabQLDiem)
        self.tableDiem.setGeometry(QtCore.QRect(10, 50, 681, 481))
        self.tableDiem.setRowCount(5)
        self.tableDiem.setColumnCount(6)
        self.tableDiem.setObjectName("tableDiem")
        item = QtWidgets.QTableWidgetItem()
        self.tableDiem.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDiem.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDiem.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDiem.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDiem.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDiem.setHorizontalHeaderItem(5, item)
        self.btnPrintAllDiem = QtWidgets.QPushButton(parent=self.tabQLDiem)
        self.btnPrintAllDiem.setGeometry(QtCore.QRect(700, 500, 91, 31))
        self.btnPrintAllDiem.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.btnPrintAllDiem.setIcon(icon4)
        self.btnPrintAllDiem.setIconSize(QtCore.QSize(20, 20))
        self.btnPrintAllDiem.setObjectName("btnPrintAllDiem")
        self.btnSortDiem = QtWidgets.QPushButton(parent=self.tabQLDiem)
        self.btnSortDiem.setGeometry(QtCore.QRect(700, 10, 91, 31))
        self.btnSortDiem.setStyleSheet("background-color: rgb(255, 182, 153);\n"
"font: 10pt \"Segoe UI\";")
        self.btnSortDiem.setIcon(icon)
        self.btnSortDiem.setIconSize(QtCore.QSize(20, 20))
        self.btnSortDiem.setObjectName("btnSortDiem")
        self.groupBox = QtWidgets.QGroupBox(parent=self.tabQLDiem)
        self.groupBox.setGeometry(QtCore.QRect(700, 50, 91, 171))
        self.groupBox.setObjectName("groupBox")
        self.maSV = QtWidgets.QLineEdit(parent=self.groupBox)
        self.maSV.setGeometry(QtCore.QRect(10, 20, 71, 22))
        self.maSV.setReadOnly(True)
        self.maSV.setObjectName("maSV")
        self.maHK = QtWidgets.QLineEdit(parent=self.groupBox)
        self.maHK.setGeometry(QtCore.QRect(10, 50, 71, 22))
        self.maHK.setReadOnly(True)
        self.maHK.setObjectName("maHK")
        self.maMon = QtWidgets.QLineEdit(parent=self.groupBox)
        self.maMon.setGeometry(QtCore.QRect(10, 80, 71, 22))
        self.maMon.setReadOnly(True)
        self.maMon.setObjectName("maMon")
        self.btnDeleteDiem = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnDeleteDiem.setGeometry(QtCore.QRect(20, 120, 51, 31))
        self.btnDeleteDiem.setStyleSheet("background-color: rgb(209, 0, 0);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btnDeleteDiem.setIconSize(QtCore.QSize(20, 20))
        self.btnDeleteDiem.setObjectName("btnDeleteDiem")
        self.btnDetailDiem = QtWidgets.QPushButton(parent=self.tabQLDiem)
        self.btnDetailDiem.setGeometry(QtCore.QRect(700, 230, 91, 31))
        self.btnDetailDiem.setStyleSheet("background-color: rgb(218, 145, 0);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btnDetailDiem.setIconSize(QtCore.QSize(20, 20))
        self.btnDetailDiem.setObjectName("btnDetailDiem")
        self.btnReloadDiem = QtWidgets.QPushButton(parent=self.tabQLDiem)
        self.btnReloadDiem.setGeometry(QtCore.QRect(700, 270, 91, 31))
        self.btnReloadDiem.setStyleSheet("background-color: rgb(16, 16, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btnReloadDiem.setIcon(icon3)
        self.btnReloadDiem.setIconSize(QtCore.QSize(20, 20))
        self.btnReloadDiem.setObjectName("btnReloadDiem")
        self.tabQuanLy.addTab(self.tabQLDiem, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabQuanLy.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnSort.setText(_translate("MainWindow", "Sắp Xếp"))
        self.btnAddLop.setText(_translate("MainWindow", "Thêm Lớp"))
        self.btnHome.setText(_translate("MainWindow", "Home"))
        item = self.tableLop.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã lớp"))
        item = self.tableLop.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mã nghành"))
        item = self.tableLop.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mã niên khóa"))
        item = self.tableLop.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tên lớp"))
        self.btnDetailLop.setText(_translate("MainWindow", "Xem Chi Tiết"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Thông Tin"))
        self.btnDeleteLop.setText(_translate("MainWindow", "Xóa Lớp"))
        self.btnReloadLop.setText(_translate("MainWindow", "Cập Nhật"))
        self.tabQuanLy.setTabText(self.tabQuanLy.indexOf(self.tabQLLop), _translate("MainWindow", "Quản Lý Lớp"))
        self.btnFindSV.setText(_translate("MainWindow", "Tìm"))
        self.btnAddSV.setText(_translate("MainWindow", "Thêm Sinh Viên"))
        self.label_3.setText(_translate("MainWindow", "Tìm Kiếm"))
        self.label_4.setText(_translate("MainWindow", "Lớp"))
        self.btnPrintAllSV.setText(_translate("MainWindow", "Xuất"))
        item = self.tableSinhVien.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã sinh viên"))
        item = self.tableSinhVien.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mã lớp"))
        item = self.tableSinhVien.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Họ tên"))
        item = self.tableSinhVien.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ngày sinh"))
        item = self.tableSinhVien.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Giới tính"))
        item = self.tableSinhVien.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Dân tộc"))
        item = self.tableSinhVien.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Địa chỉ"))
        item = self.tableSinhVien.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Số điện thoại"))
        self.btnDetailSV.setText(_translate("MainWindow", "Xem Chi Tiết"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Thông Tin"))
        self.btnDeleteSV.setText(_translate("MainWindow", "Xóa"))
        self.btnCancalFind.setText(_translate("MainWindow", "Hủy"))
        self.btnSortSV.setText(_translate("MainWindow", "Sắp Xếp"))
        self.btnReloadSV.setText(_translate("MainWindow", "Cập Nhật"))
        self.tabQuanLy.setTabText(self.tabQuanLy.indexOf(self.tabQLSV), _translate("MainWindow", "Quản Lý Sinh Viên"))
        self.label_6.setText(_translate("MainWindow", "Môn Học"))
        self.label_7.setText(_translate("MainWindow", "Học Kỳ"))
        self.label.setText(_translate("MainWindow", "CẬP NHẬT BẢNG ĐIỂM"))
        self.btnAddDiem.setText(_translate("MainWindow", "Thêm Bảng Điểm"))
        item = self.tableDiem.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã sinh viên"))
        item = self.tableDiem.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mã học kỳ"))
        item = self.tableDiem.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mã môn"))
        item = self.tableDiem.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Điểm quá trình"))
        item = self.tableDiem.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Điểm giữa kỳ"))
        item = self.tableDiem.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Điểm cuối kỳ"))
        self.btnPrintAllDiem.setText(_translate("MainWindow", "Xuất"))
        self.btnSortDiem.setText(_translate("MainWindow", "Sắp Xếp"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông Tin"))
        self.btnDeleteDiem.setText(_translate("MainWindow", "Xóa"))
        self.btnDetailDiem.setText(_translate("MainWindow", "Xem Chi Tiết"))
        self.btnReloadDiem.setText(_translate("MainWindow", "Cập Nhật"))
        self.tabQuanLy.setTabText(self.tabQuanLy.indexOf(self.tabQLDiem), _translate("MainWindow", "Quản Lý Điểm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

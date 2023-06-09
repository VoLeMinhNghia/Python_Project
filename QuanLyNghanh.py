# Form implementation generated from reading ui file 'QuanLyNghanh.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from functools import partial
from database import *

myDB = MY_DB()

class Ui_QuanLyNghanh(object):
    global myDB
    def setupUi(self, QuanLyNghanh):
        myDB.connect()

        QuanLyNghanh.setObjectName("QuanLyNghanh")
        QuanLyNghanh.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=QuanLyNghanh)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 151, 16))
        self.label_7.setStyleSheet("font: 700 12pt \"Segoe UI\";")
        self.label_7.setObjectName("label_7")
        self.btnSort = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnSort.setGeometry(QtCore.QRect(340, 40, 81, 31))
        self.btnSort.setStyleSheet("background-color: rgb(255, 182, 153);\n"
"font: 10pt \"Segoe UI\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/ic/icsort.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSort.setIcon(icon)
        self.btnSort.setIconSize(QtCore.QSize(20, 20))
        self.btnSort.setObjectName("btnSort")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 50, 131, 21))
        self.label_6.setStyleSheet("font: 700 12pt \"Segoe UI\";")
        self.label_6.setObjectName("label_6")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(430, 80, 361, 181))
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 240, 166);\n"
"font: 10pt \"Segoe UI\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 71, 41))
        self.label_4.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_4.setObjectName("label_4")
        self.IDNghanh = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.IDNghanh.setGeometry(QtCore.QRect(90, 30, 113, 22))
        self.IDNghanh.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.IDNghanh.setText("")
        self.IDNghanh.setReadOnly(False)
        self.IDNghanh.setObjectName("IDNghanh")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 71, 41))
        self.label_5.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_5.setObjectName("label_5")
        self.NameNghanh = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.NameNghanh.setGeometry(QtCore.QRect(90, 110, 161, 22))
        self.NameNghanh.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.NameNghanh.setReadOnly(False)
        self.NameNghanh.setObjectName("NameNghanh")
        self.btnSave = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btnSave.setGeometry(QtCore.QRect(200, 140, 61, 24))
        self.btnSave.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.btnSave.setObjectName("btnSave")
        self.btnCancel = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btnCancel.setGeometry(QtCore.QRect(280, 140, 61, 24))
        self.btnCancel.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.btnCancel.setObjectName("btnCancel")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_8.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_8.setObjectName("label_8")
        self.cbBoxKhoa = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.cbBoxKhoa.setGeometry(QtCore.QRect(90, 70, 111, 22))
        self.cbBoxKhoa.setObjectName("cbBoxKhoa")
        self.err = QtWidgets.QLabel(parent=self.groupBox_2)
        self.err.setGeometry(QtCore.QRect(210, 30, 121, 16))
        self.err.setStyleSheet("color: rgb(170, 0, 0);")
        self.err.setText("")
        self.err.setObjectName("err")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(430, 280, 361, 181))
        self.groupBox.setStyleSheet("background-color: rgb(112, 200, 255);\n"
"font: 10pt \"Segoe UI\";")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_2.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_2.setObjectName("label_2")
        self.detailIDKhoa = QtWidgets.QLineEdit(parent=self.groupBox)
        self.detailIDKhoa.setGeometry(QtCore.QRect(90, 60, 113, 22))
        self.detailIDKhoa.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.detailIDKhoa.setReadOnly(True)
        self.detailIDKhoa.setObjectName("detailIDKhoa")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 71, 41))
        self.label_3.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_3.setObjectName("label_3")
        self.detailNameNghanh = QtWidgets.QLineEdit(parent=self.groupBox)
        self.detailNameNghanh.setGeometry(QtCore.QRect(90, 90, 161, 22))
        self.detailNameNghanh.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.detailNameNghanh.setReadOnly(True)
        self.detailNameNghanh.setObjectName("detailNameNghanh")
        self.btnEdit = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnEdit.setGeometry(QtCore.QRect(200, 140, 61, 24))
        self.btnEdit.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btnEdit.setObjectName("btnEdit")
        self.btnDelete = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnDelete.setGeometry(QtCore.QRect(280, 140, 61, 24))
        self.btnDelete.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btnDelete.setObjectName("btnDelete")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 71, 41))
        self.label_9.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_9.setObjectName("label_9")
        self.detailIDNghanh = QtWidgets.QLineEdit(parent=self.groupBox)
        self.detailIDNghanh.setGeometry(QtCore.QRect(90, 30, 113, 22))
        self.detailIDNghanh.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.detailIDNghanh.setReadOnly(True)
        self.detailIDNghanh.setObjectName("detailIDNghanh")
        self.islock = QtWidgets.QLabel(parent=self.groupBox)
        self.islock.setGeometry(QtCore.QRect(260, 90, 51, 21))
        self.islock.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: rgb(170, 0, 0);")
        self.islock.setText("")
        self.islock.setObjectName("islock")
        self.err_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.err_2.setGeometry(QtCore.QRect(90, 115, 161, 21))
        self.err_2.setStyleSheet("color: rgb(170, 0, 0);")
        self.err_2.setText("")
        self.err_2.setObjectName("err_2")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(60, 140, 141, 21))
        self.label_10.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_10.setObjectName("label_10")
        self.btnReload = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnReload.setGeometry(QtCore.QRect(430, 480, 91, 31))
        self.btnReload.setStyleSheet("background-color: rgb(16, 16, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/ic/icreload.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnReload.setIcon(icon1)
        self.btnReload.setIconSize(QtCore.QSize(20, 20))
        self.btnReload.setObjectName("btnReload")
        self.btnHome = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnHome.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.btnHome.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 127);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/ic/icHome.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnHome.setIcon(icon2)
        self.btnHome.setIconSize(QtCore.QSize(20, 20))
        self.btnHome.setObjectName("btnHome")
        self.tableNghanh = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableNghanh.setGeometry(QtCore.QRect(10, 80, 411, 471))
        self.tableNghanh.setRowCount(5)
        self.tableNghanh.setColumnCount(3)
        self.tableNghanh.setColumnWidth(0, 90)
        self.tableNghanh.setColumnWidth(1, 70)
        self.tableNghanh.setColumnWidth(2, 250)
        self.tableNghanh.setObjectName("tableNghanh")
        item = QtWidgets.QTableWidgetItem()
        self.tableNghanh.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableNghanh.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableNghanh.setHorizontalHeaderItem(2, item)
        QuanLyNghanh.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=QuanLyNghanh)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        QuanLyNghanh.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=QuanLyNghanh)
        self.statusbar.setObjectName("statusbar")
        QuanLyNghanh.setStatusBar(self.statusbar)

        self.btnHome.clicked.connect(partial(self.goHome, QuanLyNghanh))

        self.khoaTable = myDB.select_all_khoa()
        self.cbBoxKhoa.clear()  # Xóa danh sách cũ trong combobox trước khi thêm mới
        for row_data in self.khoaTable:
                ma_khoa = row_data[0] 
                self.cbBoxKhoa.addItem(str(ma_khoa))


        self.retranslateUi(QuanLyNghanh)
        QtCore.QMetaObject.connectSlotsByName(QuanLyNghanh)

        self.nghanhTable = myDB.select_all_nghanh()

        self.tableNghanh.setRowCount(0)
        for row_num, row_data in enumerate(self.nghanhTable):
                self.tableNghanh.insertRow(row_num)
                for col_num, col_data in enumerate(row_data):
                     self.tableNghanh.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))

        self.tableNghanh.cellClicked.connect(self.on_tableNghanh_cellClicked)
        self.btnEdit.clicked.connect(self.enable_edit_mode)
        self.btnReload.clicked.connect(self.reload_data)

        self.btnSave.clicked.connect(self.on_btnSave_clicked)
        self.btnCancel.clicked.connect(self.cancel)

        self.btnDelete.clicked.connect(self.delete)
        self.btnSort.clicked.connect(self.sort_table_alphabetically)

    def goHome(self, QuanLyNghanh):
        from MainWindow import Ui_MainWindow as Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        QuanLyNghanh.close()
        self.window.show()

#-----------------------------INSERT--------------------------------------------

    def on_btnSave_clicked(self):
        maNghanh = self.IDNghanh.text().strip()
        makhoa = self.cbBoxKhoa.currentText().strip()
        tenNghanh = self.NameNghanh.text().strip()

        nghanh = myDB.select_nghanh_by_id(maNghanh).fetchone()

        if maNghanh == "" or tenNghanh == "": 
             self.err.setText("Không bỏ trống !!")
             return 
        if nghanh != None:
             self.err.setText("Mã nghành đã tồn tại")
             return
        # Thêm Nghanh vào CSDL
        myDB.insert_nghanh(maNghanh, makhoa, tenNghanh)
        self.cancel()
        self.load_data()

    def cancel(self):
        self.IDNghanh.setText("")
        self.NameNghanh.setText("")
        self.err.setText("")

#---------------------------------- UPDATE--------------------------------------
    def on_tableNghanh_cellClicked(self, row, column):
        self.load_data()
        self.islock.setText("Lock")
        self.err_2.setText("")
        # Lấy mã Nghanh từ dòng được click
        maNghanh = self.tableNghanh.item(row, 0).text()

        # Lấy thông tin Nghanh từ CSDL
        Nghanh = myDB.select_nghanh_by_id(maNghanh).fetchone()

        # Hiển thị thông tin Nghanh trong groupBox
        self.detailIDNghanh.setText(Nghanh[0])
        self.detailIDKhoa.setText(Nghanh[1])
        self.detailNameNghanh.setText(Nghanh[2])

    def enable_edit_mode(self):
        current_id = self.detailIDNghanh.text()
        current_name = self.detailNameNghanh.text()
        if current_id == "" or current_name == "":
             return self.load_data()
        else: 
             self.islock.setStyleSheet("color: rgb(0, 170, 0);")
             self.islock.setText("Unlock")
             self.detailNameNghanh.setReadOnly(False)

    def reload_data(self):
        current_id = self.detailIDNghanh.text()
        current_name = self.detailNameNghanh.text()

        current_nghanh = myDB.select_nghanh_by_id(current_id).fetchone()
        
        if current_nghanh == None:
                self.err_2.setText("Dữ liệu trống !!")
                return
        if current_name != current_nghanh[2]:
                myDB.update_nghanh(current_name, current_id)
                self.detailNameNghanh.setReadOnly(True)
        self.detailIDNghanh.setText("")
        self.detailIDKhoa.setText("")
        self.detailNameNghanh.setText("")
        self.load_data()

#-----------------------------------DELETE----------------------------------------------------
    def delete(self):
        current_id = self.detailIDNghanh.text()
        current_name = self.detailNameNghanh.text()
        if current_name == "":
             return self.load_data()
        else:
             myDB.delete_nghanh(current_id)
             self.detailIDNghanh.setText("")
             self.detailIDKhoa.setText("")
             self.detailNameNghanh.setText("")
             self.load_data()

    def load_data(self):
        self.islock.setStyleSheet("color: rgb(170, 0, 0);")
        self.islock.setText("")
        self.err_2.setText("")
        self.detailNameNghanh.setReadOnly(True)
        self.NghanhTable = myDB.select_all_nghanh()
        self.tableNghanh.setRowCount(0)
        for row_num, row_data in enumerate(self.NghanhTable):
                self.tableNghanh.insertRow(row_num)
                for col_num, col_data in enumerate(row_data):
                     self.tableNghanh.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))

    def sort_table_alphabetically(self):
        # Lấy số cột trong bảng
        column_count = self.tableNghanh.columnCount()
        # Lấy số hàng trong bảng
        row_count = self.tableNghanh.rowCount()
        # Tạo một danh sách các dòng trong bảng, mỗi dòng là một list các giá trị trong ô
        rows = [[self.tableNghanh.item(row, col).text() for col in range(column_count)] for row in range(row_count)]
        # Sắp xếp các dòng theo thứ tự tăng dần của cột tên khoa (cột thứ hai)
        sorted_rows = sorted(rows, key=lambda row: row[2])
        # Xóa tất cả các hàng cũ trong bảng
        self.tableNghanh.setRowCount(0)
        # Thêm các hàng đã sắp xếp vào bảng
        for row in sorted_rows:
                self.tableNghanh.insertRow(self.tableNghanh.rowCount())
                for col, value in enumerate(row):
                        item = QtWidgets.QTableWidgetItem(value)
                        self.tableNghanh.setItem(self.tableNghanh.rowCount() - 1, col, item)

    def retranslateUi(self, QuanLyNghanh):
        _translate = QtCore.QCoreApplication.translate
        QuanLyNghanh.setWindowTitle(_translate("QuanLyNghanh", "Quản Lý Nghành"))
        self.label_7.setText(_translate("QuanLyNghanh", "QUẢN LÝ NGHÀNH"))
        self.btnSort.setText(_translate("QuanLyNghanh", "Sắp Xếp"))
        self.label_6.setText(_translate("QuanLyNghanh", "Chức Năng"))
        self.groupBox_2.setTitle(_translate("QuanLyNghanh", "Thêm Nghành"))
        self.label_4.setText(_translate("QuanLyNghanh", "Mã Nghành:"))
        self.label_5.setText(_translate("QuanLyNghanh", "Tên Nghành:"))
        self.btnSave.setText(_translate("QuanLyNghanh", "Lưu"))
        self.btnCancel.setText(_translate("QuanLyNghanh", "Hủy"))
        self.label_8.setText(_translate("QuanLyNghanh", "Mã Khoa"))
        self.groupBox.setTitle(_translate("QuanLyNghanh", "Thông Tin Chi Tiết"))
        self.label_2.setText(_translate("QuanLyNghanh", "Mã Khoa:"))
        self.label_3.setText(_translate("QuanLyNghanh", "Tên Nghành:"))
        self.btnEdit.setText(_translate("QuanLyNghanh", "Sửa"))
        self.label_10.setText(_translate("QuanLyNghanh", "Click here to unlock ->"))
        self.btnDelete.setText(_translate("QuanLyNghanh", "Xóa"))
        self.label_9.setText(_translate("QuanLyNghanh", "Mã Nghành:"))
        self.btnReload.setText(_translate("QuanLyNghanh", "Cập Nhật"))
        self.btnHome.setText(_translate("QuanLyNghanh", "Home"))
        item = self.tableNghanh.horizontalHeaderItem(0)
        item.setText(_translate("QuanLyNghanh", "Mã nghành"))
        item = self.tableNghanh.horizontalHeaderItem(1)
        item.setText(_translate("QuanLyNghanh", "Mã khoa"))
        item = self.tableNghanh.horizontalHeaderItem(2)
        item.setText(_translate("QuanLyNghanh", "Tên nghành"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QuanLyNghanh = QtWidgets.QMainWindow()
    ui = Ui_QuanLyNghanh()
    ui.setupUi(QuanLyNghanh)
    QuanLyNghanh.show()
    sys.exit(app.exec())

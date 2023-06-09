# Form implementation generated from reading ui file 'QuanLyMon.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt6 import QtCore, QtGui, QtWidgets
from functools import partial
from database import *

myDB = MY_DB()

class Ui_MainWindow(object):
    global myDB
    def setupUi(self, MainWindow):
        myDB.connect()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 161, 21))
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
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_5.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_5.setObjectName("label_5")
        self.NameMon = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.NameMon.setGeometry(QtCore.QRect(80, 40, 161, 22))
        self.NameMon.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.NameMon.setReadOnly(False)
        self.NameMon.setObjectName("NameMon")
        self.btnSave = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btnSave.setGeometry(QtCore.QRect(200, 140, 61, 24))
        self.btnSave.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.btnSave.setObjectName("btnSave")
        self.btnCancel = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btnCancel.setGeometry(QtCore.QRect(280, 140, 61, 24))
        self.btnCancel.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.btnCancel.setObjectName("btnCancel")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_8.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_8.setObjectName("label_8")
        self.SoTC = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.SoTC.setGeometry(QtCore.QRect(80, 90, 61, 22))
        self.SoTC.setMinimum(1)
        self.SoTC.setMaximum(9)
        self.SoTC.setObjectName("SoTC")
        self.err = QtWidgets.QLabel(parent=self.groupBox_2)
        self.err.setGeometry(QtCore.QRect(80, 65, 161, 21))
        self.err.setStyleSheet("color: rgb(170, 0, 0);")
        self.err.setText("")
        self.err.setObjectName("err")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(430, 280, 361, 201))
        self.groupBox.setStyleSheet("background-color: rgb(112, 200, 255);\n"
"font: 10pt \"Segoe UI\";")
        self.groupBox.setObjectName("groupBox")
        self.detailNameMon = QtWidgets.QLineEdit(parent=self.groupBox)
        self.detailNameMon.setGeometry(QtCore.QRect(90, 70, 161, 22))
        self.detailNameMon.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.detailNameMon.setReadOnly(True)
        self.detailNameMon.setObjectName("detailNameMon")
        self.btnEdit = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnEdit.setGeometry(QtCore.QRect(200, 160, 61, 24))
        self.btnEdit.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btnEdit.setObjectName("btnEdit")
        self.btnDelete = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnDelete.setGeometry(QtCore.QRect(280, 160, 61, 24))
        self.btnDelete.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btnDelete.setObjectName("btnDelete")
        self.detailIDKMon = QtWidgets.QLineEdit(parent=self.groupBox)
        self.detailIDKMon.setGeometry(QtCore.QRect(90, 30, 113, 22))
        self.detailIDKMon.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.detailIDKMon.setReadOnly(True)
        self.detailIDKMon.setObjectName("detailIDKMon")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_10.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_9.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 120, 71, 21))
        self.label_11.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_11.setObjectName("label_11")
        self.detailSoTC = QtWidgets.QSpinBox(parent=self.groupBox)
        self.detailSoTC.setGeometry(QtCore.QRect(90, 120, 61, 22))
        self.detailSoTC.setReadOnly(True)
        self.detailSoTC.setMinimum(1)
        self.detailSoTC.setMaximum(9)
        self.detailSoTC.setObjectName("detailSoTC")
        self.islock = QtWidgets.QLabel(parent=self.groupBox)
        self.islock.setGeometry(QtCore.QRect(260, 70, 51, 21))
        self.islock.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: rgb(170, 0, 0);")
        self.islock.setText("")
        self.islock.setObjectName("islock")
        self.islock_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.islock_2.setGeometry(QtCore.QRect(160, 120, 51, 21))
        self.islock_2.setStyleSheet("font: 10pt \"Segoe UI\";\n"
"color: rgb(170, 0, 0);")
        self.islock_2.setText("")
        self.islock_2.setObjectName("islock_2")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(60, 160, 131, 21))
        self.label_12.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_12.setObjectName("label_12")
        self.err_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.err_2.setGeometry(QtCore.QRect(90, 100, 161, 16))
        self.err_2.setStyleSheet("color: rgb(170, 0, 0);")
        self.err_2.setText("")
        self.err_2.setObjectName("err_2")
        self.btnReload = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnReload.setGeometry(QtCore.QRect(430, 490, 91, 31))
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
        self.tableMon = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableMon.setGeometry(QtCore.QRect(0, 80, 421, 471))
        self.tableMon.setRowCount(5)
        self.tableMon.setColumnCount(3)
        self.tableMon.setColumnWidth(0, 55)
        self.tableMon.setColumnWidth(1, 270)
        self.tableMon.setColumnWidth(2, 71)
        self.tableMon.setObjectName("tableMon")
        item = QtWidgets.QTableWidgetItem()
        self.tableMon.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMon.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMon.setHorizontalHeaderItem(2, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.btnHome.clicked.connect(partial(self.goHome, MainWindow))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.monTable = myDB.select_all_monhoc()

        self.tableMon.setRowCount(0)
        for row_num, row_data in enumerate(self.monTable):
                self.tableMon.insertRow(row_num)
                for col_num, col_data in enumerate(row_data):
                     self.tableMon.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))

        self.tableMon.cellClicked.connect(self.on_tableMon_cellClicked)
        self.btnEdit.clicked.connect(self.enable_edit_mode)
        self.btnReload.clicked.connect(self.reload_data)

        self.btnSave.clicked.connect(self.on_btnSave_clicked)
        self.btnCancel.clicked.connect(self.cancel)

        self.btnDelete.clicked.connect(self.delete)
        
        self.btnSort.clicked.connect(self.sort_table_alphabetically)

    def goHome(self, MainWindow):
        from MainWindow import Ui_MainWindow as Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.close()
        self.window.show()

#-----------------------------INSERT--------------------------------------------

    def on_btnSave_clicked(self):
        tenMon = self.NameMon.text().strip()
        soTC = self.SoTC.value()
        if tenMon == "":
            self.err.setText("Không bỏ trống dữ liệu !!")
            return         
        # Thêm Mon vào CSDL
        myDB.insert_monhoc(tenMon, soTC)
        self.cancel()
        self.load_data()

    def cancel(self):
        self.NameMon.setText("")
        self.SoTC.setValue(1)
        self.err.setText("")

#---------------------------------- UPDATE--------------------------------------
    def on_tableMon_cellClicked(self, row, column):
        self.load_data()
        self.islock.setText("Lock")
        self.islock_2.setText("Lock")
        self.err_2.setText("")

        # Lấy mã Mon từ dòng được click
        maMon = self.tableMon.item(row, 0).text()

        # Lấy thông tin Mon từ CSDL
        Mon = myDB.select_monhoc_by_id(maMon).fetchone()

        # Hiển thị thông tin Mon trong groupBox
        self.detailIDKMon.setText(str(Mon[0]))
        self.detailNameMon.setText(Mon[1])
        self.detailSoTC.setValue(Mon[2])

    def enable_edit_mode(self):
        current_id = self.detailIDKMon.text()
        current_name = self.detailNameMon.text()

        if current_id == "" or current_name == "":
             return self.load_data()
        else: 
            self.islock.setStyleSheet("color: rgb(0, 170, 0);")
            self.islock.setText("Unlock")
            self.islock_2.setStyleSheet("color: rgb(0, 170, 0);")
            self.islock_2.setText("Unlock")
            self.detailNameMon.setReadOnly(False)
            self.detailSoTC.setReadOnly(False)

    def reload_data(self):
        current_id = self.detailIDKMon.text()
        current_name = self.detailNameMon.text()
        current_TC = self.detailSoTC.value()

        current_mon = myDB.select_monhoc_by_id(current_id).fetchone()
        if current_id == "" or current_name == "":
            self.err_2.setText("Không bỏ trống dữ liệu !!")
            return
        if current_name != current_mon[1] or current_TC != current_mon[2]:
                myDB.update_monhoc(current_name, current_TC, current_id)
                self.detailNameMon.setReadOnly(True)
                self.detailSoTC.setReadOnly(True)
        self.detailIDKMon.setText("")
        self.detailNameMon.setText("")
        self.load_data()

#-----------------------------------DELETE----------------------------------------------------
    def delete(self):
        current_id = self.detailIDKMon.text()
        current_name = self.detailNameMon.text()
        if current_id == "" or current_name == "":
             return self.load_data()
        else:
             myDB.delete_monhoc(current_id)
             self.detailIDKMon.setText("")
             self.detailNameMon.setText("")
             self.load_data()

    def load_data(self):
        self.islock.setStyleSheet("color: rgb(170, 0, 0);")
        self.islock.setText("")
        self.islock_2.setStyleSheet("color: rgb(170, 0, 0);")
        self.islock_2.setText("")
        self.err_2.setText("")
        self.detailNameMon.setReadOnly(True)
        self.detailSoTC.setReadOnly(True)
        self.detailSoTC.setValue(1)
        self.SoTC.setValue(1)
        self.monTable = myDB.select_all_monhoc()
        self.tableMon.setRowCount(0)
        for row_num, row_data in enumerate(self.monTable):
                self.tableMon.insertRow(row_num)
                for col_num, col_data in enumerate(row_data):
                     self.tableMon.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))

#----------------------------------SORT--------------------------------------------------------
    def sort_table_alphabetically(self):
        # Lấy số cột trong bảng
        column_count = self.tableMon.columnCount()
        # Lấy số hàng trong bảng
        row_count = self.tableMon.rowCount()
        # Tạo một danh sách các dòng trong bảng, mỗi dòng là một list các giá trị trong ô
        rows = [[self.tableMon.item(row, col).text() for col in range(column_count)] for row in range(row_count)]
        # Sắp xếp các dòng theo thứ tự tăng dần của cột tên khoa (cột thứ hai)
        sorted_rows = sorted(rows, key=lambda row: row[1])
        # Xóa tất cả các hàng cũ trong bảng
        self.tableMon.setRowCount(0)
        # Thêm các hàng đã sắp xếp vào bảng
        for row in sorted_rows:
                self.tableMon.insertRow(self.tableMon.rowCount())
                for col, value in enumerate(row):
                        item = QtWidgets.QTableWidgetItem(value)
                        self.tableMon.setItem(self.tableMon.rowCount() - 1, col, item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quản Lý Học Phần"))
        self.label_7.setText(_translate("MainWindow", "QUẢN LÝ MÔN HỌC"))
        self.btnSort.setText(_translate("MainWindow", "Sắp Xếp"))
        self.label_6.setText(_translate("MainWindow", "Chức Năng"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Thêm Môn"))
        self.label_5.setText(_translate("MainWindow", "Tên Môn"))
        self.btnSave.setText(_translate("MainWindow", "Lưu"))
        self.btnCancel.setText(_translate("MainWindow", "Hủy"))
        self.label_8.setText(_translate("MainWindow", "Số Tín Chỉ"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông Tin Chi Tiết"))
        self.btnEdit.setText(_translate("MainWindow", "Sửa"))
        self.btnDelete.setText(_translate("MainWindow", "Xóa"))
        self.label_10.setText(_translate("MainWindow", "Mã Môn"))
        self.label_9.setText(_translate("MainWindow", "Tên Môn"))
        self.label_11.setText(_translate("MainWindow", "Số Tín Chỉ"))
        self.label_12.setText(_translate("MainWindow", "Click here to unlock ->"))
        self.btnReload.setText(_translate("MainWindow", "Cập Nhật"))
        self.btnHome.setText(_translate("MainWindow", "Home"))
        item = self.tableMon.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã môn"))
        item = self.tableMon.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên môn"))
        item = self.tableMon.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Số TC"))

def closeWindow():
    global myDB
    myDB.disconnect()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    app.lastWindowClosed.connect(closeWindow)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

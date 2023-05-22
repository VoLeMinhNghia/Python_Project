from PyQt6 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
from database import *

class Main_Handle(Ui_MainWindow):
    def __init__(self):
        self.setupUi(MainWindow)

        myDB = MY_DB()
        myDB.connect()
        khoaTable = myDB.select_all_khoa()

        # self.tableKhoa.setRowCount(0)
        # for row_num, row_data in enumerate(khoaTable):
        #     print(row_num)
        #     print(row_data)
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main_Handle()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

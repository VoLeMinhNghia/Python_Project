from database import *

mydb = MY_DB()

mydb.connect()
mydb.create_tables()
# mydb.update_nghanh("Kế Toán", "KT")
# mydb.update_diem(10,10,10, 3, 2)
# mydb.delete_nghanh("LKD")
# all_sv = mydb.select_all_sinhvien()
# print(all_sv)
# print(mydb.select_khoa_by_id("CNTT"))
# print(mydb.select_diem_by_ids(1,1))
# mydb.insert_nienkhoa("Khóa 66")
# mydb.insert_nghanh("ABC", "CNTT", "TEST")
# mydb.delete_nienkhoa(7)
# print(mydb.select_sinhvien_by_id(1).fetchone())
# print(mydb.select_khoa_by_id("CNTT").fetchone())
# print(mydb.select_diem_by_ids(1,1).fetchone())
# mydb.insert_lop("62.CNTT-CLC", "CNTT", 2, "62 Công Nghệ Thông Tin - CLC")
# mydb.insert_lop("62.QTKD-CLC", "CNTT", 2, "62 Quản Trị Kinh Doanh - CLC")
# mydb.insert_diem(4,1,3,9,8,7)
# mydb.insert_diem(4,2,3,7,3,5)
# mydb.insert_diem(10,2,3,7,7,7)
#print(mydb.select_khoa_by_id("LU").fetchone())
mydb.disconnect()
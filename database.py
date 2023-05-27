import sqlite3

class MY_DB():
    def __init__(self):
        self.connect()

    def connect(self):
        self.conn = sqlite3.connect("qlsv_data.db")
        self.cur = self.conn.cursor()

    def create_tables(self):
        # Create KHOA table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS KHOA (
                                MaKhoa NVARCHAR(10) PRIMARY KEY NOT NULL,
                                TenKhoa NVARCHAR(50) NOT NULL
                                );""")
        # Create NGHANH table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS NGHANH (
                                MaNghanh NVARCHAR(10) PRIMARY KEY NOT NULL,
                                MaKhoa NVARCHAR(10) REFERENCES KHOA(MaKhoa) NOT NULL,
                                TenNghanh NVARCHAR(50) NOT NULL
                                );""")
        # Create NIENKHOA table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS NIENKHOA (
                                MaNienKhoa INTEGER PRIMARY KEY AUTOINCREMENT,
                                TenNienKhoa NVARCHAR(50) NOT NULL
                                );""")
        # Create HOCKY table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS HOCKY (
                                MaHocKy INTEGER PRIMARY KEY AUTOINCREMENT,
                                TenHocKy NVARCHAR(50) NOT NULL
                                );""")
        # Create LOP table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS LOP (
                                MaLop NVARCHAR(20) PRIMARY KEY NOT NULL,
                                MaNghanh NVARCHAR(10) REFERENCES NGHANH(MaNghanh) NOT NULL,
                                MaNienKhoa INT REFERENCES NIENKHOA(MaNienKhoa) NOT NULL,
                                TenLop NVARCHAR(100) NOT NULL
                                );""")
        # Create SINHVIEN table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS SINHVIEN (
                                MaSV INTEGER PRIMARY KEY AUTOINCREMENT,
                                MaLop NVARCHAR(20) REFERENCES LOP(MaLop) NOT NULL,
                                HoTen NVARCHAR(100) NOT NULL,
                                NgaySinh DATE NOT NULL,
                                GioiTinh BIT DEFAULT 1 NOT NULL,
                                DanToc NVARCHAR(50) NOT NULL,
                                DiaChi NVARCHAR(100) NOT NULL,
                                SoDienThoai VARCHAR(12) NOT NULL
                                );""")
        # Create MONHOC table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS MONHOC (
                                MaMon INTEGER PRIMARY KEY AUTOINCREMENT,
                                TenMon NVARCHAR(100) NOT NULL,
                                SoTC INT NOT NULL
                                );""")
        # Create DIEM table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS DIEM (
                                MaSV INT REFERENCES SINHVIEN(MaSV) NOT NULL,
                                MaHocKy INT REFERENCES HOCKY(MaHocKy) NOT NULL,
                                MaMon INT REFERENCES MONHOC(MaMon) NOT NULL,
                                DiemQuaTrinh DECIMAL(3,1) NOT NULL,
                                DiemGiuaKy DECIMAL(3, 1) NOT NULL,
                                DiemCuoiKy DECIMAL(3, 1) NOT NULL,
                                PRIMARY KEY (MaSV, MaHocKy, MaMon)
                                );""")
        self.conn.commit()

    def insert_data(self):
        self.cur.execute("""INSERT INTO KHOA VALUES
                                ("CNTT", "Công Nghệ Thông Tin"),
                                ("QTKD", "Quản Trị Kinh Doanh"),
                                ("NN", "Ngoại Ngữ"),
                                ("LU", "Luật");
                        """)

        self.cur.execute("""INSERT INTO NGHANH VALUES
                                ("CNTT", "CNTT", "Công Nghệ Thông Tin"),
                                ("HTTT", "CNTT", "Hệ Thông Thông Tin Quản Lý"),
                                ("QTKD", "QTKD", "Quản Trị Kinh Doanh"),
                                ("KT", "QTKD", "Kế Toán"),
                                ("LKD", "LU", "Luật Kinh Doanh");
                        """)

        self.cur.execute("""INSERT INTO NIENKHOA(TenNienKhoa) VALUES
                                ("Khóa 61"), ("Khóa 62"), ("Khóa 63"), ("Khóa 64");
                        """)

        self.cur.execute("""INSERT INTO HOCKY(TenHocKy) VALUES
                                ("Học Kỳ 1"), ("Học Kỳ 2"), ("Học Kỳ Hè");
                        """)

        self.cur.execute("""INSERT INTO LOP VALUES
                                ("62.CNTT-CLC", "CNTT", 2, "62 Công Nghệ Thông Tin CLC"),
                                ("62.QTKD-CLC", "QTKD", 2, "62 Quản Trị Kinh Doanh CLC"),
                                ("61.QTKD", "QTKD", 1, "61 Quản Trị Kinh Doanh");
                        """)

        self.cur.execute("""INSERT INTO SINHVIEN(MaLop, HoTen, NgaySinh, GioiTinh, DanToc, DiaChi, SoDienThoai) VALUES
                                ("62.CNTT-CLC", "Võ Lê Minh Nghĩa", CAST("2002-06-17" AS date), 1, "Kinh", "17/14 Cao Văn Bé", "0523053534"),
                                ("62.QTKD-CLC", "Nguyễn Thị Thu Trang", CAST("2002-03-22" AS date), 0, "Kinh", "24/9 Huỳnh Thúc Kháng", "0583958695"),
                                ("61.QTKD", "Nguyễn Thị Thanh Hằng", CAST("2001-02-14" AS date), 0, "Kinh", "24/12 Trần Não", "0962154783");
                        """)
        
        self.cur.execute("""INSERT INTO DIEM VALUES
                                (1, 1, 1, 8, 7, 10),
                                (3, 1, 2, 9, 7, 10),
                                (2, 2, 3, 6, 9, 8);
                        """)

        self.conn.commit()
    
    #-------------------------------INSERT--------------------------------------------

    def insert_khoa(self, makhoa, tenkhoa):
        self.cur.execute("INSERT INTO KHOA VALUES (?, ?)", (makhoa, tenkhoa))
        self.conn.commit()
    
    def insert_nghanh(self, manghanh, makhoa, tennghanh):
        self.cur.execute("INSERT INTO NGHANH VALUES (?, ?, ?)", (manghanh, makhoa, tennghanh))
        self.conn.commit()

    def insert_hocky(self, tenhocky):
        self.cur.execute("INSERT INTO HOCKY (TenHocKy) VALUES (?)", (tenhocky,))
        self.conn.commit()
    
    def insert_nienkhoa(self, nienkhoa):
        self.cur.execute("INSERT INTO NIENKHOA (TenNienKhoa) VALUES (?)", (nienkhoa,))
        self.conn.commit()

    def insert_lop(self, malop, manghanh, manienkhoa, tenlop):
        self.cur.execute("INSERT INTO LOP (MaLop, MaNghanh, MaNienKhoa, TenLop) VALUES (?, ?, ?, ?)", (malop, manghanh, manienkhoa, tenlop))
        self.conn.commit()
    
    def insert_monhoc(self, tenmh, sotc):
        self.cur.execute("INSERT INTO MONHOC (TenMon, SoTC) VALUES (?, ?)", (tenmh, sotc))
        self.conn.commit()

    def insert_sinhvien(self, malop, hoten, ngaysinh, gioitinh, dantoc, diachi, sodt):
        self.cur.execute("INSERT INTO SINHVIEN (MaLop, HoTen, NgaySinh, GioiTinh, DanToc, DiaChi, SoDienThoai) VALUES (?, ?, ?, ?, ?, ?, ?)", (malop, hoten, ngaysinh, gioitinh, dantoc, diachi, sodt))
        self.conn.commit()

    def insert_diem(self, masv, mahocky, mamon, diemqt, diemgk, diemck):
        self.cur.execute("INSERT INTO DIEM VALUES (?, ?, ?, ?, ?, ?)", (masv, mahocky, mamon, diemqt, diemgk, diemck))
        self.conn.commit()

    #-------------------------------UPDATE--------------------------------------------

    def update_khoa(self, tenkhoa, makhoa):
        self.cur.execute("UPDATE KHOA SET TenKhoa = ? WHERE MaKhoa = ?", (tenkhoa, makhoa))
        self.conn.commit()

    def update_nghanh(self, tennghanh, manghanh):
            self.cur.execute("UPDATE NGHANH SET TenNghanh = ? WHERE MaNghanh = ?", (tennghanh, manghanh))
            self.conn.commit()

    def update_hocky(self, tenhocky, mahocky):
            self.cur.execute("UPDATE HOCKY SET TenHocKy = ? WHERE MaHocKy = ?", (tenhocky, mahocky))
            self.conn.commit()

    def update_nienkhoa(self, tennienkhoa, manienkhoa):
            self.cur.execute("UPDATE NIENKHOA SET TenNienKhoa = ? WHERE MaNienKhoa = ?", (tennienkhoa, manienkhoa))
            self.conn.commit()

    def update_lop(self, tenlop, malop):
            self.cur.execute("UPDATE LOP SET TenLop = ? WHERE MaLop = ?", (tenlop, malop))
            self.conn.commit()

    def update_monhoc(self, tenmh, sotc, mamon):
            self.cur.execute("UPDATE MONHOC SET TenMon = ?, SoTC = ? WHERE MaMon = ?", (tenmh, sotc, mamon))
            self.conn.commit()

    def update_sinhvien(self, hoten, ngaysinh, gioitinh, dantoc, diachi, sodt, masv):
            self.cur.execute("UPDATE SINHVIEN SET HoTen = ?, NgaySinh = ?, GioiTinh = ?, DanToc = ?, DiaChi = ?, SoDienThoai = ? WHERE MaSV = ?", (hoten, ngaysinh, gioitinh, dantoc, diachi, sodt, masv))
            self.conn.commit()

    def update_diem(self, diemqt, diemgk, diemck, masv, mamon):
            self.cur.execute("UPDATE DIEM SET DiemQuaTrinh = ?, DiemGiuaKy = ?, DiemCuoiKy = ? WHERE MaSV = ? AND MaMon = ?", (diemqt, diemgk, diemck, masv, mamon))
            self.conn.commit()
        
    #----------------------------SELECT BY ID-----------------------------------------

    def select_khoa_by_id(self, makhoa):
        self.cur.execute("SELECT * FROM KHOA WHERE MaKhoa = ?", (makhoa,))
        rows = self.cur
        return rows

    def select_nghanh_by_id(self, manghanh):
        self.cur.execute("SELECT * FROM NGHANH WHERE MaNghanh = ?", (manghanh,))
        rows = self.cur
        return rows

    def select_hocky_by_id(self, mahocky):
        self.cur.execute("SELECT * FROM HOCKY WHERE MaHocKy = ?", (mahocky,))
        rows = self.cur
        return rows

    def select_nienkhoa_by_id(self, manienkhoa):
        self.cur.execute("SELECT * FROM NIENKHOA WHERE MaNienKhoa = ?", (manienkhoa,))
        rows = self.cur
        return rows

    def select_lop_by_id(self, malop):
        self.cur.execute("SELECT * FROM LOP WHERE MaLop = ?", (malop,))
        rows = self.cur
        return rows

    def select_monhoc_by_id(self, mamon):
        self.cur.execute("SELECT * FROM MONHOC WHERE MaMon = ?", (mamon,))
        rows = self.cur
        return rows

    def select_sinhvien_by_id(self, masv):
        self.cur.execute("SELECT * FROM SINHVIEN WHERE MaSV = ?", (masv,))
        rows = self.cur
        return rows
    
    def select_sinhvien_by_lop(self, malop):
        self.cur.execute("SELECT * FROM SINHVIEN WHERE MaLop = ?", (malop,))
        rows = self.cur
        return rows
    
    def select_sinhvien_by_name(self, name):
        query = "SELECT * FROM SINHVIEN WHERE HoTen LIKE ?"
        name_pattern = f"%{name}%"
        self.cur.execute(query, (name_pattern,))
        rows = self.cur
        return rows
    
    def select_diem_by_ids(self, masv, mahocky, mamon):
        self.cur.execute("SELECT * FROM DIEM WHERE MaSV = ? AND MaHocKy = ? AND MaMon = ?", (masv, mahocky, mamon))
        rows = self.cur
        return rows
    
    def select_diem_by_mon(self, mamon):
        self.cur.execute("SELECT * FROM DIEM WHERE MaMon = ?", (mamon,))
        rows = self.cur
        return rows
    
    def select_diem_by_hocky(self, mahocky):
        self.cur.execute("SELECT * FROM DIEM WHERE MaHocKy = ?", (mahocky,))
        rows = self.cur
        return rows

    def select_diem_by_hockyAndMon(self, mahocky, mamon):
        self.cur.execute("SELECT * FROM DIEM WHERE MaHocKy = ? AND MaMon = ?", (mahocky, mamon))
        rows = self.cur
        return rows


    #-----------------------------SELECT ALL------------------------------------------

    def select_all_khoa(self):
        self.cur.execute("SELECT * FROM KHOA")
        rows = self.cur
        return rows

    def select_all_nghanh(self):
        self.cur.execute("SELECT * FROM NGHANH")
        rows = self.cur
        return rows

    def select_all_hocky(self):
        self.cur.execute("SELECT * FROM HOCKY")
        rows = self.cur
        return rows

    def select_all_nienkhoa(self):
        self.cur.execute("SELECT * FROM NIENKHOA")
        rows = self.cur
        return rows

    def select_all_lop(self):
        self.cur.execute("SELECT * FROM LOP")
        rows = self.cur
        return rows

    def select_all_monhoc(self):
        self.cur.execute("SELECT * FROM MONHOC")
        rows = self.cur
        return rows

    def select_all_sinhvien(self):
        self.cur.execute("SELECT * FROM SINHVIEN")
        rows = self.cur
        return rows

    def select_all_diem(self):
        self.cur.execute("SELECT * FROM DIEM")
        rows = self.cur
        return rows

    #-------------------------------DELETE--------------------------------------------

    def delete_khoa(self, makhoa):
        self.cur.execute("DELETE FROM KHOA WHERE MaKhoa = ?", (makhoa,))
        self.conn.commit()

    def delete_nghanh(self, manghanh):
        self.cur.execute("DELETE FROM NGHANH WHERE MaNghanh = ?", (manghanh,))
        self.conn.commit()

    def delete_hocky(self, mahocky):
        self.cur.execute("DELETE FROM HOCKY WHERE MaHocKy = ?", (mahocky,))
        self.conn.commit()

    def delete_nienkhoa(self, manienkhoa):
        self.cur.execute("DELETE FROM NIENKHOA WHERE MaNienKhoa = ?", (manienkhoa,))
        self.conn.commit()

    def delete_lop(self, malop):
        self.cur.execute("DELETE FROM LOP WHERE MaLop = ?", (malop,))
        self.conn.commit()

    def delete_monhoc(self, mamon):
        self.cur.execute("DELETE FROM MONHOC WHERE MaMon = ?", (mamon,))
        self.conn.commit()

    def delete_sinhvien(self, masv):
        self.cur.execute("DELETE FROM SINHVIEN WHERE MaSV = ?", (masv,))
        self.conn.commit()

    def delete_diem(self, masv, mamon):
        self.cur.execute("DELETE FROM DIEM WHERE MaSV = ? AND MaMon = ?", (masv, mamon))
        self.conn.commit()

#----------------------------------------Get------------------------------------------------------
    
    def get_ten_nghanh(self, maNghanh):
        self.cur.execute("SELECT TenNghanh FROM NGHANH WHERE MaNghanh = ?", (maNghanh,))
        result = self.cur.fetchone()
        if result:
            return result[0]
        else:
            return ""
        
    def get_ten_sinhvien(self, maSV):
        self.cur.execute("SELECT HoTen FROM SINHVIEN WHERE MaSV = ?", (maSV,))
        result = self.cur.fetchone()
        if result:
            return result[0]
        else:
            return ""

    def get_ten_nien_khoa(self, maNienKhoa):
        self.cur.execute("SELECT TenNienKhoa FROM NIENKHOA WHERE MaNienKhoa = ?", (maNienKhoa,))
        result = self.cur.fetchone()
        if result:
            return result[0]
        else:   
            return ""
        
    def get_ten_hoc_ky(self, maHocKy):
        self.cur.execute("SELECT TenHocKy FROM HOCKY WHERE MaHocKy = ?", (maHocKy,))
        result = self.cur.fetchone()
        if result:
            return result[0]
        else:
            return ""
        
    def get_ten_mon_hoc(self, maMonHoc):
        self.cur.execute("SELECT TenMon FROM MONHOC WHERE MaMon = ?", (maMonHoc,))
        result = self.cur.fetchone()
        if result:
            return result[0]
        else:
            return ""

    def disconnect(self):
        self.conn.close()

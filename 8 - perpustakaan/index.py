import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'kuliah-pbop-perpus')

cursor = db.cursor()

class PerpusItem:

    def __init__(self, judul, subjek, lokasi, info):

        self.judul = judul
        self.subjek = subjek
        self.lokasi = lokasi
        self.info = info

class Buku(PerpusItem):

    def __init__(self, judul, subjek, lokasi, info, isbn, pengarang, jmlhal, ukuran):
        super().__init__(judul, 'Buku', lokasi, info)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlhal = jmlhal
        self.ukuran = ukuran

        cursor.execute(f"INSERT INTO item (judul, subjek, lokasi, info, isbn, pengarang, jumlah_halaman, ukuran, volume, issue,genre) VALUES ('{self.judul}', '{self.subjek}','{self.lokasi}','{self.info}','{self.isbn}','{self.pengarang}','{self.jmlhal}','{self.ukuran}','NULL','NULL','NULL')")

        db.commit()

    
class Majalah(PerpusItem):
    def __init__(self, judul, subjek, lokasi, info, volume, issue):
        super().__init__(judul, 'Majalah', lokasi, info)
        self.volume = volume
        self.issue = issue

        cursor.execute(f"INSERT INTO item (judul, subjek, lokasi, info, isbn, pengarang, jumlah_halaman, ukuran, volume, issue,genre) VALUES ('{self.judul}', '{self.subjek}','{self.lokasi}','{self.info}','NULL','NULL','NULL','NULL','{self.volume}','{self.issue}','NULL')")

        db.commit()

class Komik(PerpusItem):
    def __init__(self, judul, subjek, lokasi, info, pengarang, jumlah_halaman, genre):
        super().__init__(judul, 'Komik', lokasi, info)
        self.genre = genre
        self.pengarang = pengarang
        self.jumlah_halaman = jumlah_halaman

        cursor.execute(f"INSERT INTO item (judul, subjek, lokasi, info, isbn, pengarang, jumlah_halaman, ukuran, volume, issue,genre) VALUES ('{self.judul}', '{self.subjek}','{self.lokasi}','{self.info}','NULL','{self.pengarang}','{self.jumlah_halaman}','NULL','NULL','NULL','NULL')")

        db.commit()


print("########## Sistem Informasi Perpustakaan ##########")

while True:

    print("########## Daftar Menu Aplikasi ##########")
    print('''
    1. Tampilkan Data Item
    2. Input Data Item baru
    ''')

    menu = input("Pilih Menu : ")
    if menu == '1':
        print("Data Semua Item yang ada di perpustakaan")
        cursor.execute("SELECT * FROM item")
        for item in cursor.fetchall():
            if item[2] == 'buku':
                print(f'''
                    Judul           = {item[1]}
                    Subjek          = {item[2]}
                    Lokasi          = Rak {item[3]}
                    Info            = Rak {item[4]}
                    ISBN            = {item[5]}
                    Pengarang       = {item[6]}
                    Jumlah Halaman  = {item[7]}
                    Ukuran          = {item[8]}
                    Ditambahkan     = {item[12]}
                    ________________
                ''')
            elif item[2] == 'majalah':
                print(f'''
                    Judul           = {item[1]}
                    Subjek          = {item[2]}
                    Lokasi          = Rak {item[3]}
                    Info            = Rak {item[4]}
                    Volume          = {item[9]}
                    Issue           = {item[10]}
                    Ditambahkan     = {item[12]}
                    ________________
                ''')
            elif item[2] == 'komik':
                print(f'''
                    Judul           = {item[1]}
                    Subjek          = {item[2]}
                    Lokasi          = Rak {item[3]}
                    Info            = Rak {item[4]}
                    Pengarang       = {item[6]}
                    Jumlah Halaman  = {item[7]}
                    Genre           = {item[11]}
                    Ditambahkan     = {item[12]}
                    ________________
                ''')


    elif menu == '2':
        print("Pilih jenis item yang ingin anda masukkan")
        print('''
        1. Buku
        2. Majalah
        3. Komik
        ''')

        jenis = input()
        
        if jenis == '1':
            judul = input("Masukkan Judul : ")
            lokasi = input("Masukkan Lokasi nomor Rak : ")
            isbn = input("Masukkan nomor ISBN : ")
            pengarang = input("Masukkan nama pengarang : ")
            jumlah_halaman = input("Masukkan jumlah halaman : ")
            ukuran = input("Masukkan ukuran item : ")

            Buku(judul, 'buku',lokasi, 'ada', isbn, pengarang, jumlah_halaman,ukuran)
            print("Data berhasil ditambahkan")
        
        elif jenis == '2':
            judul = input("Masukkan Judul : ")
            lokasi = input("Masukkan Lokasi nomor Rak : ")
            volume = input("Masukkan Volume Majalah: ")
            issue = input("Masukkan Issue Majalah : ")
        
            Majalah(judul, 'majalah', lokasi, 'ada', volume, issue)
            print("Data berhasil ditambahkan")

        elif jenis == '3':
            judul = input("Masukkan Judul : ")
            lokasi = input("Masukkan Lokasi nomor Rak : ")
            pengarang = input("Masukkan nama pengarang : ")
            jumlah_halaman = input("Masukkan jumlah halaman : ")
            genre = input("Masukkan genre : ")

            Komik(judul,'komik',lokasi, 'ada', pengarang,jumlah_halaman, genre)
            print("Data berhasil ditambahkan")

        else :
            print("Jenis tidak terdaftar")


    else:
        print("Menu tidak terdaftar")
        
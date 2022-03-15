# Esa Age 
# 5210411159

class mahasiswa:
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

class siswa1(mahasiswa):
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

    def detSiswa1(self):
        print(self.nama, 'Alamat : Ngawi')

class siswa2(mahasiswa):
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

    def detSiswa2(self):
        print(self.nama, 'Jurusan : Informatika')

m1 = siswa1('Esa Age', 5210411159)
m2 = siswa2('Danu Dwiki',5210411165)

print(m1.nim)
m1.detSiswa1()

print(m2.nama)
m2.detSiswa2()
class Mahasiswa:
    def __init__(self, nama, nim, prodi, thn_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk


m1 = Mahasiswa('Udin', '10120371', 'Sistem Informasi', 2020)
m2 = Mahasiswa('Esa Age', '5210411159', 'Informatika', 2021)
m3 = Mahasiswa('Danu Dwiki Laksana', '5210411165', 'Informatika', 2021)


data_mahasiswa = [m1, m2, m3]

print('Daftar Mahasiswa')
for i in data_mahasiswa:
        print(f'{i.nama} adalah mahasiswa {i.prodi} angkatan {i.thn_masuk} dengan nim {i.nim}')
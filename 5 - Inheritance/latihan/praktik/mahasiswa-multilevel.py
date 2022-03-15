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

class siswa2(mahasiswa):
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim


m1 = mahasiswa('Esa Age', 5210411159)
m2 = siswa1('Danu Dwiki', 5210411165)
m3 = siswa2('Bellaa Triana',5210411175)

print(m1.nama , m1.nim)
print(m2.nama)
print(m3.nim)
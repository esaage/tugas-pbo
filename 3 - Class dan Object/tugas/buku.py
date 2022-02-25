class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit


buku1 = Buku('Tenggelamnya Kapal Van Der Wijck', 'Hamka', 1938)
buku2 = Buku('Psychology Of Money', 'Morgan Housel', 2022)
buku3 = Buku('The Intelligent Investor', 'Benjamin Graham', 1949)


data_buku = [buku1, buku2, buku3]

print('Daftar Buku')
for i in data_buku:
    print(
        f'Buku {i.judul} karangan {i.pengarang} pertama kali diterbitkan tahun {i.tahun_terbit}')
class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, harga):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.__harga = harga


buku1 = Buku('Tenggelamnya Kapal Van Der Wijck', 'Hamka', 1938, 20000)
buku2 = Buku('Psychology Of Money', 'Morgan Housel', 2022, 100000)
buku3 = Buku('The Intelligent Investor', 'Benjamin Graham', 1949, 80000)


data_buku = [buku1, buku2, buku3]

print('Daftar Buku')
for i in data_buku:
    print(
        f'Buku {i.judul} karangan {i.pengarang} pertama kali diterbitkan tahun {i.tahun_terbit} dengan harga Rp. {i._Buku__harga}')

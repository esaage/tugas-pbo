class menuMinuman:
    def __init__(self, nama, deskripsi, harga, ukuran):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.__ukuran = ukuran


mnm1 = menuMinuman('Jus Jambu', 'Jus jambu merah tanpa gula', 8500, 'Sedang')
mnm2 = menuMinuman('Jus Alpukat Ori','Jus alpukat dengan tambahan air gula merah', 15000, 'Besar')
mnm3 = menuMinuman('Jus Alpukat Xtra Milk','Jus alpukat dengan campuran susu coklat dan tamburan kepingan choco', 15000, 'Kecil')
mnm4 = menuMinuman('Red & Smoothie', 'Smoothie pisang susu dan strawberry', 17500, 'Sedang')
mnm5 = menuMinuman('Doger Ice Cilacap', 'Doger Ice Cilacap Vibes', 17500, 'Besar')
mnm6 = menuMinuman('Tea Ice Angkringan', 'Tea Ice Cool And Taste', 17500, 'Sedang')


pilihanMenu = [mnm1, mnm2, mnm3, mnm4, mnm5, mnm6]
print('Daftar Menu Healthy Fruits')

for i in pilihanMenu:
    print('{} - ukuran {} -  harga Rp. {} , {}'.format(i.nama, i.harga, i.deskripsi, i._menuMinuman__ukuran))
# Overriding

class ComputerPart:
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
    
class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, harga, jumlah_core, speed):
        super().__init__(pabrikan, nama, 'processor', harga)
        self.jumlah_core = jumlah_core
        self.speed = speed
    
    # method overloading
    def fungsi(self):
        print(f'{self.jenis} adalah komponen yang berfungsi untuk menjalankan proses komputasi pada sebuah komputer')

class RandomAccessMemory(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan, nama, 'RAM', harga)
        self.kapasitas = kapasitas
    
    # method overloading
    def fungsi(self):
        print(f'{self.jenis} berfungsi sebagai memori sementara pada komputer')

class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm):
        super().__init__(pabrikan, nama, 'HarddiskSATA', harga)
        self.kapasitas = kapasitas
        self.rpm = rpm

    # method overloading
    def fungsi(self):
        print(f'{self.jenis}  itu gunanya untuk tempat menyimpan file secara permanent pada komputer')

p = Processor('Intel', 'Core i9', 4000000, 4,'4 GHZ')
m = RandomAccessMemory('Sandisk', 'DD4 4 SECEPAT KILAT', 800000,'32 GB')
hdd = HardDiskSATA('WD', 'WD Green', 1200000, '1000 GB',7200)

parts = [p,m,hdd]
for part in parts:
    print('{} {} pabrikan {}'. format(part.jenis, part.nama, part.pabrikan))
    part.fungsi()
    print("")
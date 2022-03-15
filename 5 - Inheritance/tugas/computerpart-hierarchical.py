# 5210411159
# Esa Age

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
    
    def keterangan(self):
        print(f'''
        Nama        : {self.nama}
        Pabrikan    : {self.pabrikan}
        Jumlah Core : {self.jumlah_core} Core
        Speed       : {self.speed}
        Harga       : {self.harga}
        ''')


class RAM(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan, nama, 'RAM', harga)
        self.kapasitas = kapasitas
    
    def keterangan(self):
        print(f'''
        Nama        : {self.nama}
        Pabrikan    : {self.pabrikan}
        Kapasitas   : {self.kapasitas}
        Harga       : {self.harga}
        ''')

class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm):
        super().__init__(pabrikan, nama, 'SATA', harga)
        self.kapasitas = kapasitas
        self.rpm = rpm
    
    def keterangan(self):
        print(f'''
        Nama        : {self.nama}
        Pabrikan    : {self.pabrikan}
        Kapasitas   : {self.kapasitas}
        Speed       : {self.rpm} Rpm
        Harga       : {self.harga}
        ''')

processor = Processor('Intel', 'Core i9', 4000000, 4,'4 GHZ')
ram = RAM('Sandisk', 'DD4 4 SECEPAT KILAT', 800000,'32 GB')
hdd = HardDiskSATA('WD', 'WD Green', 1200000, '1000 GB',7200)

parts = [processor,ram,hdd]
for part in parts:
    print('{} {} pabrikan {}'. format(part.jenis, part.nama, part.pabrikan))
    print('Detail Part : ')
    part.keterangan()
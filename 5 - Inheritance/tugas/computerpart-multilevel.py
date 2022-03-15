# 5210411159
# Esa Age

# class parent
class ComputerPart:
    def __init__(self, jenis):
        self.jenis = jenis

# class child dari ComputerPart
class Machine(ComputerPart):
    def __init__(self, nama, pabrikan, jenis):
        super().__init__(jenis)
        self.nama = nama
        self.pabrikan = pabrikan

# class child dari Storage
class Processor(Machine):
    def __init__(self, nama, pabrikan,speed, jumlah_core):
        super().__init__(nama, pabrikan,'Processor')
        self.speed = speed
        self.jumlah_core = jumlah_core


part = Processor('Intel i9','INTEL','10000 Ghz',4)

print(f'Komputer dengan mesin {part.jenis} bermerek {part.pabrikan} dengan tipe {part.nama} yang mempunyai kecepatan {part.speed} dan berjumlah {part.jumlah_core} core' )
# 5210411159
# Esa Age
    
class Processor():
    def __init__(self, namaProcessor):
        self.processor = namaProcessor

class RAM():
    def __init__(self, kapasitasRam):
        self.ram = kapasitasRam

class HardDisk():
    def __init__(self, kapasitasHarddisk):
        self.hdd = kapasitasHarddisk

class ComputerPart(Processor, RAM, HardDisk):
    def __init__(self, namaProcessor, kapasitasRam, kapasitasHarddisk):
        Processor.__init__(self, namaProcessor)
        RAM.__init__(self, kapasitasRam)
        HardDisk.__init__(self, kapasitasHarddisk)


computer = ComputerPart('Intel core i9 18291', '16', 1000)

print(f'Komputer ini mempunyai processor {computer.processor}, RAM {computer.ram}, dan hardisk berkapasistas {computer.hdd}')
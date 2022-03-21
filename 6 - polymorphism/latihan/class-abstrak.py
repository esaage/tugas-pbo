from abc import ABC, abstractmethod

class bentuk(ABC):
    @abstractmethod
    def luas(self):
        return self.__sisi * self.__sisi
    
    @abstractmethod
    def keliling(self):
        return 4 * self.__sisi

class Persegi(bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.__sisi * self.__sisi
    
    def keliling(self):
        return 4 * self.__sisi

persegi = Persegi(6)
print(persegi.luas())
print(persegi.keliling())
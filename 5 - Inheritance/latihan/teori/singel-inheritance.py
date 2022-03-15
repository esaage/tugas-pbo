# Esa Age 
# 5210411159

# Class Parent 
class hewan:
    def bersuara(self):
        print("Kucing Bersuara ")


# child class dari hewan
class kucing(hewan):
    def suara(self):
        print('Meong')


# Objek 
k=kucing()
k.suara()
k.bersuara()
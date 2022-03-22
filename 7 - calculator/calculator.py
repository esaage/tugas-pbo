# Kelompok 4
# Esa Age - 5210411159
# Danu Dwiki - 5210411165
# Veratina Fridayanti - 5210411173
# Bella Triana - 5210411175

from colorama import Fore, Style

class calculator:
    def __init__(self,a ,b) -> None:
        self.a = a
        self.b =b
        
    def tambah(self):
        return self.a + self.b

    def kurang(self):
        return self.a - self.b

    def kali(self):
        return self.a * self.b
    
    def bagi(self):
        return self.a / self.b


while True:
    reset = False
    a = float(input('=> Masukan Nilai : '))
    while reset != True:
        print(f'''
        {Fore.BLUE}1. Tambah (+){Style.RESET_ALL}
        {Fore.RED}2. Kurang (-){Style.RESET_ALL}
        {Fore.YELLOW}3. Kali (x){Style.RESET_ALL}
        {Fore.GREEN}4. Bagi (/){Style.RESET_ALL}
        5. Reset\n''')
        
        oper = float(input('Operasi : '))
        if oper == 1:
            b = float(input('-> Masukan Nilai : '))
            calcu = calculator(a,b)
            a = calcu.tambah()
            print(Fore.BLUE+f'Hasil : {a}'+Style.RESET_ALL)
        
        elif oper == 2:
            b = float(input('-> Masukan Nilai : '))
            calcu = calculator(a,b)
            a = calcu.kurang()
            print(Fore.RED+f'Hasil : {a}'+Style.RESET_ALL)
        
        elif oper == 3:
            b = float(input('-> Masukan Nilai : '))
            calcu = calculator(a,b)
            a = calcu.kali()
            print(Fore.YELLOW+f'Hasil : {a}'+Style.RESET_ALL)
        
        elif oper == 4:
            b = float(input('-> Masukan Nilai : '))
            calcu = calculator(a,b)
            a = calcu.bagi()
            print(Fore.GREEN+f'Hasil : {a}'+Style.RESET_ALL)

        elif oper == 5:
            reset = True
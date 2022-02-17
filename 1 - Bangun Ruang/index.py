from colorama import init, Fore
init(convert=True)

# function for calculate luas bangun ruang 

def Persegi():
    print(Fore.CYAN, 'Rumus Persegi "s x s"', Fore.RESET)
    sisi = int(input(" Masukkan Sisi Persegi : "))
    print(Fore.YELLOW,"Luas Persegi tersebut adalah : ", sisi*sisi, Fore.RESET)

def PersegiPanjang():
    print(Fore.CYAN, 'Rumus Persegi "p x l"', Fore.RESET)
    panjang = int(input(" Masukkan Panjang Persegi Panjang (p): "))
    lebar = int(input(" Masukkan Lebar Persegi (l): "))
    print(Fore.YELLOW,"Luas Persegi Panjang tersebut adalah : ", panjang*lebar, Fore.RESET)

def Lingkaran():
    print(Fore.CYAN, 'Rumus Lingkaran "phi x r x r"', Fore.RESET)
    
    jari = int(input(" Masukkan Jari-jari Lingkaran (r): "))
    print(Fore.YELLOW,"Luas Lingkaran tersebut adalah : ",3.14 * jari * jari, Fore.RESET)

def SegiTiga():
    print(Fore.CYAN, 'Rumus Segitiga "1/2 x a x t"', Fore.RESET)
    
    alas = int(input(" Masukkan Alas Segitiga (a): "))
    tinggi = int(input(" Masukkan Tinggi Segitiga (t): "))
    print(Fore.YELLOW,"Luas Lingkaran tersebut adalah : ", 0.5 * alas * tinggi, Fore.RESET)

pilihan = 0

while True:
    print(Fore.YELLOW, "\n******** APLIKASI MENGHITUNG BANGUN RUANG ********", Fore.RESET)
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Lingkaran")
    print("4. Segi Tiga")
    print("5. Keluar Aplikasi")
    pilihan = input("Masukkan pilihan bangun ruang anda:")


    if pilihan == '1':
        Persegi()

    elif pilihan == '2':
        PersegiPanjang()

    elif pilihan == '3':    
        Lingkaran()

    elif pilihan == '4' :
        SegiTiga()

    elif pilihan == '5':
        print("******** KELUAR APLIKASI ********")
        print("")
        break

    else:
        print("******** APLIKASI ERROR ********")
        print("Menu yang Anda pilih tidak terdaftar")
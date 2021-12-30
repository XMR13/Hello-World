#membuat program kalkulator sederhana

print("selamat datan di dalam programn kalkulator sederhana")


def pemilihanAngka():
    x = int(input("masukkan angka pertama " ))
    y = int(input("masukkan angka kedua "))

    return x,y

def pemilihanOperasi():
    a,b = pemilihanAngka()
    operasi = True
    while operasi:
        karakter = input("masukkan operasi yang diinginkan ")
        if karakter =='+':
            return a + b
        elif karakter =='-':
            return a - b
        elif karakter =='*':
            return a * b
        elif karakter =='/':
            return a / b
        else:
            print("invalid input, silahkan ulang kembali! \n")
            pass
    

def menampilkanHasil():
    angka = pemilihanOperasi()
    print("hasil yang didapat adalah ", angka)
    
def main():
    menampilkanHasil()

if __name__ == '__main__':
    main()

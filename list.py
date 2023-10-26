kendaraan = ['model x', 'beca','150', 'pink', '3' ]
print (kendaraan)
kendaraan.append(10000000)
kendaraan.append('kopling')
print(kendaraan)
kendaraan.append('bugati')
print(kendaraan)

luas_bangun = input ('menghitung')

luas_bangun = input("Pilih bangun datar (1: Persegi, 2: Lingkaran, 3: Segitiga): ")

match luas_bangun:
    case "1":
        sisi = int(input('Masukkan panjang sisi: '))
        persegi = sisi * sisi
        print('Hasil luas persegi:', persegi)
    case "2":
        r = int(input('Masukkan jari-jari lingkaran: '))
        V = 3.14
        luas = V * r * r 
        print('Hasil luas lingkaran:', luas)
    case "3":
        a = int(input('Masukkan panjang alas segitiga: '))
        t = int(input('Masukkan tinggi segitiga: '))
        luassegi = a * t / 2
        print('Hasil luas segitiga:', luassegi)
    case _:
        print('salah')


def genapganjil(bilangan):
    match bilangan % 2:
        case 0:
            print(f"{bilangan} genap.")
        case _:
            print(f"{bilangan}ganjil.")

bilangan = int(input("Masukkan bilangan: "))
genapganjil(bilangan)

print()
print("## nomor 1 ##")
def celcius_ke_fahrenheit(celcius):
    konversi=(celcius*9/5)+32
    return konversi


print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))



print()
print("## nomor 2 ##")
def ganjil_genap(bilangan):
    penentu = bilangan % 2 == 0
    return penentu
print(ganjil_genap(4)) 
print(ganjil_genap(7)) 


print()
print("## nomor 3 ##")
def nilai(keterangan):
    if keterangan >= 80:
        print("Lulus")
    elif keterangan <= 60:
        print("Gagal")
    else :
        print("Tidak valid")
nilai(90)
nilai(50)


print()
print("## nomor 4 ##")
def bilangan_ganjil(bzirr):
    return[i for i in range(1,bzirr,2)]
print(bilangan_ganjil(20))
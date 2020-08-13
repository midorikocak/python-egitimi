numaralar = []
girdi = 0

while (girdi != "tamam"):
    girdi = input("Bir sayı giriniz\n")
    if (girdi != "tamam"):
        numaralar.append(girdi)
    else:
        break

toplam = 0

for numara in numaralar:
    # print(toplam)
    toplam = toplam + float(numara)

print(toplam)

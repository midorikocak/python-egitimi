sayilar = (74, 82, 92, 64, 84, 90, 56, 94, 87, 73)

hepsiOnaBolunmus = map(lambda x: x / 10, sayilar)

filtreli = filter(lambda x: True if x > 7 else False, hepsiOnaBolunmus)

for sayi in filtreli:
    print(sayi)

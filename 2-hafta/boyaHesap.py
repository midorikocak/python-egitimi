# -*- coding: utf-8 -*-

en = float(input('Oda eni?\n'))
boy = float(input('Oda boyu?\n'))
yukseklik = float(input('Oda yuksekliği?\n'))

duvarAlani = (2 * ((boy + en) * yukseklik))

litre = 2.5
metrekare = 12.5
fiyat = 100

print(str(litre) + " boya " + str(metrekare) + " alanı boyar.")

# round(kusuratlanacakSayi, ondalik)

ihtiyac = round(((duvarAlani / metrekare) * litre), 2)
toplamFiyat = round(ihtiyac * fiyat, 2)
print("İhtiyacınız olan boya miktari " + str(ihtiyac) + " ve ödemeniz gereken miktar " + str(toplamFiyat) + "Türk Lirasıdır")

# -*- coding: utf-8 -*-

# float(virgulluSayiyaCevirilecekMetin)
# str(metineCevirilecekSayi)
# input(sorulacakSoru)
# round(cokOndalikliSayi, ondalikMiktari)

euroMiktar = float(input('Kaç euro çevireceksiniz?\n'))
euroFiyat = 7.81
liraMiktar = round(euroMiktar * euroFiyat, 2)

print('\n')
print("Döviz Hesabı")
print('------------\n')
print('Euro miktarı: ' + str(euroMiktar) + "€")
print('Euro Kur: ' + str(euroFiyat)+ "₺")
print(str(euroMiktar)+ "€, "+ str(euroFiyat)+"₺ kurdan "+ str(liraMiktar)+ "₺ eder.")

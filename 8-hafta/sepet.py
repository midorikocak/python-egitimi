urunler = {
  'Elma': {
    'fiyat': 5,
    'miktar': 3
  },
  'Armut': {
    'fiyat': 7,
    'miktar': 9
  },
  'Mandalina': {
    'fiyat': 4,
    'miktar': 6
  },
  'Kiraz': {
    'fiyat': 8,
    'miktar': 1
  },
}

cebimdekiPara = 100
sepet = {}

def sepeteUrunEkle(urunAdi, miktar):
  global cebimdekiPara

  if(not (urunAdi in urunler)):
    print("Ürün bulunamadı")
    return

  toplamFiyat = urunler[urunAdi]["fiyat"] * miktar

  if(urunler[urunAdi]["miktar"] < miktar):
    print("Yeterli ürün yok")
  elif(cebimdekiPara < toplamFiyat):
    print("Yeterli paranız yok")
  else:
    sepet[urunAdi] = urunler[urunAdi].copy()
    sepet[urunAdi]['miktar'] = miktar
    # urunler[urunAdi]['miktar'] = urunler[urunAdi]['miktar'] - miktar
    urunler[urunAdi]['miktar'] -= miktar
    cebimdekiPara = cebimdekiPara - toplamFiyat

sepeteUrunEkle("Muz", 3)

sepeteUrunEkle("Elma", 3)

sepeteUrunEkle("Mandalina", 6)

print(sepet)
print(cebimdekiPara)

def fisYazdir():
  fisToplam = 0
  for urunAdi in sepet:
    urunFiyat = sepet[urunAdi]["fiyat"]
    toplamFiyat = sepet[urunAdi]["fiyat"] * sepet[urunAdi]["miktar"]
    print("Ürün: " + urunAdi + " Adet: "+ str(sepet[urunAdi]["miktar"]) + " Toplam: " + str(toplamFiyat))
    # fisToplam = fisToplam + toplamFiyat
    fisToplam += toplamFiyat 

  print("Alışveriş Toplam: " + str(fisToplam))

fisYazdir()
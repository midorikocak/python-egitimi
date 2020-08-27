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

sepet = {}

cebimdekiPara = 100

def satinAl(urunAdi, para):
  if urunAdi in urunler:
    urunler[urunAdi]['miktar'] = urunler[urunAdi]['miktar'] - 1
    para = para - urunler[urunAdi]['fiyat']
    if urunAdi in sepet:
      sepet[urunAdi]['miktar'] = sepet[urunAdi]['miktar'] + 1
    else:
      sepet[urunAdi] = {}
      sepet[urunAdi]['miktar'] = 1
      sepet[urunAdi]['fiyat'] = urunler[urunAdi]['fiyat']
  else:
    print("Urun bulunamadı")
  return para

urunAdi = input("Bir ürün adı giriniz: \n")
cebimdekiPara = satinAl(urunAdi, cebimdekiPara)

urunAdi = input("Bir ürün adı giriniz: \n")
cebimdekiPara = satinAl(urunAdi, cebimdekiPara)

print(sepet)
print(cebimdekiPara)
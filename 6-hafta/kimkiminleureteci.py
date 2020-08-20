import random

erkekler = ["Ali", "Ahmet", "Mehmet", "Edward", "Hasan", "Nannan"]
kizlar = ["Ayşe", "Fatma", "Eda", "Jenny", "Betül"]
yerler = ["İstanbul'da", "Ankara'da", "sınıfta", "internet üzerinden", "otobüste", "trende"]
aktiviteler = ["göbek atıyor", "dans ediyor", "python çalışıyor", "çok eğleniyor", "hopluyor, zıplıyor", "konuşuyor"]

def rastgeleEleman(dizi):
  elemanSayisi = len(dizi)
  rastgeleIndex = random.randint(0, elemanSayisi - 1)
  return dizi[rastgeleIndex]

for i in range(1,11):
  kim = rastgeleEleman(erkekler)
  kiminle = rastgeleEleman(kizlar)
  nerede = rastgeleEleman(yerler)
  neYapiyor = rastgeleEleman(aktiviteler)

  print(kim + " " + kiminle + " ile "+ nerede + " " + neYapiyor)

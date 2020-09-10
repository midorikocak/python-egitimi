ogrenciler = [{
    "adi": "Deniz",
    "not": 74,
    "sonuc": ""
}, {
    "adi": "Mahir",
    "not": 82,
    "sonuc": ""
}, {
    "adi": "Ulaş",
    "not": 92,
    "sonuc": ""
}, {
    "adi": "Hüseyin",
    "not": 64,
    "sonuc": ""
}, {
    "adi": "İbrahim",
    "not": 84,
    "sonuc": ""
}, {
    "adi": "Erdal",
    "not": 90,
    "sonuc": ""
}, {
    "adi": "Sinan",
    "not": 56,
    "sonuc": ""
}, {
    "adi": "Taylan",
    "not": 94,
    "sonuc": ""
}, {
    "adi": "Yusuf",
    "not": 87,
    "sonuc": ""
}, {
    "adi": "Cihan",
    "not": 73,
    "sonuc": ""
}]


#for ogrenci in ogrenciler:
#  print(ogrenci["adi"])
#  print(ogrenci["not"])
#  if(ogrenci["not"] < 75):
#    ogrenci["sonuc"] = "kaldı"
#  else:
#    ogrenci["sonuc"] = "gecti"
#  print(ogrenci["sonuc"] + "\n")

def sonucYaz(ogrenci):
  if(ogrenci["not"] < 75):
    ogrenci["sonuc"] = "kaldı"
  else:
    ogrenci["sonuc"] = "gecti"
  return ogrenci

def gectiMiFiltre(ogrenci):
  if(ogrenci["sonuc"] == "kaldı"):
    return False
  else:
    return True

sonucluOgrenciler = map(sonucYaz, ogrenciler)

gecenler = filter(gectiMiFiltre, sonucluOgrenciler)

for ogrenci in gecenler:
  print(ogrenci)


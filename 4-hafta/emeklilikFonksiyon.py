import datetime

def emeklilikHesapla(dogumTarihi):
    tarihler = datetime.datetime.now()

    suAnkiYil = tarihler.year
    yas = suAnkiYil - dogumTarihi
    emeklilikYasi = 65
    kalanYil = emeklilikYasi - yas

    return kalanYil + suAnkiYil


print(emeklilikHesapla(1984))
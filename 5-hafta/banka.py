islem = input("Hangi işlemi yapmak istiyorsunuz?\n")

if (islem == "havale"):
    yanit = input("Kendi hesabınıza mı?\n")
    if (yanit == "evet"):
        print("Kendi hesabınıza havale yapıyorsunuz.")
    else:
        print("Başka hesaba havale yapıyorsunuz.")
elif (islem == "sifre"):
    print("Kart şifrenizi değiştiriyorsunuz")
elif (islem.lower() == "fatura"):
    kurum = input("Hangi kurum faturasını ödemek istiyorsunuz?")
    if (kurum == "su"):
        print("Su faturanızı ödüyorsunuz")
    elif (kurum == "elektrik"):
        print("Elektrik faturanızı ödüyorsunuz.")
    else:
      print("Kurum bulunamadı")
elif (islem == "döviz"):
    islemTipi = input("Döviz Al / Döviz sat?")
    if (islemTipi == "al"):
        print("Döviz alıyorsunuz")
    elif (islemTipi == "sat"):
        print("Döviz satıyorsunuz")
else:
    print("Böyle bir işlem bulunmamaktadır")

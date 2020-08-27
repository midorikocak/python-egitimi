import random

zorluk = input("Zorluk derecesi giriniz: (1,2,3)\n")

sonsayi = 10;

if(zorluk == 1):
  sonsayi = 10
elif(zorluk == 2):
  sonsayi = 100
elif(zorluk == 3):
  sonsayi = 1000

tahminEdilecek = random.randint(0, sonsayi)

tahmin = 0
deneme = 0

while (tahmin != tahminEdilecek):
    deneme = deneme + 1
    tahmin = int(input("Bir sayı giriniz:\n"))
    if (tahmin < tahminEdilecek):
        print('Küçük')
    elif (tahmin > tahminEdilecek):
        print('Büyük')
    else:
        print("Tebrikler " + str(deneme) + " adımda bildiniz.")
    
    if(deneme == 5):
      print("5 adımda bilemediniz. Kaybettiniz.")
      break

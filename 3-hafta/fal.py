import random
cevap = random.randint(0, 1)

soru = input('Neyi merak ediyorsun?\n')

if cevap == 0:
  print("Biraz daha beklemen lazım canım.")
else:
  print("Sen bu işi oldu bil.")
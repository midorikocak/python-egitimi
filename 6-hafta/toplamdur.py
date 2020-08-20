# sum(2*n),n=1..30 
# https://www.wolframalpha.com/input/?i=sum%282*n%29%2Cn%3D1..30
toplam = 0

for i in range(1, 31):
   toplam = toplam + (2 * i)

   if(toplam > 50):
     break


print(toplam)
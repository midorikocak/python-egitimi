ayIsimleri = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]

# Bilgisayarlar saymaya sıfırdan başlarlar
# print(ayIsimleri[0]) # Ocak
# print(ayIsimleri[4]) # Mayıs

kacinciAy = int(input("Hangi ay?\n"))

kacinciAy = kacinciAy % 12
print(ayIsimleri[kacinciAy - 1])
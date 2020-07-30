boy = int(input('Boyunuz?\n')) / 100
kilo = int(input('Kilonuz?\n'))

vki = round(kilo / (boy**2), 2)

if vki < 18:
    print('Aşırı zayıfsınız')
elif vki >= 18 and vki <= 25:
    print('Kilonuz ideal')
elif vki > 25:
    print('İdeal kilonuzun üzerindesiniz..')

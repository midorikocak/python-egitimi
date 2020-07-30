def vki(boy, kilo):
    boyBoluYuz = boy / 100
    vki = round(kilo / (boyBoluYuz**2), 2)

    if vki < 18:
        return -1
    elif vki >= 18 and vki <= 25:
        return 0
    elif vki > 25:
        return 1

print(vki(178, 79))
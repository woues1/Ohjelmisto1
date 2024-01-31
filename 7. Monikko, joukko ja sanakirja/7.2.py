
joukko = set()

while True:
    nimi = input('Nimi: ').lower()
    if nimi != '':
        if nimi not in joukko:
            print('Uusi nimi')
            joukko.add(nimi)
        else:
            print('Aiemmin syötetty nimi')
    else:
        break

for i in sorted(joukko):
    print(i)

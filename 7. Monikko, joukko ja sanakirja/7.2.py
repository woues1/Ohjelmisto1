
nimet = set()

while True:
    nimi = input('Nimi: ').lower()
    if nimi != '':
        if nimi not in nimet:
            print('Uusi nimi')
            nimet.add(nimi)
        else:
            print('Aiemmin syötetty nimi')
    else:
        break

for i in sorted(nimet):
    print(i)

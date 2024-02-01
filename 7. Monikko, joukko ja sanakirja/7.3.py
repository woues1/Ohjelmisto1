lentokentat = {'EFHK': 'helsinki-vantaa'}

while True:
    Valinta = input('Lisää / Etsi lentokenttää(L/E): ').upper()

    if Valinta == 'L':
        tunnus = input('ICAO tunnus: ').upper()
        nimi = input('Lentokentän nimi: ')
        lentokentat.update({tunnus: nimi})

    elif Valinta == 'E':
        tunnus = input('ICAO tunnus: ').upper()
        temp = dict((ICAO, nimi) for ICAO, nimi in lentokentat.items())
        print(temp[tunnus])

import numpy as np
import math
# 1

num = 0
while num < 1001:
    if num % 3 == 0:
        print(num)
    num += 1

# 2

while True:
    tuuma = float(input("Tuuma: "))
    if tuuma < 0:
        break
    else:
        print(tuuma*2.54)

# 3

numerot = []

while True:
    luku = input("Luku: ")
    if luku == '' and len(numerot) > 1:
        pienin = min(numerot)
        suurin = max(numerot)
        print(f"Pienin luku: {pienin} Suurin luku: {suurin}")
        break
    elif luku == '':
        print(f"Lukuja ei annettu tarpeeksi")
    elif luku.isnumeric():
        numerot.append(float(luku))
    else:
        print(f"Virheellinen syöte")

# 4

tietokoneen_luku = np.random.randint(1, 11)
arvaus = 0

while arvaus != tietokoneen_luku:
    arvaus = int(input("Anna luku"))
    if arvaus > tietokoneen_luku:
        print(f"Liian suuri arvaus")
    elif arvaus < tietokoneen_luku:
        print(f"Liian pieni arvaus")
    elif arvaus == tietokoneen_luku:
        print(f"Oikein")
    else:
        print(f"Virheellinen syöte")

# 5

yritys_kerta = 0

while True:
    salasana = input("Salasana: ")
    kayttajatunnus = input("käyttäjänimi")
    if yritys_kerta == 4:
        print("Pääsy evätty")
        break
    if salasana != 'rules' or kayttajatunnus != 'python':
        print("käyttäjätunnus tai salasana on väärin")
        yritys_kerta += 1
    elif salasana == 'rules' and kayttajatunnus == 'python':
        print(f"Tervetuloa")

# 6

pisteiden_maara = int(input(f"anna pisteiden luku määrä"))
i = 0
Pisteet_ympyran_sisalla = 0

while i < pisteiden_maara:
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    i += 1

    if math.pow(x,2)+math.pow(y,2) <= 1:
        Pisteet_ympyran_sisalla += 1

pii_likuarvo = 4 * (Pisteet_ympyran_sisalla / pisteiden_maara)

print(f"{pii_likuarvo:.5f}")



import numpy as np

# 1

syote = int(input(f"Anna heitettävien noppien määrä"))
arvotut_luvut = []
for i in range(syote+1):
    noppa = np.random.randint(1,6)
    arvotut_luvut.append(noppa)
print(f"{sum(arvotut_luvut)}")

arvotut_luvut = []

# 2

numerot = []

while True:
    luku = input("Anna luku")
    if luku != '' and luku.isnumeric():
        numerot.append(luku)
    else:
        break

numerot.sort(reverse=True)
for i in numerot: print(i, end=" ")

# 3

n = int(input("\nAnna luku"))

if n<2:
    print("luku ei ole alkuluku")
elif n == 2:
    print(f"luku on alkuluku")
else:
    for i in range(2,n):
        if (n % i) == 0:
            print(f"luku ei ole")
    print("luku on alkuluku")

# 4

kaupungit = []

for i in range(5):
    kaupunki = input("anna kaupungin nimi")
    kaupungit.append(kaupunki)
for i in kaupungit:
    print(i)

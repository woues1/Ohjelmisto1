
import numpy as np

# 0.1 

print("Hei, Toni Hirvikallio!")

# 1

k = input("Anna nimesi: ")
print("Terve, " + k)

# 2

sade = float(input("Anna ympyrän säde: "))
print(3.14 * (sade**2))

# 3

kanta = float(input("Anna suorakulmion kanta"))
korkeus = float(input("Anna suorakulmion korkeus"))
pinta_ala = kanta * korkeus
piiri = (kanta * 2) + (korkeus * 2)

print("Suorakulmion pinta-ala on:", pinta_ala, "ja piiri on:", piiri)

# 4

num1 = int(input("Anna luku"))
num2 = int(input("Anna luku"))
num3 = int(input("Anna luku"))

print("lukujen summa on:", num1+num2+num3, "keskiarvo on:", (num1+num2+num3)/3, "tulo on:", num1*num2*num3)

# 5

leviskat = float(input("Anna leiviskät."))
naulat = float(input("Anna naulat."))
luodit = float(input("Anna luodit."))

kg = ((luodit * 13.3)+(naulat*32*13.3)+(leviskat*20*32*13.3))/1000
g = (kg % 1)*1000

print("Massa nykymittojen mukaan:")
print(int(kg), "kilogrammaa ja", g, "grammaa.")

# 6

print("kuuden numeron koodi väliltä 0...9", np.random.randint(0, 10, 3))
print("neljän numeron koodi väliltä 0...6", np.random.randint(0, 7, 4))


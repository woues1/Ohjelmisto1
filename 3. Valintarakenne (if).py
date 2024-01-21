# 1

pituus = float(input("Anna kuhan pituus senttimetreinä."))

if pituus < 37:
    print(f"Päästä kuha takaisin järveen."
          f" Kuhan pituus on {37-pituus} cm liian lyhyt")
else:
    print("Kuha on tarpeeksi pitkä")

# 2

hyttiluokka = input("Anna hyttiluokkasi")

if hyttiluokka == 'LUX':
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == 'A':
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == 'B':
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == 'C':
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")

# 3

sukupuoli = input("Sukupuoli mies/nainen ")
hemoglobiiniarvo = float(input("Anna hemoglobiiniarvosi "))

if sukupuoli == 'mies':
    if 134 <= hemoglobiiniarvo <= 195:
        print(f"hemoglobiiniarvosi on normaali")
    elif hemoglobiiniarvo < 134:
        print(f"hemoglobiiniarvosi on alhainen")
    elif hemoglobiiniarvo > 195:
        print(f"hemoglobiiniarvosi on korkea")

if sukupuoli == 'nainen':
    if 117 <= hemoglobiiniarvo <= 175:
        print(f"hemoglobiiniarvosi on normaali")
    elif hemoglobiiniarvo < 117:
        print(f"hemoglobiiniarvosi on alhainen")
    elif hemoglobiiniarvo > 175:
        print(f"hemoglobiiniarvosi on korkea")

# 4

vuosiluku = int(input("Anna vuosiluku"))

if vuosiluku % 4 == 0:
    print("Vuosi on karkausvuosi")
elif vuosiluku % 100 == 0 and vuosiluku % 400 == 0:
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")

vuodenajat = ("kevät", "kesä", "syksy", "talvi")

kuukausi = int(input("Anna kuukausi numerona"))


if kuukausi <= 3:
    print(vuodenajat[0])
elif kuukausi > 3 and kuukausi <= 6:
    print(vuodenajat[1])
elif kuukausi > 6 and kuukausi <= 9:
    print(vuodenajat[2])
else:
    print(vuodenajat[3])
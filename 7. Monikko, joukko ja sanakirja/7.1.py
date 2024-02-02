
vuodenajat = ("kevät", "kesä", "syksy", "talvi")

kuukausi = int(input("Anna kuukausi numerona"))


if kuukausi > 11 or kuukausi <=2:
    print(vuodenajat[3])
elif kuukausi > 2 and kuukausi <= 5:
    print(vuodenajat[0])
elif kuukausi > 5 and kuukausi <= 9:
    print(vuodenajat[1])
else:
    print(vuodenajat[2])

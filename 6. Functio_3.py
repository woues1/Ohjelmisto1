def gallona_litra_muunnos(gallona) -> float:
    litra_muunnos = gallona*3.785
    return litra_muunnos
def main():

    while True:
        gallona_maara = float(input('Anna bensiinin gallonamäärä(negatiivinen luku lopettaa) '))
        if gallona_maara > 0:
            print(gallona_litra_muunnos(gallona_maara))
        else:
            break


if __name__ == '__main__':
    main()
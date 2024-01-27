import numpy as np

def heita_noppa(tahko) -> int:
    return np.random.randint(1, tahko+1)

def main():
    tahko = int(input("Anna nopan tahko"))
    while True:

        tulos = heita_noppa(tahko)
        if tulos != tahko:
            print(tulos)
        else:
            print(tulos)
            break


if __name__ == '__main__':
    main()

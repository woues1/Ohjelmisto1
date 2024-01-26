import numpy as np


def heita_noppa() -> int:
    return np.random.randint(1, 7)


def main():
    while True:
        tulos = heita_noppa()
        if tulos != 6:
            print(tulos)
        else:
            print(tulos)
            break


if __name__ == '__main__':
    main()

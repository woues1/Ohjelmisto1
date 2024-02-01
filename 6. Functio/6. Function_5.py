def parilliset_numerot(numerot):
    tulos = []
    for i in numerot:
        if i % 2 == 0:
            tulos.append(i)
    return tulos


def main():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list2 = [1, 2, 3, 4, 5, 6, 7]
    print(parilliset_numerot(list1), parilliset_numerot(list2))


if __name__ == '__main__':
    main()
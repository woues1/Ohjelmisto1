
def summa(lista):
    tulos = 0
    for i in lista:
        tulos += i
    return tulos

def main():
    list1 = [1,2,3,4,5,6,7,8]
    list2 = [1,2,3,4,5,6,7]
    print(summa(list1), summa(list2))
    
if __name__ == '__main__':
    main()
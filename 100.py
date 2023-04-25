from random import randint
from time import sleep

lista = []
soma = 0


def sort(a):
    a = []
    print('Sorteando 5 valores:', end='')
    for i in range(0, 5):
        a.append(randint(0, 100))
        sleep(0.25)
        print(a[i], end=' ')
    print()


def sompar(num):
    s = 0
    for valor in num:
        if valor % 2 == 0:
            s += valor
    print(s)


sort(lista)
sompar(lista)

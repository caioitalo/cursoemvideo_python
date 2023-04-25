from random import randint
from time import sleep

def maior(c ,b):
    for cont in range(0, c):

        print('Analisando os números passados...')
        cont = mai = 0
        for i in range(0, b):
            a = randint(0, 100)
            cont += 1
            if i == 0:
                mai = a
            elif a > mai:
                mai = a
            print(a, end=' ')
            sleep(0.5)

        print()
        print(f'Foram sorteados {cont} números')
        print(f'O maior número foi {mai}')
        print('=' * 30)
        sleep(1)


n1 = randint(1, 5)
n2 = randint(1, 10)
maior(n1, n2)

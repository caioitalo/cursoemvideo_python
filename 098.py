from time import sleep

def contador(ini, fim, passo):
    if passo != 0:
        for c in range(ini, fim+1, passo):
            print(c, end=' > ')
            sleep(0.25)
        print('FIM')
        print()
    elif ini > fim:
        for c in range(ini, fim-1, -1):
            print(c, end=' > ')
            sleep(0.25)
        print('FIM')
        print()
    elif ini < fim:
        for c in range(ini, fim+1, 1):
            print(c, end=' > ')
            sleep(0.25)
        print('FIM')
        print()


contador(1, 10, 1)
contador(10, 0, -2)
print('=' * 30)
i = int(input('Digite o valor inicial da contagem:'))
f = int(input('Digite o valor final da contagem:'))
p = int(input('Digite o passo da contagem:'))

contador(i, f, p)

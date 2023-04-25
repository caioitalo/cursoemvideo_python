print(f'{"=-"*20}\nContador de pares \n{"=-"*20}')

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

print(f'Os números pares entre {n1} e {n2} são:')
for i in range(n1, n2+1):
    if (i % 2) == 0:
        print(f'{i}', end=' ')

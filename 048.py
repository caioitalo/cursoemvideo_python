print(f'{"-=" * 20}\nSomador de ímpares múltiplos de 3\n{"-=" * 20}\n')

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n = 0

for i in range(n1, n2+1):
    if i % 2 == 1 and i % 3 == 0:
        n += i

print(f'A soma entre {n1} e {n2} dos múltiplos impares de 3 é de {n}')

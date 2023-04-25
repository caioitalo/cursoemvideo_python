print(f'{"-=" * 20}\nSomador de n termos de uma P.A\n{"-=" * 20}')

a1 = int(input('Digite o 1º termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
n = int(input('Quantos termos você deseja somar? '))
cont = 1
op = n

while op != 0:
    while cont < (n+1):
        termo = a1 + (cont - 1) * r
        print(f'{termo}', end=' - ')
        cont += 1
    op = int(input('\nVocê deseja contar quantos termos mais?'))
    n += op

an = a1 + (n - 1) * r
soma = float((a1 + an) * n / 2)

print(f'\nA soma dos {n} primeiros termos da P.A é {soma:.1f}')

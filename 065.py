n = 0
soma = 0
cont = 0
op = 'S'
num = []

while op == 'S':
    n = int(input('Digite um número: '))
    soma += n
    num.append(n)
    cont += 1

    op = str(input('Você deseja continuar (S/N)? ')).strip().upper()
    while op != 'S' and op != 'N':
        op = str(input('Por favor, digite S/N: ')).strip().upper()

med = soma / cont
print(f'O maior número é {max(num)} e o menor é {min(num)}')
print(f'A média foi de {med:.2f}')

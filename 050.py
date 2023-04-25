soma = 0

for i in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma = soma + n

print(f'A soma dos números pares é igual a: {soma}')

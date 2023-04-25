cont = 0
n = soma = 0

while True:  # chamado de loop infinito
    n = int(input('Digite um número a ser somado: '))  # fazendo isso, não precisa de gambiarra na soma.
    if n == 999:
        break
    cont += 1
    soma += n

print(f'\nForam digitados {cont} números')
print(f'E a soma deles foi igual a {soma}')

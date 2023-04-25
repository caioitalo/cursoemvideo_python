cont = -1
n = soma = 0

n = int(input('Digite um número a ser somado: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número a ser somado: '))  # fazendo isso, não precisa de gambiarra na soma.

print(f'Foram digitados {cont} números')
print(f'E a soma deles foi igual a {soma}')

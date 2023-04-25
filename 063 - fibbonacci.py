n = int(input('Digite um número de termos da sequência de fibonacci: '))
cont = 3  # foi um erro que percebi. como o n começa com 3. eu preciso ajustar o cont.
a = 0
b = 1

if n == 1:
    print('0')

elif n == 2:
    print('0 1')

else:
    print('0 1', end=' ')
    while cont <= n:
        soma = a + b
        print(f'{soma}', end=' ')
        a = b
        b = soma
        cont += 1

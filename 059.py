print('===== MINICALCULADORA =====')
op = 0

a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))

while op != 5:
    print('''\n   = OPERAÇÕES =
    [1] - SOMA
    [2] - MULTIPLICAÇÃO
    [3] - MAIOR
    [4] - NOVOS NÚMEROS
    [5] - SAIR DO PROGRAMA''')
    op = int(input('OPERAÇÃO: '))
    if op == 1:
        print(f'A soma é igual a {a + b}')
    elif op == 2:
        print(f'A multiplicação é igual a {a * b}')
    elif op == 3:
        print(f'O maior valor é {max(a, b)}')
    elif op == 4:
        a = float(input('Digite um valor: '))
        b = float(input('Digite outro valor: '))
    else:
        print('Por favor, digite um valor válido de operação.')


print('Muito obrigado por utilizar o programa!')

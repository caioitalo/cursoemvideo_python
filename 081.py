lista = []

while True:
    op = ''
    lista.append(int(input('Digite um número: ')))
    while op != 'S' and op != 'N':
        op = str(input('Você deseja continuar [S/N]? ')).strip().upper()
    if op == 'N':
        break

print(sorted(lista, reverse=True))

if 5 in lista:
    print('O número 5 foi digitado')
else:
    print('O número 5 não foi digitado')

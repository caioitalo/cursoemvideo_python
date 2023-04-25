lista = []
par = []
imp = []

while True:
    op = ''
    lista.append(int(input('Digite um número: ')))

    while op != 'S' and op != 'N':
        op = str(input('Você deseja continuar [S/N]? ')).strip().upper()
    if op == 'N':
        break

for c in lista:
    if c % 2 == 0:
        par.append(c)
    elif c % 2 == 1:
        imp.append(c)

print(lista)
print(par)
print(imp)
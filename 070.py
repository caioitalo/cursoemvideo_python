prod = []
prod_preco = []
ind_menor = []
op = ''
n = maiorqmil = total_compra = menor = 0


print(f'{"=" * 20}\nLEITOR DE COMPRAS\n{"=" * 20}')
while True:
    prod.append(str(input(f'Digite o nome do produto: ')).strip().upper())
    prod_preco.append(float(input('Digite o preço do produto (em R$): ')))
    while prod_preco[n] < 0:
        prod_preco[n] = (float(input('Por favor, digite um valor válido (em R$): ')))

    total_compra += prod_preco[n]
    if prod_preco[n] > 1000:
        maiorqmil += 1

    if n == 0:
        menor = prod_preco[0]
    elif prod_preco[n] <= menor:
        ind_menor.append(n)  # aqui há um problema, se a pessoa digitar o menor preço no local [0], não vai mostrar.
    n += 1

    print(f'{"-" * 30}\nSUBTOTAL: R${total_compra:.2f}')
    op = str(input('Encerra essa compra[S/N]? ')).strip().upper()
    while not op in 'SN':
        op = str(input('Comando inválido! Encerrar essa compra [S/N]? ')).strip()[0].upper()
    if op == 'S':
        break

print('-' * 25)
print(f'{"=" * 30}\nCOMPRA ENCERRADA\n{"-" * 30}')
print(f'''TOTAL DA COMPRA: R$ {total_compra:.2f}
{maiorqmil} produto(s) tinha(m) um preço acima de R$1.000,00
Os produtos com menores preços foram:''')
for c in range(0, len(ind_menor)):
    print(f'{prod[ind_menor[c]]}')

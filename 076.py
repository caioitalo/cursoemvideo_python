lista = ('Lápis', 1.75, 'Caneta', 2.50, 'Borracha', 0.50, 'Abacaxi', 7.80, 'Bola', 145.00)

print(f'{"-" * 40}')
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print(f'{"-" * 40}')

for c in range(0, len(lista), 2):
    print(f'{lista[c]:.<30} R$ {lista[c+1]:>6.2f}')  # olha essa bizarrice. aprendi na cagada como tabula os elementos.

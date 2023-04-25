print('===== EXERCÍCIO 11 =====')

h = float(input('Digite a altura da parede (em m): '))
l = float(input('Digite a largura da parede (em m): '))

tinta = (h * l)/2           # area/2, pois no exercício cada L de tinta pinta 2m²

print(f'A quantidade de tinta necessária para pintar é de {tinta:.3f} L.')

print('=' *12)  # interessante a mistura entre string e operador aritmetico

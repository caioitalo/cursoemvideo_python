lista = []

for c in range(0, 5):
    lista.append(int(input('Digite um número: ')))
print(f'O maior número é {max(lista)} e o menor é {min(lista)}.')
print(f'O maior número ocupa as posições: ', end='')
for c in range(0, len(lista)):
    if lista[c] == max(lista):
        print(c, end=' ')

print(f'\nO menor número ocupa as posições: ', end='')
for c in range(0, len(lista)):
    if lista[c] == min(lista):
        print(c, end=' ')


m33 = [[], [], []]
sum_par = sum_col3 = 0

for l in range(0,3):
    for c in range (0, 3):
        m33[c][l] = int(input(f'Digite o elemento {c}x{l}:'))  # como é uma lista, pode usar assim ou append.

print('A matriz formada é:')
for l in range(0,3):
    for c in range (0, 3):
        print(f'[{m33[l][c]:^4}]', end='')
        if m33[l][c] % 2 == 0:
            sum_par += m33[l][c]
        if c == 2:
            sum_col3 += m33[l][c]
    print()

print(f'A soma dos elementos pares da matriz é igual a {sum_par}')
print(f'A soma dos elementos da coluna 3 é igual a {sum_col3}')
print(f'O maior valor da 2a linha é igual a {max(m33[:][1])}')
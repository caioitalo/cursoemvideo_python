num = [[], []]

for c in range(0, 7):
    a = int(input(f'Digite o {c+1}º número: '))
    if a % 2 == 0:
        num[0].append(a)
    else:
        num[1].append(a)

print('-' * 30)
if len(num[0]) == 0:
    print('Não foram digitados números pares')
else:
    print(f'Os números pares digitados pares foram: {sorted(num[0])}')

if len(num[1]) == 0:
    print('Não foram digitados números ímpares')
else:
    print(f'Os números pares digitados ímpares foram: {sorted(num[1])}')

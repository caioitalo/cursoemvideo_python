num = (int(input('Digite um número: ')), int(input('Digite outro número: ')),  # não sabia que dava pra fazer isso em tupla
       int(input('Digite mais um número: ')), int(input('Digite um último número: ')))

par = cont3 = 0
for cont in num:
     if cont % 2 == 0:
          par += 1

print(f'''Você digitou {num}
O número 9 apareceu {num.count(9)} vezes
Foram digitados {par} números pares''')

if 3 in num:
     print(f'O número 3 aparece primeiro na posição {num.index(3)+1}')
else:
     print('O número 3 não foi digitado')

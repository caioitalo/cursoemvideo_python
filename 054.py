from datetime import date
anoatual = date.today().year
menor = 0
maior = 0
for i in range(0, 6):
    x = int(input('Digite o ano de nascimento: '))
    if (x - anoatual) < 18 and 1900 < x <= anoatual:
        menor += 1
    elif (x - anoatual) >= 18 and 1900 < x <= anoatual:
        maior += 1
    else:
        print('Você digitou um ano inválido!')
        exit()  # encerra o programa caso você digite algo errado

print(f'{maior} são maiores e {menor} são menores.')
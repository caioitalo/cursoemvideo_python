from datetime import date


nasc = int(input('Digite o ano de nascimento do atleta: '))
anoatual = date.today().year
idade = anoatual - nasc

if idade <= 9:
    print('O atleta está na categoria MIRIM.')
elif idade <= 14:
    print('O atleta está na categoria INFANTIL.')
elif idade <= 19:
    print('O atleta está na categoria JUNIOR.')
elif idade <= 20:
    print('O atleta está na categoria SÊNIOR.')
else:
    print('O atleta está na categoria MASTER.')

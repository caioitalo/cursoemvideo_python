from random import choice

print('-=' * 21)
print('JO-KEN-PÔ')
print('-=' * 21)

print('Vamos jogar? Eu escolho um e você outro!')
user = str(input('Escolha o seu movimento: ')).strip().title()

lista = ('Pedra', 'Papel', 'Tesoura')

if user == lista[0] or user == lista[1] or user == lista[2]:
    pc = choice(lista)
    if user == 'Pedra' and pc == 'Tesoura' or user == 'Papel' and pc == 'Pedra' or user == 'Tesoura' and pc == 'Papel':
        print(f'Escolho {pc}!!\nParabéns, você me derrotou!')

    elif user == pc:
        print(f'Escolho {user}!!\nIh! Empatamos!')

    elif user != pc:
        print(f'Escolho {pc}!!\nHAHAHA! Perdeu, seu otário!')

else:
    print('Você digitou uma opção inválida!!')

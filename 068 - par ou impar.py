from random import randint
pc = randint(0, 11)
log = parouimp = ''
cont = 0

print('--- JOGO DO PAR OU ÍMPAR ---')
while True:
    user = int(input('Escolha um inteiro de 0 a 10: '))
    parouimp = str(input('Você deseja Par ou Ímpar[P/I]? ')).strip().upper()
    while parouimp not in 'PI':
        parouimp = str(input('Opção inválida. Deseja Par ou Ímpar[P/I]? ')).strip().upper()

    soma = pc + user

    if soma % 2 == 0:
        log = 'P'
        res = 'Par'
    else:
        log = 'I'
        res = 'Ímpar'

    if log != parouimp:
        break

    print(f'''{'-' * 30}\nParabéns, me venceu. Escolhi {pc} e você {user} resultando em {res}
{'=' * 30}
Vamos jogar novamente!''')
    cont += 1

print(f'\nGAME OVER! Escolhi {pc} e você escolheu {user}, resultando em {res}'
      f'\nVocê conseguiu me vencer {cont} vezes')

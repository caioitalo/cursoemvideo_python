from random import randint

n = int(input('Digite o número de jogos que quer gerar: '))
for n in range(0, n):
    jogo = []
    for c in range(0, 6):
        jogo.append(randint(1, 60))

        while jogo.count(jogo[c]) > 1:
            jogo.pop()
            jogo.append(randint(1, 60))
    print(f'Jogo número {n+1}: {jogo.sort()}')

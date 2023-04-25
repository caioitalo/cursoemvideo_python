from random import randint
from operator import itemgetter

ranking = []
dicio = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}

print('=' * 30)
print('-- Ranking dos ganhadores --')
ranking = sorted(dicio.items(), key=itemgetter(1), reverse=True)  # essa parada aqui que eu não sabia

for i, c in enumerate(ranking):
    print(f'O jogador{i+1} tirou {c[0]} com {c[1]}')

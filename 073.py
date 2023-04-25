BR = ('Pal', 'Int', 'Flu', 'Fla', 'Cor', 'Cap', 'Cam', 'Amg', 'Goi', 'Bot', 'San', 'Bra', 'Spo', 'For', 'Cea',
      'Ctb', 'Ava', 'Ago', 'Juv')
print(f'Os primeiros 5 colocados do BR22 atualmente são {BR[0:6]}')
print(f'Os últimos 4 colocados do BR22 atualmente são {BR[-4:]}')  # modo de mostrar os últimos elementos de uma tupla
print(sorted(BR))
print(f'O Fortaleza está na {BR.index("For")+1}ª posição')
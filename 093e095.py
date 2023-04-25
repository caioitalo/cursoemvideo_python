jog = {}
gols = []
cad_jog = []
while True:
    jog.clear()
    op = ''
    jog['Nome'] = str(input('NOME DO JOGADOR: '))
    part = int(input('No DE PARTIDAS JOGADAS: '))

    for c in range(1, part+1):
        gols.append(int(input(f'GOLS DA PARTIDA {c}: ')))

    jog['Gols'] = gols[:]
    gols.clear()
    jog['Total'] = sum(jog['Gols'])
    cad_jog.append(jog.copy())

    while op != 'N' and op != 'S':
        op = str(input('Deseja adicionar outra pessoa[S/N]? ').strip().upper())
    if op == 'N':
        break

    print('-' * 30)

print('=' * 30)
print('cod ', end='')
for i in jog.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 30)
for k, v in enumerate(cad_jog):  # olha só isso aqui, forma de formatar um dicionário
    print(f'{k:>4}',end='')
    for c in v.values():
        print(f'{str(c):<15}', end='')  #pra funcionar a formataçao necessita transformar aqui em string
    print()
print()
while True:
    dados = int(input('Mostrar dados de qual jogador(999 para parar)    ?'))
    while dados > (len(cad_jog)-1):
        dados = int(input('ERRO, digite um valor válidos para dados de jogador(999 para parar)'))
    if dados == 999:
        break
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {cad_jog[dados]["Nome"].upper()} --')
        for c in range(0, len(cad_jog[dados]['Gols'])):
            print(f"Na partida {c + 1}, fez {cad_jog[dados]['Gols'][c]}")

from datetime import date

print('Analisador de alistamento militar')
print('-=' * 21)

anoatual = date.today().year  # ficar atento à biblioteca de tempo (time) e datetime
nasc = int(input('Digite o ano de nascimento da pessoa: '))

if (anoatual - nasc) < 18:
    print('O jovem ainda não tem idade para alistamento.\n'
          f'Ainda falta(m) {18 - (anoatual - nasc)} ano(s) para se alistar.')

elif (anoatual - nasc) == 18:
    print('Chegou a hora! O jovem está na idade militar!')

else:
    print('O jovem demorou. Passou a idade militar, pague a multa!\n'
          f'Já há {(anoatual - nasc) - 18} ano(s) de atraso.')
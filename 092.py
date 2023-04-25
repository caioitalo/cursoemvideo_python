from datetime import datetime
pessoa = []
cad = {}

cad['Nome'] = str(input('NOME: ')).strip()
anonasc = int(input('ANO DE NASCIMENTO: '))
cad['Idade'] = datetime.today().year - anonasc
cad['CTPS'] = int(input('No da CTPS(digite 0 se não possuir): '))
if cad['CTPS'] != 0:
    cad['Ano de Contratação'] = int(input('ANO DE CONTRATAÇÃO: '))
    cad['Salário'] = float(input('SALÁRIO: '))
    cad['Aposentadoria'] = cad['Idade'] + (35 - (datetime.today().year - cad['Ano de Contratação']))


for i, c in cad.items():
    print(f'{i} tem o valor de {c}')

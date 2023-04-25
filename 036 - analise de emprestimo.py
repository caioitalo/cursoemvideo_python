print('=-'*25)
print('Analisador de empréstimo')
print('=-'*25)

casa = float(input('Digite o valor da casa em reais: '))
sal = float(input('Digite o salário do interessado: '))
tempo = int(input('Insira o tempo em que será pago (em anos):'))

prest = casa/(tempo * 12)

if prest > (0.3 * sal):
    print('Sentimos muito! O empréstimo não pode ser aprovado.')

else:
    print('Parabéns! O seu empréstimo foi aprovado!')
x1 = float(input('Digite a primeira nota: '))
x2 = float(input('Digite a segunda nota: '))

med = (x1 + x2)/2

print(f'A média é: {med:.2f}')

# a partir daqui foi a adição do exercício 40

if med <= 5.00:
    print('O Aluno está REPROVADO!')

elif med > 5.00 and med < 7.00:
    print('O aluno está de RECUPERAÇÃO!')

elif med >= 7.00 and med <= 10.00:
    print('Parabéns! O aluno está APROVADO!')

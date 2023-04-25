num = []

while True:
    op = ''
    num.append(int(input('Digite um número: ')))
    while num.count(num[len(num)-1]) > 1:  # aqui daria pra ter colocado o not in num. ficaria muito mais simples
        num.pop()
        num.append(int(input('Valor já adicionado. Digite um número diferente: ')))

    while op != 'S' and op != 'N':
        op = str(input("Você deseja continuar [S/N]?")).upper().strip()
    if op == 'N':
        break
print(sorted(num))
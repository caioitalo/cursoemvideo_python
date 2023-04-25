palavras = ('CAIO', 'NAARA', 'ABACATE', 'DEUS', 'BANANA', 'PROGRAME', 'NIMO', 'BUCAL')

for c in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[c]} temos as vogais: ', end='')
    print(palavras[c].count('A') * 'a' if 'A' in palavras[c] else '', end='')
    print(palavras[c].count('E') * 'e' if 'E' in palavras[c] else '', end='')
    print(palavras[c].count('I') * 'i' if 'I' in palavras[c] else '', end='')
    print(palavras[c].count('O') * 'o' if 'O' in palavras[c] else '', end='')
    print(palavras[c].count('U') * 'u' if 'U' in palavras[c] else '', end='')

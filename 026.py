frase = str(input('Digite uma frase qualquer: ')).strip()

frase = frase.lower()  # necessário para contar eventuais letras maiúsculas
frase = frase.replace("á", "a")  # só um exemplo de retirar caracteres especiais, daria pra por outros

print(f'A letra "a" aparece {frase.count("a")} vezes')
print(f'A primeira vez em que ela aparece é na posição {frase.index("a")+1}')
print(f'A última vez em que ela aparece é na posição {frase.rindex("a")+1}')

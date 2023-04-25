import random

print('=== JOGO DA ADIVINHAÇÃO ===')
user = int(input("Digite um inteiro entre 0 e 10: "))
pc = random.randint(0, 10)
cont = 0

while user != pc:  # while not user == pc:
    print(f'Seu miserável, errou uma merda dessa, eu pensei em {pc}. huauahuaha')
    user = int(input("Tente novamente digitando outro valor entre 0 e 10: "))

    cont += 1

print('Parabéns! Você adivinhou o número que pensei!'
      f'\nForam necessários {cont} palpites para me vencer!')

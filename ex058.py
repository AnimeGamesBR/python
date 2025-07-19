from random import randint
n = randint(0, 10)
print('O computador pensou em um número de 0 a 10. ', end='')
r = -1
c = 1

while r != n:
    r = int(input('Tente adivinhar: '))
    if r != n:
        c += 1
        if r > n:
            print('Você errou. É menos que isso...')
        else:
            print('Você errou. É mais que isso...')

if c == 1:
    print(f'Você precisou de apenas {c} palpite para acertar. Parabéns, você foi muito bem.')
elif c <= 3:
    print(f'Você precisou de apenas {c} palpites para acertar. Parabéns, você foi muito bem.')
elif c >= 4:
    print(f'Você precisou de {c} palpites para acertar. Que pena, mais sorte da próxima vez.')

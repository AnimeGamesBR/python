from random import randint
n = randint(0, 5)
r = int(input('Adivinhe o número de 0 a 5: '))

print(f'Parabéns! Você acertou! O número correto era {n}.' if r == n else f'Puts! Não foi dessa vez, tente novamente! O número correto era {n}.')

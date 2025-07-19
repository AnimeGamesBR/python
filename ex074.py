from random import randint
maior = menor = 0
lista = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), )
print('Os valores sorteados foram: ', end='')
for n in lista:
    print(f'{n} ', end='')

print(f'\nO maior número é {max(lista)}')
print(f'O menor número é {min(lista)}')

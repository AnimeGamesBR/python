'''from random import randint

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
escolhido = randint(1,4)

if escolhido == 1:
    print(f'O escolhido foi {a1}.')
elif escolhido == 2:
    print(f'O escolhido foi {a2}.')
elif escolhido == 3:
    print(f'O escolhido foi {a3}.')
else:
    print(f'O escolhido foi {a4}')'''

from random import choice

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = [a1, a2, a3, a4]
escolhido = choice(lista)

print(f'O aluno escolhido foi {escolhido}.')

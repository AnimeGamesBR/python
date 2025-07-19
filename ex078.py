lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))

print(f'Você digitou os valors: {lista}')
print(f'O maior valor digitado foi {max(lista)} e ele está na posição ', end='')
for c, v in enumerate(lista):
    if v == max(lista):
        print(c, end='... ')

print(f'\nO menor valor digitado foi {min(lista)} e ele está na posição ', end='')
for c, v in enumerate(lista):
    if v == min(lista):
        print(c, end='... ')

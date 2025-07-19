'''e = str(input('Digite uma expressão qualquer: '))
c1 = e.count('(')
c2 = e.count(')')

if c1 != c2:
    print('Sua expressão é inválida!')
else:
    print('Sua expressão é válida!')'''

e = str(input('Digite uma expressão qualquer: '))
pilha = []
for s in e:
    if s == '(':
        pilha.append('(')
    elif s == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')

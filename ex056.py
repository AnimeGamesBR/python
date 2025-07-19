velho = 0
media = 0
mulher = 0
pessoas = 0

for c in range(1, 5):
    print(f'----- {c}° PESSOA -----')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M / F]: ')).upper().strip()
    media += idade
    if sexo == 'F' and idade < 20:
        mulher += 1
    if velho < idade and sexo == 'M':
        velho = idade
        nomeH = nome
    elif velho > idade and sexo == 'M':
        velho = velho

print(f'A média de idade do grupo digitado é {media / c:.0f} anos.')
print('Não existe homem no grupo digitado.' if velho == 0 else f'O homem mais velho tem {velho} anos e seu nome é {nomeH}.')
print(f'O grupo tem {mulher} mulheres com menos de 20 anos.' if mulher > 1 else f'O grupo tem {mulher} mulher com menos de 20 anos.')

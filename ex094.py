dados = {}
pessoas = []
mulheres = []
count = 1
soma = 0

while True:
    dados['nome'] = str(input(f'Digite o nome da {count}° pessoa: ')).strip()

    dados['sexo'] = str(input(f'Digite o sexo da {count}° pessoa [M/F]: ')).strip().upper()
    if dados['sexo'] in 'Ff':
        mulheres.append(dados['nome'])

    dados['idade'] = int(input(f'Digite a idade da {count}° pessoa: '))
    soma += dados['idade']

    pessoas.append(dados.copy())
    count += 1

    continuar = str(input('Deseja continuar [S/N]? ')).strip()
    if continuar in 'Nn':
        break

print(f'- O grupo tem {count - 1} pessoas.')
print(f'- A média de idade é de {soma / (count - 1)}')
print('- Não houve cadastro de nenhuma mulher.\n' if len(mulheres) == 0 else f'- As mulheres cadastradas foram: ', end='')
if len(mulheres) != 0:
    for m in mulheres:
        if len(mulheres) != 1:
            print(f'{m}', end=' ')
        else:
            print(f'{m}')

print('\n- Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] > soma / (count - 1):
        print(f'    nome = {p['nome']}; sexo = {p['sexo']}; idade = {p['idade']};')

print('')
print('<< ENCERRADO >>')

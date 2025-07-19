c18 = ch = m20 = 0

print('[ CADASTRE PESSOAS ]')
while True:
    sexo = str(input('Digite o sexo [M/F]: '))
    while sexo not in 'MmFf':
        print('Seleção inválida. Por favor digite o sexo conforme as opções indicadas.')
        print('=-' * 20)
        sexo = str(input('Digite o sexo [M/F]: '))
    if sexo in 'Mm':
        ch += 1

    idade = int(input('Digite a idade: '))
    while idade < 0:
        print('Idade inválida. Por favor digite uma idade com valores positivos.')
        print('=-' * 20)
        idade = int(input('Digite a idade: '))
    if idade >= 18:
        c18 += 1
    if sexo in 'Ff' and idade < 20:
        m20 += 1

    continuar = str(input('Deseja continuar [S/N]? '))
    if continuar in 'Nn':
        break

print('=-' * 20)
print(f'{c18} pessoas tem mais de 18 anos.' if c18 != 1 else f'{c18} pessoa tem mais de 18 anos.')
print(f'{ch} homens foram cadastrados.' if ch != 1 else f'{ch} homem foi cadastrado.')
print(f'{m20} mulheres com menos de 20 anos foram cadastradas.' if m20 != 1 else f'{m20} mulher com menos de 20 anos foi cadastrada.')

dados = {}
nome = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
ctps = int(input('Carteira de trabalho: '))
idade = 2025 - ano
if ctps != 0:
    contrato = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$ '))
    ads = 2025 - contrato
    if ads <= 35:
        aposentadoria = idade + 35 - ads

dados['nome'] = nome
dados['idade'] = idade
dados['ctps'] = ctps
if ctps != 0:
    dados['contrato'] = contrato
    dados['salário'] = salario
    dados['aposentadoria'] = aposentadoria

for d in dados.items():
    print(f'{d[0]} tem o valor de {d[1]}')

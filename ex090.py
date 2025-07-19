boletim = {}
boletim['nome'] = str(input('Nome do aluno: '))
boletim['média'] = float(input('Média do aluno: '))
if boletim['média'] < 7:
    boletim['situação'] = 'reprovado!'
else:
    boletim['situação'] = 'aprovado!'
print(f'O aluno {boletim["nome"]} tem uma média de {boletim["média"]}! Então ele está {boletim["situação"]}')

boletim = []
lista = []
cont = q = 0
while True:
    lista.append(str(input('Digite o nome do aluno: ')))
    for c in range(0, 2):
        cont += 1
        lista.append(float(input(f'Digite a {cont}° nota de {lista[0]}: ')))
    boletim.append(lista[:])
    lista.clear()
    cont = 0
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print('-=' * 40)
for aluno in boletim:
    q += 1
    print(f'{q}° ALUNO')
    print(f'Nome: {aluno[0]}')
    print(f'Notas: {aluno[1]}, {aluno[2]}')
    print('-=' * 40)

alunos = int(input('Quer ver a média de qual aluno? (999 interrompe): '))
while alunos != 999:
    soma = boletim[alunos - 1][1] + boletim[alunos - 1][2]
    print(f'{boletim[alunos - 1][0]} tem uma média de {soma/2:.1f}!')
    print('-=' * 40)
    alunos = int(input('Quer ver a média de qual aluno? (999 interrompe): '))

tabela = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Bragantino', 'Ceará SC', 'Bahia', 'Fluminense', 'Corinthians', 'Atlético-MG', 'Botafogo', 'São Paulo', 'Mirassol', 'Vasco da Gama', 'Fortaleza', 'Internacional', 'EC Vitória', 'Grêmio', 'Juventude', 'Santos', 'Sport Recife')

print(f'Os 5 primeiros colocados são {tabela[0:5]}')
print(f'Os 4 últimos são {tabela[-4:]}')
print(f'Lista com os times em ordem alfabética:')
print(sorted(tabela))
print(f'O time Internacional está em {tabela.index('Internacional') + 1}° lugar!')

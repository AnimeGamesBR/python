from random import choice
palavras = [
    'carta', 'livro', 'banco', 'pente', 'cinto', 'limpo', 'muito', 'bravo', 'feliz', 'doido',
    'vazio', 'lento', 'curva', 'noite', 'nuvem', 'verde', 'lugar', 'roupa', 'passe', 'dente',
    'ponto', 'vento', 'claro', 'fosso', 'tenso', 'leite', 'cinco', 'lindo', 'cobre', 'porta',
    'morro', 'risco', 'justo', 'troco', 'linha', 'peixe', 'gente', 'letra', 'gosto', 'fruta',
    'baixo', 'manga', 'limao', 'seiva', 'carro', 'bolsa', 'velha', 'livre', 'pouco', 'reino',
    'pedra', 'barco', 'festa', 'haste', 'norte', 'sulco', 'grama', 'canto', 'cansa', 'farol',
    'vapor', 'nobre', 'chuva', 'casal', 'sinal', 'vinho', 'corpo', 'brisa', 'folha', 'troca',
    'lucro', 'digno', 'pardo', 'plano', 'sonho', 'faixa', 'algum', 'sorte', 'piano', 'audio',
    'ficar', 'morto', 'parar', 'meter', 'rasga', 'andar', 'botar', 'tirar', 'campo', 'acaso',
    'limar', 'rolar', 'saber', 'criar', 'achar', 'dizer', 'ouvir', 'calmo', 'cheio', 'chefe',
    'cesta', 'cobra', 'cerca', 'danca', 'dedos', 'deixa', 'drama', 'motor', 'etapa', 'feira',
    'fenda', 'ferro', 'ficou', 'firma', 'firme', 'forno', 'fosco', 'gaita', 'ganho', 'garra',
    'golpe', 'graca', 'grato', 'grosso', 'idade', 'inato', 'icone', 'jogar', 'junta', 'justa',
    'lapis', 'larga', 'larva', 'linda', 'livra', 'lombo', 'lousa', 'luxo', 'macio', 'massa',
    'meigo', 'meios', 'milha', 'misto', 'molho', 'monte', 'mover', 'mudar', 'muros', 'movel',
    'navio', 'nervo', 'nicho', 'nivel', 'nossa', 'ocio', 'odiar', 'olhos', 'opaco', 'ossos',
    'outra', 'padre', 'palco', 'papel', 'parei', 'parou', 'parte', 'pedal', 'perda', 'perto',
    'pesar', 'pesca', 'pique', 'pisar', 'pista', 'poder', 'pobre', 'poema', 'poeta', 'ponta',
    'preto', 'primo', 'prato', 'queda', 'perca', 'lasca', 'radar', 'rasgo', 'regra', 'salto',
    'sabor', 'santa', 'santo', 'saque', 'saldo', 'senda', 'senso', 'serra', 'servo',
    'setor', 'sigla', 'sinto', 'sobra', 'socio', 'sobre', 'solto', 'sonar', 'surto', 'talha',
    'tarde', 'tenha', 'termo', 'terno', 'texto', 'tinha', 'tirou', 'tomar', 'torna', 'tosco',
    'traje', 'treta', 'trono', 'truco', 'turma', 'turvo', 'unido', 'urina', 'usina', 'valer',
    'valia', 'valsa', 'veloz', 'venda', 'verbo', 'verao', 'miojo', 'versa', 'verso', 'vetor',
    'vezes', 'visto', 'vista', 'viuva', 'viver', 'vocal', 'volta', 'votar', 'zelar', 'zebra',
    'atomo', 'ambar', 'amago', 'angulo', 'epico', 'epoca', 'exito', 'idolo', 'impar', 'indio',
    'opera', 'orfao', 'ovalo', 'umido', 'utero', 'natal', 'repor', 'rival', 'trava', 'aureo',
    'mural', 'vinil', 'pleno', 'pinho', 'puxar', 'refem', 'retas', 'rolou', 'salas', 'sujar'
]

letrasCorretas = []
letrasIncertas = []
palavraCorreta = choice(palavras)
tentativas = 7

#print(palavraCorreta)
print('{:=^100}'.format('\033[36m [ TERMO ] \033[m'))
print(f'Você tem {tentativas} tentativas para descobrir qual a palavra correta. Jogue com cautela e boa sorte!')
palavra = str(input('Digite uma palavra com 5 letras: ')).lower()



while palavra != palavraCorreta:
    while len(palavra) != 5:
        print('Você não digitou uma palavra com 5 letras. Por favor, tente novamente.')
        palavra = str(input('Digite uma palavra com 5 letras: ')).lower()
    print('Você digitou a palavra errada.')
    tentativas -= 1
    if tentativas <= 0:
        break
    print(f'Te restam {tentativas} tentativas!')

    for pos, l in enumerate(palavra):
        if l != palavraCorreta[pos]:
            letrasCorretas.append('_')
        if l == palavraCorreta[pos]:
            letrasCorretas.append(l)
        if l in palavraCorreta and l != palavraCorreta[pos]:
            letrasIncertas.append(l)
    print(f'As letras que você acertou foram \033[32m{letrasCorretas}\033[m!')
    print(f'As letras \033[33m{letrasIncertas}\033[m estão na palavra, porém não nessa posição.')
    letrasCorretas.clear()
    letrasIncertas.clear()

    print('-=' * 40)
    palavra = str(input('Digite outra palavra: ')).lower()
else:
    print('Você digitou a palavra correta. Parabens!!!')

if tentativas <= 0:
    print(f'Você acabou perdendo todas as suas chances. Que pena. Mais sorte da próxima vez!')
print(f'A palavra correta era {palavraCorreta}!')

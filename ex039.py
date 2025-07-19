'''from datetime import date
an = int(input('Digite seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - an

if idade < 18 and 18 - idade == 1:
    print(f'Falta {18 - idade} ano para você se alistar.')
    print(f'Seu alistamento será em {anoAtual + 1}.')
elif idade < 18 and 18 - idade > 1:
    print(f'Faltam {18 - idade} anos para você se alistar.')
    print(f'Seu alistamento será em {anoAtual + (idade - 18)}.')
elif idade > 18 and idade - 18 == 1:
    print(f'Passou {idade - 18} ano do seu prazo de alistamento.')
    print(f'Seu alistamento foi em {anoAtual - 1}.')
elif idade > 18 and idade - 18 > 1:
    print(f'Passou {idade - 18} anos do seu prazo de alistamento.')
    print(f'Seu alistamento foi em {anoAtual - (idade - 18)}.')
else:
    print('Já é hora de você se alistar.')'''

from datetime import date
genero = str(input('Qual seu genêro? ')).strip().upper()

if genero == 'HOMEM':
    an = int(input('Qual seu ano de nascimento? '))
    anoAtual = date.today().year
    idade = anoAtual - an
    if idade < 18 and 18 - idade == 1:
        print(f'Falta {18 - idade} ano para você se alistar. \nSeu alistamento será em {anoAtual + (18 - idade)}.')
    elif idade < 18 and 18 - idade > 1:
        print(f'Falta {18 - idade} anos para você se alistar. \nSeu alistamento será em {anoAtual + (18 - idade)}.')
    elif idade > 18 and 18 + idade == 1:
        print(f'Já passou {idade - 18} ano do seu prazo de alistamento. \nSeu alistamento foi em {anoAtual - (idade - 18)}.')
    elif idade > 18 and 18 + idade > 1:
        print(f'Já passou {idade - 18} anos do seu prazo de alistamento. \nSeu alistamento foi em {anoAtual - (idade - 18)}.')
    else:
        print('Já é hora de você se alistar.')
elif genero == 'MULHER':
    print('Você não precisa se alistar.')
else:
    print('Opção inválida. Tente novamente.')

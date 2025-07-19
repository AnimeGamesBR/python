from datetime import date
an = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - an

print(f'O atleta tem {idade} ano.' if idade == 1 else f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif an == 1945:
    print('Adolf bff!')
elif an <= 1600:
    print('Saia escravo podre!')
elif 2001 == an:
    print('11 de setembro...')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

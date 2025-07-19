n1 = float(input('\033[36mDigite a primeira nota:\033[m '))
n2 = float(input('\033[36mDigite a segunda nota:\033[m '))

print(f'\033[36mA média das notas\033[m \033[1;31m{n1:.1f}\033[m \033[36me\033[m \033[1;34m{n2:.1f}\033[m \033[36mé\033[m \033[1;35m{(n1+n2) / 2:.1f}\033[36m!')

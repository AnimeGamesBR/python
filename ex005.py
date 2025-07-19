n = float(input('\033[1;36mDigite um número:\033[m '))

if n.is_integer():
    n = int(n)
    print(f'O número antecessor à \033[1;31m{n:.0f}\033[m é \033[1;34m{n - 1:.0f}\033[m, e o seu sucessor é \033[1;35m{n + 1:.0f}\033[m!')
else:
    print(f'O número antecessor à \033[1;31m{n:.2f}\033[m é \033[1;34m{n-0.01:.2f}\033[m e o seu sucessor é \033[1;35m{n+0.01:.2f}\033[m!')

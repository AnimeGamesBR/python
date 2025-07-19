n = float(input('Digite um número: '))

if n.is_integer():
    n = int(n)
    print(f'O dobro de \033[1;31m{n:.0f}\033[m é \033[1;32m{n*2}\033[m! \nO triplo de \033[1;33m{n:.0f}\033[m é \033[1;34m{n*3}\033[m! \nE a raiz quadrada de \033[1;35m{n:.0f}\033[m é aproximadamente \033[1;36m{n**(1/2):.2f}\033[m!')
else:
    print(f'O dobro de \033[1;31m{n}\033[m é \033[1;32m{n*2}\033[m! \nO triplo de \033[1;33m{n}\033[m é \033[1;34m{n*3}\033[m! \nE a raiz quadrada de \033[1;35m{n}\033[m é aproximadamente \033[1;36m{n**(1/2):.2f}\033[m!')

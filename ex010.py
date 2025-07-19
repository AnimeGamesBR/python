vReal = float(input('Quanto tem na sua carteira? R$'))
cDolar = vReal / 5.76
cEuro = vReal / 6.18

print(f'Você pode comprar \033[1;31mUS${cDolar:.2f}\033[m e \033[1;34mEU${cEuro:.2f}\033[m com \033[1;4;32mR${vReal:.2f}\033[m!')

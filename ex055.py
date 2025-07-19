p = 0
p2 = 100000

for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}°: '))
    if p > peso:
        p = p
    elif p < peso:
        p = peso
    if p2 < peso:
        p2 = p2
    elif p2 > peso:
        p2 = peso

print(f'O maior peso lido foi {p:.2f}!')
print(f'O menor peso lido foi {p2:.2f}!')

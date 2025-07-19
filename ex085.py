n = []
i = 0
for c in range(1, 8):
    v = int(input(f'Digite o {c}° valor: '))
    if v % 2 == 0:
        n.append(v)
    else:
        n.insert(0, v)
        i += 1
print(f'Os valores pares digitados foram: {sorted(n[i:])}')
print(f'Os valores impares digitados foram: {sorted(n[:i])}')

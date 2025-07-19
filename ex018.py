from math import sin, cos, tan, radians

a = float(input('Digite o valor de um ângulo: '))
c = cos(radians(a))
s = sin(radians(a))
t = tan(radians(a))

print(f'O valor {a} tem como SENO {s:.2f}, COSSENO {c:.2f} e TANGENTE {t:.2f}.')

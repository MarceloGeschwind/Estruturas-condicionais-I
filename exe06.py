'''
6- Crie um programa que peça  três lados de um triângulo e diga se ele é Equilátero (3 lados iguais),
Isósceles (2 iguais) ou Escaleno (todos diferentes) .
'''

lado1 = int(input('Fala o lado 1: '))
lado2 = int(input('Fala o lado 2: '))
lado3 = int(input('Fala o lado 3: '))

if lado1 == lado2 == lado3:
    print('Equilátero.')
elif lado1 == lado2 != lado3:
    print('Isósceles.')
elif lado1 != lado2 == lado3:
    print('Isósceles.')
elif lado2 == lado1 != lado3:
    print('Isósceles.')
elif lado1 != lado2 != lado3:
    print('Isósceles.')
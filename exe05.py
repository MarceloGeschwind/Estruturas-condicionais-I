'''
5- Crie um programa que peça a idade e classifique: Menor de 13 (Criança), menor de 20 (Adolescente),
menor de 60 (Adulto) e 60 ou mais (Idoso).
'''

idade = int(input('Qual a idade: '))

if idade < 13:
    print('Criança')
elif idade < 20:
    print('Adolescente')
elif idade < 60:
    print('Adulto')
elif idade > 60:
    print('Idoso.')
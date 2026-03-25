'''
4-  Escreva um programa que vai perguntar ao usuário um número e imprimirá o dia da semana 
correspondente a esse número (1 = domingo, 2 = segunda, etc), ou dizer se o número digitado é 
inválido.
'''

numero = int(input('Fala um número:'))

if numero == 1:
    print('1 = domingo')
    
elif numero == 2:
    print('2 = segunda')
    
elif numero == 3:
    print('3 = terça')
    
elif numero == 4:
    print('4 = quarta')
    
elif numero == 5:
    print('5 = quinta')
    
elif numero == 6:
    print('6 = sexta')
    
elif numero == 7:
    print('7 = sabado')
    
else:
    print('Numero invalido')
    
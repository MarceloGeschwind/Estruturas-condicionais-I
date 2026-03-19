'''1- Faça um programa que leia 2 números e imprima uma mensagem dizendo o maior deles. 
Detalhe: se os números forem iguais, imprima uma mensagem avisando ao usuário.'''

numero = float(input('Fala um numero:'))
numero2 = float(input('Fala outro numero:'))
                
if numero > numero2:
    print('O primeiro numero é maior.')
elif numero2 > numero :
    print('O segundo numero é maior.')
elif numero2 == numero :
    print('Eles são iguais.')
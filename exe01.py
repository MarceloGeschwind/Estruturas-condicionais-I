'''1- Faça um programa que leia 2 números e imprima uma mensagem dizendo o maior deles. 
Detalhe: se os números forem iguais, imprima uma mensagem avisando ao usuário.'''

numero = float(input('Fala um numero:'))
numero2 = float(input('Fala outro numero:'))
                
if numero > numero2:
    print('O numero 1 [{}] é maior que o numero 2 [{}].'.format(numero, numero2))
elif numero2 > numero :
    print('O numero 2 [{}] é maior que o numero 1 [{}].'.format(numero, numero2))
elif numero2 == numero :
    print('o numero 1 [{}] e o número 2 [{}]'.format(numero,numero2))
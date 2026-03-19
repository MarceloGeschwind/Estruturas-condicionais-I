'''
3- Faça um programa que leia três notas de um aluno, calcule sua média aritmética e imprima uma
 mensagem dizendo se o aluno foi aprovado, reprovado ou deverá fazer prova final. O critério de 
aprovação é o seguinte: 
aprovado (média ≥ 7); 
reprovado (média < 3);
prova final ( 3 ≤ média < 7).
'''
n1 = float(input('Nota1:'))

n2 = float(input('Nota2:'))

n3 = float(input('Nota3:'))

media = (n1 + n2 + n3)/3

if n1 > 10:
    print('N1 invalida') 
    sys.exit
if n2 > 10:
    print('N2 invalida') 
    sys.exit
if n3 > 10:
    print('N3 invalida') 
    sys.exit
elif n1<=10 and n1<=10 and n1<=10 :
    print('Ok.')

if media >= 7:
    print('Aprovado.') 
elif media < 3:
    print('Reprovado.') 
elif media <= 3 or media < 7:
    print('Prova final.')
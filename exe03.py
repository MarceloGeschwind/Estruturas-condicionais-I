'''
3- Faça um programa que leia três notas de um aluno, calcule sua média aritmética e imprima uma
 mensagem dizendo se o aluno foi aprovado, reprovado ou deverá fazer prova final. O critério de 
aprovação é o seguinte: 
aprovado (média ≥ 7); 
reprovado (média < 3);
prova final ( 3 ≤ média < 7).
'''
def captura_nota(tipo_nota):
    while(True):
        nota = float(input('Informe a nota{}'.format(tipo_nota)))
        if 0 > nota or nota > 10:
            print('Valor inválido, a nota deve ser entre 0 - 10.')
        else:
            print('Nota gravada.')
            return nota
        
n1 = captura_nota(' N1 ')
n2 = captura_nota(' N2 ')
n3 = captura_nota(' N3' )

media = (n1 + n2 + n3)/3

if media >= 7:
    print('Aprovado.') 
elif media < 3:
    print('Reprovado.') 
elif media <= 3 or media < 7:
    print('Prova final.')
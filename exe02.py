'''
2- Faça um programa que receba uma senha digitada pelo usuário e informe se a mesma é válida ou não
(supondo que a senha válida é “ort123”).
'''

senha = input('Digite a senha: ')
senhacorreta = ('ort123')
if senha == senhacorreta:
    print('Senha valida.')
else:
    print('Senha invalida.')
import random
n1 = str  (input('Digite o nome do primeiro aluno: '))
n2 = str  ( input('Digite o nome do segundo aluno: '))
n3 = str  ( input('Digite o nome do terceiro aluno: '))
n4 = str  ( input( 'Digite o nome do quarto aluno: '))

lista= [n1,n2,n3,n4]
print('A pessoa escolhida para  lavar a  louça foi {}'.format(random.choice(lista)))

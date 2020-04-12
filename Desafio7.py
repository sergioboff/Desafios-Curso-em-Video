nome = str (input('Digite o nome do aluno: '))
n1= float (input ('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota : '))
media = (n1+n2)/2
print('O aluno {}, tirou na primeira prova {:.2f} e na segunda prova {:.2f} tendo uma média {:.2f}'.format(nome,n1,n2,media))
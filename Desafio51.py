#Leitura de um número e razão de Progressão aritmética , exibindo 10 elementos da PA.
n = int(input('Digite o valor da base: '))
r = int(input('Digite o valor da razão de progressão: '))
soma =n
for i in range(1,11):
    soma = soma + r
    print ('Os {}º elemento é :  {}'.format(i, soma))

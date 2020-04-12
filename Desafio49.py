# TABUADA USANDO O FOR
n = int(input('Digite um número para que façamos o calculo da Tabuada: '))

for i in range (1, 11):
    print('{} x {} = {}'.format(n,i,n*i))

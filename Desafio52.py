#leitura de um inteiro verificação se primo

n = int(input('Digite um valor inteiro: '))
x = 0
for i in range(2, n):
    if n % i ==0:
        print('Numero não é Primo')
    else:
        print('Numero  é primo')

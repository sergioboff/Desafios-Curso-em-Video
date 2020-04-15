#leitura de um inteiro verificação se primo
n = int(input('Digite um valor inteiro: '))
x = 0
for i in range(1, n+1):
    if n % i == 0:
        print ('\033[34m', end='')
        x += 1
    else:
        print('\033[31m', end='')
    print ('{}  '.format(i), end='')
print('\n\033[m')
if x == 2:
    print(' O número {} foi divisivel {}x, portanto ele  é Primo'.format(n, x))
else:
    print('O número {} foi divisivel {}x, portanto ele não é Primo'.format(n, x))

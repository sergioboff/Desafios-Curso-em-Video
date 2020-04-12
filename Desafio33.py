num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if num1 > num2 and num3:
    print('O valor {} é o maior valor.'.format(num1))
elif num2 > num3 and num1:
    print('O valor {} é o maior valor'.format(num2))
elif num3 > num2 and num1:
    print('O valor {}  é o maior valor'.format(num3))
else:
    print ('Não há valores diferentes')
#Menor Valor
if num1 < num2 and num3:
    print('Este é o menor valor : {}'.format(num1))
elif num2< num1 and num3:
    print(('Este é o menor valor : {}'.format(num2)))
elif num3< num2 and num1:
    print('Este é o menor valor : {] '.format(num3))
else:
    print('Não há menor valor')

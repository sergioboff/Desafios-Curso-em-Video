#Bases Númericas - Conversão
num = int(input('Digite um numero  inteiro: '))
conversao = int(input( 'Selecione a base de conversão: \n 1.Binário \n 2.Octal \n 3.Hexadecimal\nDigite sua opção: '))
if conversao == 1:
    print('O numero convertido para binario : {}'.format(bin(num)[2:]))
elif conversao == 2:
    print('O numero convertido para Octal : {}'.format(oct(num)[2:]))
elif conversao ==3 :
    print('O numero convertido para Hexadecimal: {}'.format(hex(num)[2:]))
else:
    print('opção inválida')


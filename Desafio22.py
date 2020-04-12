nome = str(input('Digite seu nome : '))
print('O nome em letra Maiuscula é: {}'.format(nome.upper()))
print('O nome em letra minuscula é : {}'.format(nome.lower()))
print('A quantidade de caracteres com espaço é de :{} '.format( len(nome)))
print('A quantidade de caracteres excluindo espaço é de : {}'.format(len(nome.replace(" ",""))))
print ('A função capitalize : {} '.format(nome.capitalize()))
print('Seu primeiro nome possui : {}'.format(nome.find(" ")))
if 'Roberto' in nome:
    print('Sim, Seu nome tem a palavra Roberto')
else:
    print('Seu nome não possui a palavra Roberto')


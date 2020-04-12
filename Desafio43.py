#Calculo de IMC
peso = float (input('Informe seu peso em Kg: '))
altura = float(input('Informe sua altura em Mts : '))
calculo = (peso/(altura**2))
print('Seu Indice de massa Corporea é : {:.2f} '.format(calculo))
if  calculo <=18.5:
    print ('Você está abaixo do peso recomendado, indice de massa corporea de {:.2f}'.format(calculo))
elif calculo <=25:
    print('Você está com seu peso ideal, indice de massa corporea de {:.2f}'.format(calculo))
elif calculo <=30:
    print('Você precisa ir pra Academia, seu indice de massa corporea é {:.2f}, considerado SOBREPESO. '.format(calculo))
elif calculo >40:
    print ('Como é que você se levanta?')
#Multa por KM
velocidade = int (input('Digite a velocidade do Carro: '))
if velocidade <= 80:
    print('Ótimo, você não foi multado')
else:
    y = (velocidade - 80)*7
    print('Você foi multado em R${:.2f}'.format(y))

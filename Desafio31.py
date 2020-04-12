#viagens curtas e longas
viagem = int(input('Digite a KM da sua viagem : '))
if viagem <= 200:
    x = viagem *0.50
    print ('O Custo da sua passagem é de : R${:.2f}'.format(x))
else:
    x = viagem *0.45
    print('O custo da sua passagem é de : R$ {:.2f}'.format(x))


print('='*30,'Calculo para pintura','='*30)
altura = float (input('informe a altura da parede : '))
largura = float (input('informe a largura da parede : '))
area = altura * largura
#1 balde de tinta pode cobrir 2m**2
Qtd = area/2
print('A quantidade de baldes a serem utilizados para area de {}m2 para pintura são : {} baldes'.format(area,Qtd))
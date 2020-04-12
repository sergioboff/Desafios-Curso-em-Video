#Concessão de empréstimo#
bem = float (input('Digite o valor do bem a ser financiado: '))
salario = float(input('Digite o valor da renda familiar : '))
anos = int(input('Qual a quantidade de anos que você pretende pagar o imóvel: '))

resultado = bem/(anos*12)

if resultado <= (salario *0.3) :
    print('Emprestimo concedido')
else:
    print('Emprestimo negado pois o valor da parcela está R${:.2f}, comprometendo a renda do fiduciário.'.format(resultado))
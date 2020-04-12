#Desconto ou acréscimo de acordo com modalidade de pagamento
modo = int(input('Informe seu modo de pagamento : \n[ 1 ] À vista (dinheiro ou cheque);\n[ 2 ] À vista no cartão de débito;'
                 '\n[ 3 ] Em duas vezes no crédito;\n'
                 '[ 4 ] Em 3x no cartão de crédito;\n Informe sua opção:'))
preço = int(input('Informe o valor do produto : '))
if modo == 1:
    print('Você optou por pagamento a vista, para esse modo de pagamento é aplicado 10% de desconto, sendo o valor da sua compra de R${:.2f}'.format(preço*0.9))
elif modo ==2:
    print('Você optou por modo de pagamento a vista no débito, aplicamos um desconto de 5% , sendo o valor final de R${:.2f} '.format(preço*0.95))
elif modo ==3:
    print('Você optou por duas vezes no cartão de crédito, as parcelas serão de 2 X R$3{:.2f}'.format(preço/2))
elif modo==4:
    print('Nessa opção de pagamento é acrescido um valor para repasse de tributos, sendo  o preço final de R${:.2f} em parcelas de 3 X de R${:.2f}'.format(preço*1.2,((preço*1.2)/3)))
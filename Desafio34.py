#calculodeSalario
salario= int(input('Digite o valor do seu salário : '))
if salario < 1250:
    salario = salario *1.15
    print ('Seu novo sálario passa a ser de R${:.2f}'.format(salario))
else:
    salario > 1250
    salario =salario *1.10
    print('Seu novo salário passa a ser de R${:.2f}'.format(salario))
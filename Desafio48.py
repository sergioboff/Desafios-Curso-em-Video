# Soma de todos os números divisiveis por 3 até 500;
soma=0
for i in range (0,501):
    if i % 3 == 0:
        soma = soma+i
        print('O indice: {} e o valor {}'.format(i,soma))


print (' A soma de todos os números divisiveis por 3 até 500 é {}'.format(soma))

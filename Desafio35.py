#Desafio do principio triangular - Soma de dois lados, maior que o outro lado
retaA = int(input('Digite o valor em cm da reta A: '))
retaB = int(input('Digite o valor em cm da reta B: '))
retaC = int(input('Digite o valor em cm da reta C: '))
if retaA+retaB < retaC:
    print('Não existe possibilidade de construir um triangulo')
elif retaB + retaC < retaA:
    print('Não existe possibilidade de construir um triangulo')
elif retaC + retaA < retaB:
    print('Não existe possibilidade de construir um triangulo')
else:
    print('O triangulo possui medidas : A : {}cm, B:{}cm e C:{}cm'.format(retaA,retaB,retaC))
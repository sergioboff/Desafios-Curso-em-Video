#partindo do principio fundamental do triangulo informar se é equilatero, escaleno ou isosceles
retaA = int(input('Digite o valor em CM para a reta A: '))
retaB = int(input('Digite o valor em CM para a reta B: '))
retaC = int(input('Digite o valor em CM para a reta C: '))
if  retaA + retaB < retaC:
    print('Não há possibilidades de um triangulo')
elif retaB + retaC < retaA:
    print('Não há possibilidades de um triangulo')
elif retaC + retaA < retaB:
    print('Não há possibilidade de um triangulo')
else:
    if retaA == retaB == retaC:
        print('Este é um triangulo Equilátero com retas : A {}cm , B {}cm e C {}cm iguais.'.format(retaA,retaB,retaC))
    elif retaA == retaB or retaB == retaC or retaC==retaA:
        print('Este é um triangulo Isosceceles')
    else:
        print('Este triangulo é escaleno')
import math
catop = float (input('Digite o comprimento do Cateto Oposto : '))
catad = float (input('Digite o comprimento do Cateto Adjacente: '))
hip = sum ((math.pow(catop,2), math.pow(catad,2)))
print('O valor da hipotenusa e : {}'.format(math.sqrt(hip)))
print ('O valor da hipotenusa é : {}'.format(math.hypot(catad,catop)))
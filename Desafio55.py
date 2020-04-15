import math
peso = []
for i in range (1, 6):
    x = float(input('Digite o peso da {}º pessoa : '.format(i)))
    peso.append(x)
peso.sort()
print('O menor peso medido foi {}'.format(peso[0]))
print('O maior peso medido foi {}'.format(peso[-1]))
print('A media dos pesos é de {}'.format(sum(peso)/len(peso)))
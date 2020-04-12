import random
print('Olá , Meu nome é BIT e quero jogar, um jogo com você!')
print('Vou pensar em um número de 0 a 5 e você deve adivinhar')
print(' Boa sorte!')
num = int(input('Digite seu palpite : '))
x = random.randrange(0,5)
if num == x:
    print('Parabéns você acertou!')
else:
    print('Tente novamente.')

print('Pensei no numero : {}'.format(x))
#Jogo do Jokenpo
import random
item = ('pedra', 'papel', 'tesoura')
CPU = (random.randint(0,2))
print(item[CPU])
print('################   Bem Vindo ao jogo do JokenPô ############################')

#for i in a range( 0, n)
player = int(input('Selecione sua opção \n[ 0 ] - Pedra \n[ 1 ] - Papel \n[ 2 ] - Tesoura\nDigite sua opção: '))
if CPU is 0 and player is 0:
    print('Empate')
elif CPU is 0 and player is 1:
    print('Parabéns você ganhou!')
elif CPU is 0 and player is 2:
    print('A CPU venceu.\n ')
elif CPU is 1 and player is 0:
    print( 'A CPU venceu!\n ')
elif CPU is 1 and player is 1:
    print('Empate\n ')
elif CPU is 1 and player is 2:
    print('Parabéns você ganhou!\n ')
elif CPU is 2 and player is 0:
    print('Parabéns você venceu!\n')
elif CPU is 2 and player is 1:
    print('CPU venceu!!\n')
elif CPU is 2 and player is 2:
    print('Empate!')
else:
    print('opção invalida')


print ('A CPU selecionou {} e você selecionou {}' .format(item[CPU],item[player]))

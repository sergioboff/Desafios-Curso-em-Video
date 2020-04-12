# alistamento militar
import datetime
ano = int(input('Digite o ano de nascimento :  '))
atual = datetime.date.today().year
idade = atual - ano
if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!!!')
elif idade > 18:
    print('Você já passou do tempo de se alistar.Voce deveria ter se alistado a {} anos atrás'.format((idade-18)))
else:
    print ('Você ainda não possui o tempo para alistamento, seu alistamento deve ocorrer em : {} anos'.format(18-idade))

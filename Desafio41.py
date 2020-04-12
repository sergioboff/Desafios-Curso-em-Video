#classificação dos nadadores
import datetime
ano = int(input('Digite o ano do atleta : '))
atual = datetime.date.today().year
saldo = atual - ano
if  saldo <= 9:
    print('Parabéns, com sua idade de {} você é um mini atleta: Categoria Mirim'.format(saldo))
elif saldo <=14:
    print('Parabéns, com sua idade de {} , você cresceu um pouco, passou para categoria : Categoria Infantil'.format(saldo))
elif saldo <= 19:
    print('Parabéns, você está passou para categoria  Junior com seus {} anos'.format(saldo))
elif saldo  <= 20:
    print ('Parabéns você está em sua melhor forma, {} anos, agora você é Senior '.format(saldo))
elif saldo >=21:
    print('Parabéns você é MASTER')


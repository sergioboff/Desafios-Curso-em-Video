frase = str(input('Digite uma frase : ')).strip()
lower=frase.lower()
print('##########################################################################')
print('#################   A N A L I Z A N D O   A   F R A S E  #################')
print('##########################################################################')
print ('A Letra A aparece {} '.format(lower.count('a')))
print ('A Letra A aparece na posição {}'.format (lower.find('a')))
print ('A letra A aparece pela ultima vez na frase na posição {}'.format(lower.rfind('a')))
print ('A quantidade de caracteres é de : {}'.format(len(lower)))
print ('A quantidade de caracteres sem espaço corresponde : {}'.format (len(lower.replace(" ",""))))
print ('############################################################################')
from datetime import date
ano = []
atual = date.today().year
print(atual)
menor = 0
maior = 0
for i in range(1, 8):
    x = int(input('Em que ano {}º pessoa nasceu : '.format(i)))
    ano.append(x)
for i in range(0, len(ano)):
    if atual - ano[i] > 21:
        maior += 1
    else:
        menor += 1
print('Há um Total de {} pessoas, sendo que :'.format(len(ano)))
print('Temos {} pessoas com maior idade'.format(maior))
print('Temos {} pessoas que são de menor idade'.format(menor))

num =list()
impares= list()
while True:
    num.append(int(input('Digite um número: ')))
    r= str(input('Quer continuar ? [S/N]'))
    if r in 'Nn':
        break
for i , v in enumerate (num):
    if v % 2 == 1:
        impares.append(v)

print(max(num)-min(num))
print('=' *30)
print(impares)
print('A quantidade de impares: {}3'
      ''.format(len(impares)))
#print(sum(num))
#print(sum(num)/len(num))



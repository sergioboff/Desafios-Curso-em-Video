#Soma somente de números pares
soma=0
cont=0
for i in range(1,7):
    n=int(input('Digite numero: '))
    if n % 2==0:
        soma =soma +n
        cont=cont+1
print('A soma dos {} números pares é:{}'.format(cont,soma))
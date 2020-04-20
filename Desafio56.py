#Leitura de um conjunto de dados e análise
#Homem mais velho
#Media de Idade
#Volume de mulheres com menos de 20 anos
Idade = []
Sexo = []
Nome = []
for i in range (0, 6):
    z = str (input('Digite seu Nome : ')).strip()
    x = int (input('Digite sua Idade : '))
    y = str (input('Informe seu sexo : [M / F] :')).upper().strip()
    print('--'*30)
    Nome.append(z)
    Sexo.append(y)
    Idade.append(x)

for i in range (0, len(Sexo)):
    if Sexo[i] in 'M':
        print( Idade[i])


print('A Média das idades é de : {} anos'.format(sum(Idade)/len(Idade)))
#print('De uma população de {} a quantidade de mulheres é de : {} '.format (Sexo.count(),Sexo.count('F')))


print('O Homem mais velho possui idade de : {} anos'.format(Sexo=='mM' and Idade[-1]))
print(Idade)
print(Sexo)
print(Nome)

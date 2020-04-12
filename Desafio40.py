#calculo de uma média de duas notas
num = int(input('Por favor digite o número de alunos da sala : '))
for i in range(0,num):
    nota1=float(input('Digite a primeira nota: '))
    nota2=float(input('Digite a segunda nota: '))
    mean = (nota1+nota2)/2
    if mean > 7:
        print('Aluno Aprovado')
    elif mean >= 5 <= 6.9:
        print('Aluno em Recuperação')
    else:
        print('Aluno reprovado')






# Detector de Palindromo
frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
junto = ''.join(separar)
inverso = ''
for i in range(len(junto)-1, -1, -1):
    inverso += junto[i]
print(inverso, junto)

if inverso == junto:
    print("É um Palindromo")
else:
    print('Não é um Palindromo')
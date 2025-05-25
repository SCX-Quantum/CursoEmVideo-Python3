#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;31m='+'\033[1;35m-')+'\033[1;31m=\n\033[m'
titulo = '\033[1;35m       COMPARADOR DE NÚMEROS\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('Por favor insira as informações abaixo:'.center(60))
print ('')
print (line)

#Solicitação de informações

num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
print ('')
print (line)

#Condicionamento

if num1 == num2:
    print('Os dois números são iguais.')
    print('')
    print(line)
elif num1 > num2:
    print('O primeiro número é maior.')
    print('')
    print(line)
else:
    print('O segundo número é maior.')
    print('')
    print(line)
#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;32m='+'\033[1;36m-')+'\033[1;32m=\n\033[m'
titulo = '\033[1;36m       CONVERSOR DE BASES NUMÉRICAS\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('Por favor insira as informações abaixo:'.center(60))
print ('')
print (line)

#Solicitação de informações

num = int(input('Digite um número para conversão: '))
option = int(input('[1]BINÁRIO [2]OCTAL [3]HEXADECIMAL  : '))
print('')
print (line)

#Condicionamento

if option == 1:
    print(f'O número {num} em BINÁRIO é: {bin(num)[2:]}.')
    print('')
    print(line)
elif option == 2:
    print(f'O número {num} em OCTAL é: {oct(num)[2:]}.')
    print('')
    print(line)
elif option == 3:
    print(f'O número {num} em HEXADECIMAL é: {hex(num)[2:]}.')
    print('')
    print(line)
else:
    print('Opção digitada inválida.')
    print('')
    print(line)




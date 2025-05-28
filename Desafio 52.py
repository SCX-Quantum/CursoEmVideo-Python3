
#EXECUTEI O CODIGO DE EFORMA MAIS EFICIENTE, TESTANDO APENAS ATÉ A RAIZ QUADRADA DO NUM,
#EXCLUINDO NÚMEROS PARES E TESTANDO APENAS OS IMPARES.


#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;35m&'+'\033[1;32m*')+'\033[1;35m&\n\033[m'
titulo = '\033[1;36m           IDENTIFICADOR DE NÚMEROS\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('PRIMOS...'.center(60))
print ('')
print (line)

#Solicitando valores:

num = int(input('Digite um número inteiro para eu avaliar:'))
print('')
print(line)

#Condicionamento:

if num <= 1 or num == 2:
    print(f'{num} não é PRIMO'.center(60))
    print('')
    print(line)

elif num % 2 == 0:
    print(f'{num} não é PRIMO'.center(60))
    print('')
    print(line)

else:
    for c in range (3, int(num**0.5) + 1, 2):
        if num % c == 0:
            print(f'{num} não é PRIMO'.center(60))
            print('')
            print(line)
            break
    else:
        print(f'{num} É PRIMO'.center(60))
        print('')
        print(line)
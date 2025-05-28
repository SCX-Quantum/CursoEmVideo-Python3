#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;35m&'+'\033[1;32m*')+'\033[1;35m&\n\033[m'
titulo = '\033[1;36m          PROGRESSÃO ARITMÉTICA\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('INSIRA AS INFORMAÇÕES ABAIXO:'.center(60))
print ('')
print (line)

#Solicitando valores:

num = int(input('Qual o primeiro termo?: '))
raz = int(input('Qual a razão aplicada? '))

print ('')
print (line)

#Condicionamento

for i in range(10):
    termo = num + i * raz
    print(termo, end=' → ')

print ('...')
print ('')
print (line)


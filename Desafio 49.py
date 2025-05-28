#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;35m&'+'\033[1;32m*')+'\033[1;35m&\n\033[m'
titulo = '\033[1;36m           TABUADA 2.0\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('AGORA USANDO A ESTRUTURA DE LAÇO'.center(60))
print ('')
print (line)

#Solicitando valores

num = int(input('Qual o número que deseja saber a tabuada ?'))
max = int(input('Até quantas vezes quer saber ?'))
print ('')
print (line)

#Condicionamento

for c in range (1, ( max + 1 )):
    print(f'{num} x {c} = {(num * c)}')

print ('')
print (line)

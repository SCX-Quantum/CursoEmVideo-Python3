#Importando biblioteca de timer

from time import sleep

#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;35m&'+'\033[1;32m*')+'\033[1;35m&\n\033[m'
titulo = '\033[1;36m           TODOS OS NÚMEROS PARES ENTRE 1 E 50\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('Faremos a impressão automáticamente:'.center(60))
print ('')
print (line)
sleep(3)

#Condicionamento:

for c in range ( 2, 51, 2 ):
        print(c)

print ('')
print (line)
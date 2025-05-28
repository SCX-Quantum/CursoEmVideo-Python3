#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;35m&'+'\033[1;32m*')+'\033[1;35m&\n\033[m'
titulo = '\033[1;36m           IMPARES ENTRE 1 E 500\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('Além disso precisam ser múltiplos de 3.'.center(60))
print ('')
print (line)

#Solicitando valores:

soma = 0
for c in range ( 1, 500):
    if c % 2 != 0 and c % 3 == 0:
        soma += c

print(f'A Soma de todos os núemeros é {soma}'.center(60))


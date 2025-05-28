#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;35m&'+'\033[1;32m*')+'\033[1;35m&\n\033[m'
titulo = '\033[1;36m           COMPARADOR DE PESOS\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('TUDO SERÁ ANALISADO EM KILOGRAMAS'.center(60))
print ('')
print (line)

#Solicitando valores:

peso = float(input('Digite o peso da 1ª pessoa:'))
max = peso
min = peso

for c in range ( 2, 6 ):
    peso = float(input(f'Digite o peso da {c}ª pessoa:'))
    if peso >= max :
        max = peso
    elif peso <= min:
        min = peso

print ('')
print (line)
print(f'O Maior peso digitado foi {max:.2f}Kg\nO Menor peso digitado foi {min:.2f}Kg')
print ('')
print (line)

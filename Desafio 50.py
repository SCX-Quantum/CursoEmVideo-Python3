#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;35m&'+'\033[1;32m*')+'\033[1;35m&\n\033[m'
titulo = '\033[1;36m           SOMAR APENAS VALORES PARES\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('VALORES IMPARES SERÃO DESCONSIDERADOS.'.center(60))
print ('')
print (line)

#Solicitando valores com condicionamento:

soma = 0
for c in range ( 1, 7 ):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        soma += num

print ('')
print (line)
print(f'A soma total dos valores PARES digitados foi: {soma}.'.center(60))
print ('')
print (line)





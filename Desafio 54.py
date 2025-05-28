#Importando bibliotecas

from datetime import date
ano_atual = date.today().year

#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;35m&'+'\033[1;32m*')+'\033[1;35m&\n\033[m'
titulo = '\033[1;36m           ANALISADOR DE MAOIRIDADE\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('INSIRA O ANO DE NASCIMENTO DE 7 PESSOAS:'.center(60))
print ('')
print (line)

#Solicitando valores:
maiores = 0
menores = 0
for c in range (1, 8):
    ano_nasc = int(input(f'Digite a {c}ª data de nascimento:'))
    idade = ( ano_atual - ano_nasc )
    if idade <= 21:
        menores += 1
    else:
        maiores += 1

print ('')
print (line)
print('De acordo com as datas inseridas: '.center(60))
print(f'{menores} dessas pessoas são MENORES de idade e {maiores} são MAIORES.'.center(60))
print ('')
print (line)

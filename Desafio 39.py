#Importando bibliotecas para data atual

from datetime import date

ano_atual = date.today().year

#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;32m='+'\033[1;33m-')+'\033[1;32m=\n\033[m'
titulo = '\033[1;31m       ALISTAMENTO MILITAR\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('Por favor insira as informações abaixo:'.center(60))
print ('')
print (line)

#Solicitação de informações

data = int(input('Digite o ano do seu nascimento:'))
idade = ano_atual - data
print ('')
print (line)

#Condicionamento
if idade == 18:
    print('Você deve se alistar \033[1;31mIMEDIATAMENTE\033[m!')
    print('')
    print(line)
elif idade < 18:
    print('Não chegou a hora de você se alistar.')
    print(f'Faltam {18 - idade} anos para você se apresentar.')
    print('')
    print(line)
elif idade > 18:
    print('Já passou do seu tempo de se alistar.')
    print(f'Você deveria ter se apresentado a {idade - 18} anos atras.')
    print('')
    print(line)
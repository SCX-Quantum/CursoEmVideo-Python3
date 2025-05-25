#Importando bibliotecas para data atual

from datetime import date

ano_atual = date.today().year

#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;31m='+'\033[1;35m-')+'\033[1;31m=\n\033[m'
titulo = '\033[1;35m       CLASSIFICADOR DE ATLETAS\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('Definiremos a sua classificação nos esportes Olímpicos.'.center(60))
print ('')
print (line)

#Solicitação idade do usuário:
ano = int(input('Digite em que ano você nasceu:'))
idade = ano_atual - ano
print ('')
print (line)

#Condicionamento

if idade <= 9:
    print('Sua categoria é MIRIM'.center(60))
    print('')
    print(line)
elif idade <= 14:
    print('Sua categoria é INFANTIL'.center(60))
    print('')
    print(line)
elif idade <= 19:
    print('Sua categoria é JÚNIOR'.center(60))
    print('')
    print(line)
elif idade <= 20:
    print('Sua categoria é SÊNIOR'.center(60))
    print('')
    print(line)
else:
    print('Sua categoria é MASTER'.center(60))
    print('')
    print(line)
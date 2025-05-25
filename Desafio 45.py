#Importando a biblioteca

from time import sleep
from random import choice

#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;31m='+'\033[1;35m-')+'\033[1;31m=\n\033[m'
titulo = '\033[1;33m       JO - KEN - PO\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('Está preparado para perder?'.center(60))
print ('')
print (line)

#Criando jogada da máquina:

jogadas = ['PEDRA','PAPEL','TESOURA']
jog_pc = choice(jogadas)

#Solicitação de jogada:

jog_user = str(input('PEDRA, PAPEL OU TESOURA?:')).strip().upper()
print ('')
print (line)

#Variavel de definição de resultado.

result = 0

#Condicionamento

if jog_user == jog_pc:
    result += 0
elif jog_user == 'PEDRA' and jog_pc == 'PAPEL':
    result -=1
elif jog_user == 'PAPEL' and jog_pc == 'TESOURA':
    result -= 1
elif jog_user == 'TESOURA' and jog_pc == 'PEDRA':
    result -= 1
elif jog_user == 'PEDRA' and jog_pc == 'TESOURA':
    result +=1
elif jog_user == 'PAPEL' and jog_pc == 'PEDRA':
    result += 1
elif jog_user == 'TESOURA' and jog_pc == 'PAPEL':
    result += 1

#simulação de processamento.

print('...')
sleep(1)
print('JO')
sleep(0.3)
print('KEN')
sleep (0.3)
print ('PO')
sleep (0.5)
print('...')
sleep (1)
print ('')
print (line)

#Resultado.

print(f'Eu joguei {jog_pc} e você jogou {jog_user}.'.center(60))
if result == 0:
    print('EMPATAMOS'.center(60))
    print('')
    print(line)
elif result == 1:
    print('VOCÊ VENCEU!'.center(60))
    print('')
    print(line)
else:
    print('VOCÊ PERDEU'.center(60))
    print('')
    print(line)






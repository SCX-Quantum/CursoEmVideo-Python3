from random import randint

num_pc = randint(1,500)

#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;32m|'+'\033[1;31m=')+'\033[1;32m|\n\033[m'
titulo = '\033[1;36m           ADVINHE O NÚMERO\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('Pronto para perder várias vezes?'.center(60))
print ('Pensei em um número entre 1 e 500.'.center(60))
print ('')
print (line)

contador = 1
num_jogador = int(input('Digite o seu palpite:'))
while num_jogador != num_pc:
    if num_jogador < num_pc:
        print ('Meu número é \033[1;31mMAIOR\033[m, tente novamente.')
        num_jogador = int(input('-->'))
        contador += 1
    elif num_jogador > num_pc:
        print ('Meu número é \033[1;36mMENOR\033[m, tente novamente.')
        num_jogador = int(input('-->'))
        contador += 1

print ('')
print (line)
print ('Finalmente acertou!!!'.center(60))
print (f'Você precisou de {contador} tentativas.'.center(60))
print ('')
print (line)

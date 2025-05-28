#Importando biblioteca de timer

from time import sleep

#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;35m&'+'\033[1;32m*')+'\033[1;35m&\n\033[m'
titulo = '\033[1;36m           CONTAGEM REGRESSIVA\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('O ANO VAI MUDAR... ACOMPANHE A CONTAGEM:'.center(60))
print ('')
print (line)

#Condicionamento:
for n in range( 10, 0, -1 ):
    print (n)
    print ('...')
    sleep (1)

# Lista de cores ANSI
colors = [
    '\033[91m',  # Vermelho
    '\033[92m',  # Verde
    '\033[93m',  # Amarelo
    '\033[94m',  # Azul
    '\033[95m',  # Magenta
    '\033[96m',  # Ciano
]

# Representações dos fogos de artifício
fireworks = [
    "        *\n       ***\n      *****\n     *******\n      *****\n       ***\n        *",
    "    .''.      \n  .:o o:.     \n .:  o  o:.   \n ':     :'    \n   ':::''     ",
    "    *   *   *\n  *    *    *\n *  *     *  *\n  *    *    *\n    *   *   *",
]

# Animação dos fogos de artifício
for i in range(5):
    color = colors[i % len(colors)]
    firework = fireworks[i % len(fireworks)]
    print(f"{color}{firework}\033[0m")
    sleep(0.5)

print ('')
print (line)
print('FELIZ ANO NOVOOOOOO!!!!'.center(60))
print ('')
print (line)
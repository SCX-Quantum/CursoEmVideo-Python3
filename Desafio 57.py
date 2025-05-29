#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;32m|'+'\033[1;31m=')+'\033[1;32m|\n\033[m'
titulo = '\033[1;36m           ANALISADOR DE PESSOAS\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('Queremos apenas saber o seu sexo.'.center(60))
print ('')
print (line)

sexo = str(input('[M] [F] : ')).strip().upper()
while sexo[0] not in 'MF':
    print('Comando inválido')
    sexo = str(input('[M] [F] : ')).strip().upper()

print ('')
print (line)
print('DADOS REGISTRADOS COM SUCESSO!'.center(60))
print ('')
print (line)

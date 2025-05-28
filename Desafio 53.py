#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;35m&'+'\033[1;32m*')+'\033[1;35m&\n\033[m'
titulo = '\033[1;36m           PALINDROMOS\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('DIGITE A SUA FRASE ABAIXO:'.center(60))
print ('')
print (line)

#Solicitando valores:

txt = str(input('--->')).strip().upper()
txt_cut = txt.replace(' ','')
print ('')
print (line)

#Fatiamento e verificação

if txt_cut == txt_cut[::-1]:
    print(f'Essa frase é um palindromo.'.center(60))
    print('')
    print(line)
    print(f'Normal: \n{txt_cut}')
    print(f'Ao contrário: \n{txt_cut[::-1]}')
    print('')
    print(line)
else:
    print('Essa frase Não é palíndromo!'.center(60))
    print('')
    print(line)
    print(f'Normal: \n{txt_cut}')
    print(f'Ao contrário: \n{txt_cut[::-1]}')
    print('')
    print(line)
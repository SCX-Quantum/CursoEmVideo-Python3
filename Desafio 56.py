#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;35m&'+'\033[1;32m*')+'\033[1;35m&\n\033[m'
titulo = '\033[1;36m           ANALISADOR DE PESSOAS\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('DIGITE NOME IDADE E SEXO DE 4 PESSOAS.'.center(60))
print ('')
print (line)

#Solicitando valores:

media = 0
idade_max = 0
homem_mais_velho = ''
mulheres_menores = 0

for c in range ( 1, 5 ):
    print(f'#PESSOA {c}:')
    nome = str(input('NOME: ')).strip().upper()
    sexo = str(input('SEXO [M] [F]: ')).strip().upper()
    idade = int(input('IDADE: '))
    media += idade
    print('')
    print(line)

    if sexo[0] == 'M':
        if idade > idade_max:
            idade_max = idade
            homem_mais_velho = nome

    elif sexo[0] == 'F':
        if idade < 20:
            mulheres_menores += 1


print('Aqui está detalhadamente oque a pesquisa nos forneceu:'.center(60))
print('')
print(line)
print(f'''
[MÉDIA DE IDADE]:{(media/4)}
[NOME DO HOMEM MAIS VELHO]:{homem_mais_velho}
[MULHERES MENOR DE IDADE]: {mulheres_menores}''')
print('')
print(line)



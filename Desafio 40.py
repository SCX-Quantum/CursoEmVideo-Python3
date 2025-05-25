#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;31m='+'\033[1;35m-')+'\033[1;31m=\n\033[m'
titulo = '\033[1;35m       ANÁLISE DE ALUNOS\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('Digite sua matéria e notas escolares para analise:'.center(60))
print ('')
print (line)

#Solicitação de qual matéria analisar.

while True:
    print('Matérias disponíveis:'.center(60))
    print('[1]MATEMÁTICA [2]PORTUGUÊS'.center(60))
    curso = int(input('--->'))
    print('')
    print(line)
    if curso == 1:
        materia = ('Matemática')
        break
    elif curso == 2:
        materia = ('Português')
        break
    else:
        print('\033[1;31mOpção inválida\nTente Novamente\033[m')
        print('')
        print(line)

#Solicitando as 3 notas:

nota1 = float(input('1ª Nota:'))
nota2 = float(input('2ª Nota:'))
nota3 = float(input('3ª Nota:'))
media = (nota1 + nota2 + nota3) / 3
print('')
print(line)

#Dividindo entre matemática ou português para diferentes analises.

if curso == 1:
    if media < 60:
        print(f'Sua média foi: {media:.2f}'.center(60))
        print('REPROVADO'.center(60))
        print('')
        print(line)
    elif 60 < media < 80:
        print(f'Sua média foi: {media:.2f}'.center(60))
        print('RECUPERAÇÃO'.center(60))
        print('')
        print(line)
    elif media > 80:
        print(f'Sua média foi: {media:.2f}'.center(60))
        print('APROVADO'.center(60))
        print('')
        print(line)

elif curso == 2:
    if media <= 49:
        print(f'Sua média foi: {media:.2f}'.center(60))
        print('REPROVADO'.center(60))
        print('')
        print(line)
    elif 50 < media < 70:
        print(f'Sua média foi: {media:.2f}'.center(60))
        print('RECUPERAÇÃO'.center(60))
        print('')
        print(line)
    elif media >= 70:
        print(f'Sua média foi: {media:.2f}'.center(60))
        print('APROVADO'.center(60))
        print('')
        print(line)


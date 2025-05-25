#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;34m='+'\033[1;33m-')+'\033[1;34m=\n\033[m'
titulo = '\033[1;33m       CALCULO DE IMC\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('Insira as informações e verifique sua saúde corporal.'.center(60))
print ('')
print (line)

#Solicitando valores:

peso = float(input('Digite o seu peso atual:'))
altura = float(input('Digite sua altura atual:'))
imc = peso / ( altura ** 2 )
print ('')
print (line)

#Condicionamento

if imc < 18.5:
    print('Você está abaixo do peso.')
    print('')
    print(line)
elif imc < 25:
    print('Você está no peso ideal.')
    print('')
    print(line)
elif imc < 30:
    print('Você está acima do peso.')
    print('')
    print(line)
elif imc < 40:
    print('Você está com Obesidade.')
    print('')
    print(line)
elif imc > 40:
    print('Você está com Obesidade Mórbida.')
    print('')
    print(line)

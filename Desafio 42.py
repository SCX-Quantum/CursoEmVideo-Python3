#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;30m='+'\033[1;35m-')+'\033[1;30m=\n\033[m'
titulo = '\033[1;33m       ANALISADOR DE TRIANGULOS 2.0\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('Verificaremos os segmentos e analisaremos sua forma.'.center(60))
print ('')
print (line)

#Solicitando valores:

num1 = int(input('Digite o primeiro segmento:'))
num2 = int(input('Digite o  segundo segmento:'))
num3 = int(input('Digite o terceiro segmento:'))
print ('')
print (line)

#Condicionamento:

if num1 < num2 + num3 and num2 < num1 + num2 and num3 < num1 + num2:
    if num1 == num2 == num3:
        print('Este triângulo é Equilátero.')
        print('')
        print(line)
    elif num1 != num2 != num3 != num1:
        print('Este triangulo é Escaleno.')
        print('')
        print(line)
    else:
        print('Este triangulo é Isoceles.')
        print('')
        print(line)
else:
    print('Esses segmentos de reta NÃO PODEM formar um triangulo')
    print('')
    print(line)
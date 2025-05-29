#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;32m|'+'\033[1;31m=')+'\033[1;32m|\n\033[m'
titulo = '\033[1;36m           CALCULADORA SIMPLES\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('DIGITE OS VALORES E ESCOLHA A OPERAÇÃO:'.center(60))
print ('')
print (line)

#Solicitação

num1 = 0
num2 = 0
app_on = 1
while app_on != 0:
    num1 = int(input('Digite o 1º número:'))
    num2 = int(input('Digite o 2º número:'))
    print('')
    print(line)
    print('Qual a operação que deseja realizar?:')
    print('[1]SOMA '
          '[2]SUBTRAÇÃO '
          '[3]MULTIPLICAÇÃO '
          '[4]DIVISÃO '
          '[5]SAIR')
    opt = int(input('--->'))
    print('')
    print(line)

    #Condicionamento:

    if opt == 1:
        print(f'A soma entre {num1} e {num2} é {(num1+num2)}')
        print('')
        print(line)
        while True:
            continuar = str(input('Continuar?: [S] [N]')).strip().upper()
            if continuar == 'N':
                app_on = 0
                break
            elif continuar == 'S':
                print('')
                print(line)
                break
            else:
                print('Comando inválido.')

    elif opt == 2:
        print(f'A subtração entre {num1} e {num2} é {(num1-num2)}')
        print('')
        print(line)
        while True:
            continuar = str(input('Continuar?: [S] [N]')).strip().upper()
            if continuar == 'N':
                app_on = 0
                break
            elif continuar == 'S':
                print('')
                print(line)
                break
            else:
                print('Comando inválido.')


    elif opt == 3:
        print(f'A multiplicação entre {num1} e {num2} é {(num1*num2)}')
        print('')
        print(line)
        while True:
            continuar = str(input('Continuar?: [S] [N]')).strip().upper()
            if continuar == 'N':
                app_on = 0
                break
            elif continuar == 'S':
                print('')
                print(line)
                break
            else:
                print('Comando inválido.')


    elif opt == 4:
        print(f'A divisão entre {num1} e {num2} é {(num1/num2):.2f}')
        print('')
        print(line)
        while True:
            continuar = str(input('Continuar?: [S] [N]')).strip().upper()
            if continuar == 'N':
                app_on = 0
                break
            elif continuar == 'S':
                print('')
                print(line)
                break
            else:
                print('Comando inválido.')

    elif opt == 5:
        app_on = 0

    else:
        print('Comando inválido.Insira as informações novamente')
        print('')
        print(line)

print('Obrigado por usar os nossos serviços.'.centetr(60))
print('')
print(line)
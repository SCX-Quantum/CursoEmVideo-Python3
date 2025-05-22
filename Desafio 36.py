#Importando Bibliotecas:
from time import sleep
    #importar sleep para simular processamento da máquina

#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;33m='+'\033[1;31m-')+'\033[1;33m=\n\033[m'
titulo = '\033[1;33m       EMPRÉSTIMOS ITAÚ\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('Bem vindo ao simulador da CASA PRÓPRIA.'.center(60))
print ('Por favor insira as informações abaixo:'.center(60))
print ('')
print (line)

#Solicitação de informações:

valor = float(input('Qual o valor da casa que deseja financiar?:\nR$ '))
renda = float(input('Qual seria sua renda mensal atualmente?:\nR$ '))
prazo_anos = int(input('Em quantos anos pretende pagar o empreendimento?\nR$ '))
    #convertendo prazo para meses
prazo_meses = prazo_anos * 12

print ('')

#Simulação de processamento

print (line)
print ('Informações registradas com sucesso!'.center(60))
print ('')
print ('...'.center(60))
print ('PROCESSANDO'.center(60))
print ('...'.center(60))
print ('')
print (line)
sleep (2)

#Processamento das condicionais:
    #Interromper processo por prazo acima do limite.
if prazo_anos > 45:
    print ('     \033[1;31mPROCESSO NEGADO\033[m'.center(60))
    print ('Não é permitido financiamentos acima de 45 anos.\n'.center(60))
    print (line)
    #Se o salario da pessoa ser impossivel de pagar o empréstimo dentro do prazo
elif (renda * prazo_meses) < valor:
    print('Com a renda mensal e o valor do financiamento informados'.center(60))
    print('        Seria \033[1;31mIMPOSSIVEL\033[m realizar esse processo.\n'.center(60))
    print(line)
    #Se o valor da parcela ser menor que 30% do salário
elif (valor / prazo_meses) < (renda * 30 / 100):
    print ('       \033[4;32mEMPRÉSTIMO CONCEDIDO!\033[m'.center(60))
    print ('')
    print (f'Contrato efetivado no valor de \033[1;33mR$\033[1;32m {valor:.2f}\033[m \nem \033[1;32m{prazo_meses}\033[m parcelas de \033[1;33mR$\033[1;32m {(valor / prazo_meses):.2f}\033[m.\n')
    print (line)
    #Se o valor da parcela estiver entre 30% e 50% do salário
elif (valor / prazo_meses) > (renda * 30 / 100) and (valor / prazo_meses) < (renda * 50 / 100):
    print ('Não é possivel conceder o empréstimo nestas condições'.center(60))
    print ('      '
           '\033[4;32mRealize outra proposta...\033[m'.center(60))
    print(line)
    #Se o valor da parcelas ser acima de 50% do salário
else:
    print ('\033[1;31mSistema fora do Ar. Volte mais tarde.\033[m\n')
    print (line)
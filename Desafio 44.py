#Definindo um Layout da linha/ Titulo do Desafio:

line = 30 * ('\033[1;35m='+'\033[1;32m-')+'\033[1;35m=\n\033[m'
titulo = '\033[1;31m       CALCULADORA DE PRODUTO\033[m\n'

#Apresentação do titulo do Programa:

print (line)
print (titulo.center(60))
print (line)
print ('Insira o preço do produto e seu método de pagamento:'.center(60))
print ('')
print (line)

#Solicitando valores:

preço = float(input('Qual o valor do produto?:'))
print ('')
print (line)

#Tabela de métodos
print('[1] PIX\n[2]A VISTA NO CRÉDITO\n[3]2X SEM JÚROS\n[4]3X OU MAIS')
print ('')
print (line)
condicao = int(input('--->'))

#Condicionamento

if condicao == 1:
    print(f'Seu produto de R${preço:.2f} sairá por R${(preço - (preço * 10/100)):.2f}. ')
    print('')
    print(line)
elif condicao == 2:
    print(f'Seu produto de R${preço:.2f} sairá por R${(preço - (preço * 5 / 100)):.2f}. ')
    print('')
    print(line)
elif condicao == 3:
    print(f'Seu produto de R${preço:.2f} será dividido em 2 parcelas de R${(preço / 2):.2f}. ')
    print('')
    print(line)
elif condicao == 4:
    parcelas = int(input('Em quantas parcelas pretende pagar?'))
    prod = preço + (preço * 20 / 100)
    print('')
    print(line)
    print(f'Seu produto de R${preço:.2f} será dividido em {parcelas} parcelas de R${(prod / parcelas):.2f}. ')
    print('')
    print(line)
else:
    print('Opção invalida, tente novamente.')
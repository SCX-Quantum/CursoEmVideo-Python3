print(14*'*~~'+'*')
print('DOBRO, TRIPLO E RAIZ QUADRADA?')
print(14*'*~~'+'*')
num = int(input('Digite um número para eu trabalhar:'))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('De acordo com minhas analises o resultado é o seguinte:\n'
      'DOBRO  : {}\n'
      'TRIPLO : {}\n'
      'RAIZ²  : {:.2f}\n'.format(dobro, triplo, raiz))
print(14*'*~~'+'*')
print('Satisfeito com o resultado?')
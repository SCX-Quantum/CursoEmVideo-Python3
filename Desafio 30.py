print(40*'=')
print('PAR OU IMPAR')
print(40*'=')
print('')
num = int(input('Digite um número qualquer:'))
print('')
if num == 0:
    print('Zero não é par nem impar.')
else:
    obj = num % 2
    if obj == 0:
        print('Este número é PAR')
    else:
        print('Esse número é IMPAR')
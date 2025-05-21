from random import randint

print(40*'=')
print('ADIVINHE MEU NUMERO')
print(40*'=')
print('')

num = randint(1, 10)

num_p = int(input('Pensei em um número entre 1 e 10, Adivinhe-o:'))
print('')
print(40*'=')
print('')
if num == num_p:
    print('Você acertou!!! INCRÍVEL.')
else:
    print('Você errou terrívelmente.')
print('')
print(40*'=')

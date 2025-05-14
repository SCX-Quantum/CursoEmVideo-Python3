from random import sample

print(40*'=')
print('         0DEFINIDOR DE SEQUENCIAS')
print(40*'=')
print('')
print('Digite o nome dos participantes:')
print('')
n1 = str(input('1º:'))
n2 = str(input('2º:'))
n3 = str(input('3º:'))
n4 = str(input('4º:'))
n5 = str(input('5º:'))
print('')
print('A ordem ficou a seguinte:')
print('')
ordem = sample([n1, n2, n3, n4, n5], 5)
print(f'1º: {ordem[0]}\n'
      f'2º: {ordem[1]}\n'
      f'3º: {ordem[2]}\n'
      f'4º: {ordem[3]}\n'
      f'5º: {ordem[4]}')

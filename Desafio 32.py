print(40*'=')
print('ANOS BISSEXTOS')
print(40*'=')
print('')
ano = int(input('Digite um ano válido:'))
print('')
if ano %4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} É Bissexto')
else:
    print(f'O ano de {ano} NÃO É Bissexto')
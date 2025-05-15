print(40*'=')
print('         ANALISADOR DE STRINGS')
print(40*'=')
print('')
nome = str(input('Escreva o seu nome completo:'))

print('')
print(f'Em letras minúsculas: {nome.lower()}\n'
      f'Em letras maiúsculas: {nome.upper()}\n'
      f'Possui um total de {(len(nome) - nome.count(' '))} letras, sem espaços.\n'
      f'E o primeiro nome possui {len(nome.split()[0])} letras.')
print('')
print(40*'=')
print('             VOLTE SEMPRE')
print(40*'=')
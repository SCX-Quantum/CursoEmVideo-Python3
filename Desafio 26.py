print(30*'=')
print('Analisador de letras A')
print(30*'=')
print('')
frase = str(input('Digite uma frase:')).strip().lower()
print(f'''A letra 'A' aparece {frase.count('a')} vezes
A primeira vez que ela aparece foi no {frase.find('a')+1}º caractere.
E sua última aparição no {frase.rfind('a')+1}º caractere.''')

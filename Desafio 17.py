from math import hypot

print(30*'=')
print('     HIPOTENUSA CALCULATOR')
print(30*'=')
print('')
cat1 = float(input('Qual o valor do cateto oposto?'))
cat2 = float(input('Qual o valor do cateto adjacente?'))
print('')
print('O valor da Hipotenusa é:')
print(30*'=')
print(f'            {hypot(cat1, cat2):.2f}')
print(30*'=')
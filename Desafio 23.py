print(40*'=')
print('         ANALISADOR DE NÚMEROS')
print(40*'=')
print('')
num = int(input('Digite um número entre 0 e 9999 : '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"""Este número apresentado possiu:
{u} Unidades.
{d} Dezenas.
{c} Centenas.
{m} Milhares.""")

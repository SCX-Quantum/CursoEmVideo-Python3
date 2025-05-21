print(40*'=')
print('TRIP CALCULATOR')
print(40*'=')
print('')
x = int(input('Quantos KM terá a sua viajem?'))
if x <= 200:
    pas = x * 0.5
else:
    pas = x * 0.4
print('')
print(f'O preço da sua passagem será de R${pas:.2f}')
print('')
print(25*'+-')
print('   Conversor Universal de Metros em Centímetros')
print(25*'+-')
print('')
metros = float(input('Digite aqui a quantia em METROS que deseja converter:'))
centimetros = metros * 100
milimetros = metros * 1000
print('{} Metros é equivalente á {:.0f} Centímetros e {:.0f} Milímetros'.format(metros, centimetros, milimetros))
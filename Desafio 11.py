print(30*'#')
print('      IA PARA PINTORES')
print(30*'#')
print('')
alt = float(input('Qual a altura da parede em metros?'))
comp = float(input('E qual seria o comprimento? '))
area = alt * comp
tinta = area // 2
total = tinta + (tinta * 15 / 100)
print('')
print('Para pintar uma parede de {:.2f}m², você precisará de {}L de tinta.'.format(area, total))
print('Já calculamos com 15% adicional para possiveis imprevistos. ')
print('')
print('Use tintas CORAL!')
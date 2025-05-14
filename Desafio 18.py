from math import radians, sin, cos, tan

print(40*'=')
print('              SEN COS TAN')
print(40*'=')
print('')
ang = float(input('Digite o angulo a ser analisado:'))
rad = radians(ang)
print('')
print(f'Valor analisado com sucesso!\n\nSEN : {sin(rad):.3f}\nCOS : {cos(rad):.3f}\nTAN : {tan(rad):.3f}')
print('')
print(40*'=')

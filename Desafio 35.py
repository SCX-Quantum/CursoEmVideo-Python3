print(40*'=')
print('TRIANGLE ANALISER')
print(40*'=')
print('')
num1 = int(input('Digite o primeiro segmento:'))
num2 = int(input('Digite o  segundo segmento:'))
num3 = int(input('Digite o terceiro segmento:'))
if num1 < num2 + num3 and num2 < num1 + num2 and num3 < num1 + num2:
    print('Esses segmentos de reta PODEM formar um triangulo')
else:
    print('Esses segmentos de reta NÃO PODEM formar um triangulo')
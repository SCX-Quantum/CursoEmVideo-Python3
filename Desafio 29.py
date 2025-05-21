

print(40*'=')
print('REGISTRADORA DE MULTAS')
print(40*'=')
print('')
vel = int(input('Qual a velocidade registrada?'))
print('')
if vel <= 80:
    print('Você está abaixo do limite de velocidade. Parabéns')
elif vel > 80:
    print('VELOCIDADE ACIMA DO PERMITIDO!')
    print(15*'=')
    print('MULTA REGISTRADA')
    print(15*'=')
    multa = (vel - 80) * 7
    print(f'O Valor a pagar da multa é de R${multa:.0f},00')
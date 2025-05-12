print(30*'=')
print('    PROMOTION CALCULATOR')
print(30*'=')
print('')
nome = str(input('Qual o nome do funcionário?'))
salario_atual = float(input('Qual o salário atual de {}?'.format(nome)))
porcent_aumento = float(input('Qual seria a porcentagem de aumento?'))
valor_aumento = salario_atual * porcent_aumento / 100
salario_final = salario_atual + valor_aumento
print('')
print('O novo salário de {}, passará a ser de R${:.2f} para R${:.2f} nesse novo cargo.'.format(nome, salario_atual, salario_final))
print('Um aumento de R${:.2f}. PARABÉNS {}'.format(valor_aumento, nome))
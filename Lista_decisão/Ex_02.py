# 2) Faça um programa para ler a temperatura de uma pessoa e exibir a mensagem "ESTÁ COM FEBRE" ou "ESTÁ NORMAL". Considere o valor base como 36.5:

temp = float(input('Informe sua temperatura: '))

if temp < 36.5:
	print('ESTÁ COM FEBRE')
else:
	print('ESTÁ NORMAL')

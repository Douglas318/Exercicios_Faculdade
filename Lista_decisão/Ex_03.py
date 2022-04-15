# 3) Faça um programa para ler dois valores e imprimir “EM ORDEM” caso o primeiro seja menor que o segundo e “FORA DE ORDEM” no caso contrário.

primeiro_valor = float(input('Informe o primeiro valor: '))

segundo_valor = float(input('Informe o segundo valor: '))

if primeiro_valor > segundo_valor:
	print('FORA DE ORDEM')
elif segundo_valor > primeiro_valor:
	print('EM ORDEM')

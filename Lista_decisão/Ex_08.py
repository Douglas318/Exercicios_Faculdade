# 8) Escreva um programa que leia 3 números inteiros e mostre o maior deles


num1 = int(input('informe o primeiro numero: '))

num2 = int(input('informe o segundo numero: '))

num3 = int(input('informe o terceiro numero: '))

if num1 > num2 and num1 > num3:
	print('O maior deles é o {}.'.format(num1))

if num2 > num1 and num2 > num3:
	print('O maior deles é o {}'.format(num2))

if num3 > num1 and num3 > num2:
	print('O maior deles é o {}'.format(num3))

#10) Uma empresa concederá um aumento de salário aos funcionários que possuirem mais de 4 anos de serviço, mais
#de 3 dependentes e salário atual abaixo de R$500,00. Faça um programa que leia estes dados de um funcionário e
#imprima uma mensagem dizendo se o funcionário tem direito ao aumento ou não. Caso ele tenha este direito, calcule o 
#novo salário com 40% de aumento. Mostre o salário antigo, o novo salário e a diferença.

tempo_servico = float(input('Informe seu tempo de serviço: '))
dependentes = int(input('Informe a quantidade de dependentes: '))
salario = float(input('Informe o seu salario: '))

novo_salario = salario +(salario*40)/100


if tempo_servico >= 4 and dependentes >= 3 and salario <= 500:
	print('Você tem direito a um aumento de 40%')
	print('Seu salário era {} e seu novo salário passará a ser:{}'.format(salario,novo_salario))
else:
	print('Você não tem direito a este beneficio')

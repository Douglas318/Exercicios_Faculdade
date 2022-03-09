''' Os preços das mercadorias apresentam descontos diferenciados pela forma de pagamento.
Escreva um programa para ler o tipo de pagamento e o preço da mercadoria e imprimir o
resultado com desconto de acordo com a tabela abaixo:
------------------------------------------------------
Forma de pagamento   código    percentual
Cartão de crédito      5         -10%
À vista           outro valor    -20% '''

codigo = int(input('informe a forma de pagamento: '))
mercadoria = float(input('informe o preço da mercadoria: '))
desconto_cartao = mercadoria - (mercadoria*10)/100
desconto_dinheiro = mercadoria - (mercadoria*20)/100

if codigo == 5:
	print('Você tem direito a 10% de desconto')
	print('O valor do produto com desconto será {}'.format(desconto_cartao))
elif codigo == 10:
	print('Você tem direito a 20% de desconto')
	print('O valor do produto com desconto será {}'.format(desconto_dinheiro))

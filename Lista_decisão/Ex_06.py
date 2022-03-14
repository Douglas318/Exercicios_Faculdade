 #Os preços das mercadorias apresentam descontos diferenciados pela forma de pagamento.
#Escreva um programa para ler o tipo de pagamento e o preço da mercadoria e imprimir o
#resultado com desconto de acordo com a tabela abaixo:
#Forma de pagamento      código        percentual
#Cartão de crédito         5              -10%
#À vista                   6             - 20%
#3 vezes                   7              -5 %
  
  
print('Cartão: Código 5 - ', 'Dinheiro: Código 6 - ', 'Cartão 3x: Código 7')
codigo = int(input('informe a forma de pagamento:'))
mercadoria = float(input('informe o preço da mercadoria:'))
desconto_cartao = mercadoria - (mercadoria*10)/100
desconto_dinheiro = mercadoria - (mercadoria*20)/100
desconto_cartao_3_vezes = mercadoria - (mercadoria*5)/100
 
if codigo == 5:
	print('Você tem direito a 10% de desconto')
	print('O valor do produto com desconto será {}'.format(desconto_cartao))
elif codigo == 6:
	print('Você tem direito a 20% de desconto')
	print('O valor do produto com desconto será {}'.format(desconto_dinheiro))
if codigo == 7:
	print('Você tem direito a 5% de desconto')
	print('O valor do produto com desconto será {}'.format(desconto_cartao_3_vezes))
  

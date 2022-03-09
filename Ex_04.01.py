""" Você foi escolhido para desenvolver três programas para uma loja:
Programa 1: Os preços das mercadorias expostas apresentam descontos diferenciados. Escreva um
programa para ler o valor da compra e o percentual do desconto. Imprimir a seguinte mensagem:
"PARA xx.xx % DE DESCONTO O VALOR É R$ yy.yy”"""


valor_da_compra = int(input('informe o valor da compra: '))
desconto_10 = valor_da_compra - (valor_da_compra*10)/100
desconto_20 =valor_da_compra - (valor_da_compra*20)/100

if valor_da_compra <= 50:
	print('você recebeu 10% de desconto o novo valor é {}'.format(desconto_10))
	print('Para receber 20% de desconto o valor é acima de R$50')
elif valor_da_compra > 50 :
	print('Você recebeu 20% de desconto o novo valor é {}'.format(desconto_20))



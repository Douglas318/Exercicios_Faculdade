km = float(input('informe a distancia percorrida em km: '))
hr = float(input('informe o tempo de viagem em horas: '))

velocidade_media = km/hr

print(velocidade_media, 'Km/hr')

if velocidade_media > 80:
	print(' Velocidade média superior a 80km/h')
else:
	print('velocidade média abaixo de 80km/h')

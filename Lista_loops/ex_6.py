peso = int(input('Informe o peso: '))
peso_inválido = 0
while peso != 0:
    peso = int(input('Informe o peso novamente: '))
    if peso < 100 or peso > 900:
        peso_inválido += 1
while peso == 0:
    print('Encerrando, {} pesos inválidos.'.format(peso_inválido))
    break
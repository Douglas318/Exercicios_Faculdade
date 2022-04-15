nota = float(input('Informe o valor da nota: '))

contador = 0

while nota != 0 and contador <= 8:
    
    nota = float(input('Informe o valor da nota: '))
    
    contador += 1

if nota == 0:
    
    print('Não aprovado')

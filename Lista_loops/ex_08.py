notas = [ ]
nota = 1
while nota != 0:
     nota =(float(input(f"Digite o valor da nota:")))
     notas.append(nota)
soma = 0
for nota in notas:
    soma = soma + nota
notas=notas[:-1]
media = soma / len(notas)
print(f"O valor da média é {round(media,2)}")





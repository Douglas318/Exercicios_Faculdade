notas = []
nota = 1
while nota != 0:
    nota = float(input('Continue informando as notas dos alunos: '))
    notas.append(nota)
soma = 0
for nota in notas:
    soma = soma + nota
nota = notas [:-1]
media = soma / len(notas)

print('A média da turma é {}'.format(notas))
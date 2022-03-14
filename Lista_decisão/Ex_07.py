#Faça um programa que leia três valores representando as notas de um aluno. Informe a situação do aluno: Aprovado, Reprovado ou Prova Final. Considere:
#APROVADO - nota maior ou igual a 6.
#PROVA FINAL - nota entre 4 e 5.9
#REPROVADO – nota menor que 4

primeira_nota = float(input('Informe a primeira nota: '))
segunda_nota = float(input('Informe a segunda nota: '))
terceira_nota =float(input('Informe a terceira nota: '))

media = (primeira_nota + segunda_nota + terceira_nota)/3

if media >= 60:
	print('APROVADO')
elif media >= 40 or media >= 59:
	print('PROVA FINAL')
if media < 40:
	print('REPROVADO')


# Autor: Gabriel Moreira Silva
# Submissão: 16/12/2019 03:15:57
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1073

N = int(input())
quadrado = []
conta= 0
if N > 5 or N < 2000:
	while conta != N:
		conta = conta+2
		quadrado = conta**2
		print(conta,'^',2,' = ',quadrado,sep='')
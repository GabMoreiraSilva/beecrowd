# Autor: Gabriel Moreira Silva
# Submissão: 23/11/2022 15:27
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1113

entradas = []
while(True):
	entrada = input().split(' ')
	if(entrada[0] == entrada[1]):
		break
	entradas.append([int(entrada[0]),int(entrada[1])])

for n in range(len(entradas)):
	if (entradas[n][0] > entradas[n][1]):
		print('Decrescente')
	else:
		print('Crescente')
# Autor: Gabriel Moreira Silva
# Submissão: 16/12/2019 03:33:31 
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1115

cor = []
while (cor != 0):
	cor = (input())
	cor= cor.split(' ')
	if int(cor[0]) == 0 or int(cor[1] == 0):
		break
	if int(cor[0]) > 0 and int(cor[1]) > 0:
		print('primeiro')
		continue
	if int(cor[0]) < 0 and int(cor[1]) > 0:
		print('segundo')
		continue
	if int(cor[0]) < 0 and int(cor[1]) < 0:
		print('terceiro')
		continue
	if int(cor[0]) > 0 and int(cor[1]) < 0:
		print('quarto')
		continue
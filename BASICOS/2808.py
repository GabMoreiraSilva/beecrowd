# Autor: Gabriel Moreira Silva
# Submissão: 17/12/2019 19:10:56
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/2808 

lista = input()
linha =[]
coluna =[]
check = [1,2,3,4,5,6,7,8]
linha_c = {'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8}
coluna_c = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8}
for x in lista:
    if x.isdigit():
        linha.append(linha_c[x])
    elif x == ' ':
        continue
    else:
        coluna.append(coluna_c[x])
if linha[0] in check and linha[1] in check and coluna[0] in check and coluna[1] in check:
    coluna = abs(coluna[0] - coluna[1])
    linha = abs(linha[0] - linha[1])
    if(coluna == 1 and linha == 2) or (coluna == 2 and linha == 1):
        print('VALIDO')
    else:
       print('INVALIDO')
else:
    print('INVALIDO')

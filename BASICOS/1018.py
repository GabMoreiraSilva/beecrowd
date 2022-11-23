# Autor: Gabriel Moreira Silva
# Submissão: 17/12/2019 23:17
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1018

x = int(input())
entrada = x
nota = [100,50,20,10,5,2,1]
valor = []

for i in range(7):
    if x >= nota[i]:
       valor.append(int(x/nota[i]))
       x = x-(nota[i]*valor[i])
    else:
        valor.append(0)

print(entrada,end='\n')
for i in range(7):
      print(valor[i], ' nota(s) de R$ ',(nota[i]),',00', sep='', end='\n')
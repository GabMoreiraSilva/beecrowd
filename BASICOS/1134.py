# Autor: Gabriel Moreira Silva
# Submissão: 16/12/2019 14:48
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1134

x = 0
lista = []

while (x!= 4):
    x = int(input())
    if x < 0 or x > 5:
        x = 0
    x = int(x)
    lista.append(x)
    if x == 4:
        break

print('MUITO OBRIGADO')
print('Alcool:', lista.count(1))
print('Gasolina:',lista.count(2))
print('Diesel:',lista.count(3))

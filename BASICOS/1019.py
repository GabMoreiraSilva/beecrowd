# Autor: Gabriel Moreira Silva
# Submissão: 15/12/2019 17:52:10
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/1019

N = int(input())
s = m = h = 0

s = int(N % 60) 
m = int((N / 60) % 60)
h = int((N / 60) / 60)

print(h, m, s, sep=':')
# Autor: Gabriel Moreira Silva
# Submissão: 19/12/2019 01:24:18
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/2663

while True:
  try:
    n = 0
    k = 0
    verificador = 0
    contador = []
    valores = []
    passou = []
    repescagem = []

    while verificador != 1:
        n = int(input())
        if n <= 1000:
            verificador = 1 
    verificador = 0    
    while verificador != 1:
        k = int(input())
        if k <= n:
            verificador = 1    
    for i in range(n):
        valor = int(input())
        valores.append(valor)
    valores = sorted(valores, reverse = True)
    for i in valores:
        if len(passou) != k:
            passou.append(i)
        else:
            contador.append(i)
        
    for i in contador:
        if i == min(passou):
            repescagem.append(i)
        else:
            continue

    print((len(passou)+len(repescagem)))

  except EOFError:
    break
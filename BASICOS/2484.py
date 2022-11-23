# Autor: Gabriel Moreira Silva
# Submissão: 18/12/2019 17:10
# Link: https://www.beecrowd.com.br/judge/pt/problems/view/2484

while True:
  try:
    x = input()
    s = ' '
    y = 0
    h = []
    for i in x:
        h.append(i)

    x = ' '.join(h)
    c = len(x)

    for i in x:
        if i != ' ':
            print(s*y, end='')
            print(x[:c])
            y += 1
            c = c-1
        else:
            c = c-1
        continue
    print()
  except EOFError:
    break
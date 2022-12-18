import random 

histograma = [0]*101

for i in range(len(histograma)):
    nota = int(random.random()*101)
    histograma[nota] = histograma[nota] + 1

for i in range(len(histograma)):
    print(f'Nota {i/10:.1f}: {histograma[i]}')

for i in range(len(histograma)):
    bar = '='*histograma[i]
    print(f'Nota {i/10:.1f}: {bar}', end='*\n')
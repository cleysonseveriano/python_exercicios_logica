M = [None]*12
for i in range(len(M)):
    M[i] = [None]*12
T = input()
for i in range(len(M)): 
    for j in range(len(M[i])):
        M[i][j] = float(input())
Soma = 0
Média = 0
stop = len(M) - 1
for i in range(len(M)): 
    if i == 11:
        break
    for j in range(stop):
        Soma = Soma + M[i][j]
    stop = stop - 1
if T=='S':
    print(f'{Soma:.1f}')
elif T=='M':
    Média = Soma/66
    print(f'{Média:.1f}')
M = [None]*12
for i in range(len(M)):
    M[i] = [None]*12
T = input()
for i in range(len(M)): 
    for j in range(len(M[i])):
        M[i][j] = float(input())
Soma = 0
Média = 0
start = 1
for i in range(len(M)): 
    for j in range(start, len(M[i])):
        Soma = Soma + M[j][i]
    start+=1
if T=='S':
    print(f'{Soma:.1f}')
elif T=='M':
    Média = Soma/66
    print(f'{Média:.1f}')
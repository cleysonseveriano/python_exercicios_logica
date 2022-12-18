M = [None]*12
for i in range(len(M)):
    M[i] = [None]*12
C = int(input())
T = input()
for i in range(len(M)): 
    for j in range(len(M[i])):
        M[i][j] = float(input())
Soma = 0
Média = 0
for j in range(len(M)):
    Soma = Soma + M[j][C]
if T=='S':
    print(f'{Soma:.1f}')
elif T=='M':
    Média = Soma/len(M)
    print(f'{Média:.1f}')
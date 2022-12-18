M = [None]*12
for i in range(len(M)):
    M[i] = [None]*12
L = int(input())
T = input()
for i in range(len(M)): 
    for j in range(len(M[i])):
        M[i][j] = int(float())
        
Soma = 0
Média = 0
for j in range(len(M[L])):
    Soma = Soma + M[L][j]
if T=='S':
    print(f'{Soma:.1f}')
elif T=='M':
    Média = Soma/len(M[L])
    print(f'{Média:.1f}')
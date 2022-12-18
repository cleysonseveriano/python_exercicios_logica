M = [None]*12
for i in range(len(M)):
    M[i] = [None]*12
T = input()
for i in range(len(M)): 
    for j in range(len(M[i])):
        M[i][j] = float(input())
Soma = 0
Média = 0
cont = 0
for i in range(5):
    for j in range(1+i, len(M)-1-i):
        Soma += M[i][j]
        cont+=1
if T=='S':
    print(f'{Soma:.1f}')
elif T=='M':
    Média = Soma/cont
    print(f'{Média:.1f}')
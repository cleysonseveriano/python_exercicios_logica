M = [None]*12
for i in range(len(M)):
    M[i] = [None]*12
O = input()
for i in range(len(M)): 
    for j in range(len(M[i])):
        M[i][j] = float(input())
Soma = 0
Média = 0
inf = 5
sup = 7
cont = 0
for i in range(7,12):
    for j in range(inf,sup):
        Soma += M[i][j]
        cont+=1
    inf-=1
    sup+=1
if O=='S':
    print(f'{Soma:.1f}')
elif O=='M':
    Média = Soma/cont
    print(f'{Média:.1f}')
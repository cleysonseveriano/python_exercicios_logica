M=1
N=1
while M!=0 and N!=0:
    M, N = input().split(' ')
    M = int(M)
    N = int(N)
    if (M==0 or N==0) or (M<0 or N<0):
        break
    else:
        if M > N:
            maior = M 
            menor = N
        elif N > M:
            menor = M
            maior = N
        soma = 0
        for i in range(menor, maior+1):
            print(i, end=' ')
            soma = soma + i
        print(f'Sum={soma}')
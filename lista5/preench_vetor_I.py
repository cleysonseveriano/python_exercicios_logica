X = int(input())
N = [None]*10
for i in range(len(N)):
    if i==0:
        N[i] = X
    else:
        N[i] = X * (2**i)
    print(f'N[{i}] = {N[i]}')
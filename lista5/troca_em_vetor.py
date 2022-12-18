N = [None]*10
for i in range(len(N)-1, -1, -1):
    N[i] = int(int(input()))
for i in range(len(N)):
    print(f'N[{i}] = {N[i]}')
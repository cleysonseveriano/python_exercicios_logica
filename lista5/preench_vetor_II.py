T = int(input())
N = [None]*1000
j = 0
for i in range(1000):
    if j == T:
        j = 0
    N[i] = j
    print(f'N[{i}] = {N[i]}')
    j = j + 1
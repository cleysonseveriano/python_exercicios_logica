A =[None]*10
r = []
for i in range(len(A)):
    A[i] = int(input())
    if A[i] <= 10:
        r.append(i)
for i in r:
    print(f'A[{i}] = {A[i]}')
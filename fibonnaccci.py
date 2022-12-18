N = int(input())
t1 = 0
t2 = 1
while N>0:
    if N!=1:
        print(t1, end=' ')
    else:
        print(t1)
    p = t1 + t2
    t1 = t2
    t2 = p
    N = N - 1
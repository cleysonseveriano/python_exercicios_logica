N = int(input())
while N > 0:
    T = int(input())
    x = T
    t1 = 0
    t2 = 1
    while T>0:
        p = t1 + t2
        t1 = t2
        t2 = p
        T = T - 1
    print(f'Fib({x}) = {t1}')
    N-=1
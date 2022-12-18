N = int(input())
while N > 0:
    X, Y = input().split(' ')
    X = int(X)
    Y = int(Y)
    if Y == 0:
        print('divisao impossivel')
    else:
        divisao = X/Y
        print(f'{divisao:.1f}')
    N-=1
N = int(input())
i = 0
j = 0
while N > 0:
    i = i + 1
    while j < (4*i):
        j = j + 1
        if j%4==0:
            print('PUM')
        else:
            print(j, end=' ')
    N = N - 1
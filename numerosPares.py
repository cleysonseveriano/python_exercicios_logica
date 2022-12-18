N = int(input())
i = 0
if N>5 and N<2000:
    while i<N:
        i+=1
        if i%2==0:
            print(f'{i}^2 = {i**2}')
N = int(input())
i = 0
while i<N:
    n1,n2,n3 = input().split(' ')
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    media = (n1*2+n2*3+n3*5)/10
    print(round(media,1))
    i += 1
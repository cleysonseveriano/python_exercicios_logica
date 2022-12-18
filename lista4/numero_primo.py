N = int(input())
while N > 0:
    X = int(input())
    somatorio = 0
    for i in range(1,X+1):
        if X%i==0:
            somatorio+=1
    if somatorio==2:
        print(f'{X} eh primo')
    else: 
        print(f'{X} nao eh primo')
    N-=1
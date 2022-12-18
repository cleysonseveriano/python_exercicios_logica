N = int(input())
i = 0
while i<=N:
    if i==0:
        pass
    else:
        X = int(input())
        if X==0: 
            print('NULL')
        else:
            if X%2==0:
                print('EVEN',end=' ')
            if X%2!=0:
                print('ODD',end=' ')
            if X>0:
                print('POSITIVE')
            if X<0:
                print('NEGATIVE')
    i+=1
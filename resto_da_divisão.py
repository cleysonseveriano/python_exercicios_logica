X = int(input())
Y = int(input())
if X > Y:
    A = Y
    B = X
if Y > X:
    A = X
    B = Y
while A < B:
    if A%5==2 or A%5==3:
        print(A)
    A = A + 1
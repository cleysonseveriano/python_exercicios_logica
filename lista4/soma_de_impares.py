X =int(input())
Y = int(input())
if X > Y:
    A = Y
    B = X
if Y > X:
    A = X
    B = Y
if X==Y:
    A = X
    B = Y
s_impar = 0
while (B-1) > A:
    A = A + 1
    if A%2!=0:
        s_impar = s_impar + A
print(f'{s_impar}')
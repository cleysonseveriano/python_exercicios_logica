X = int(input())
Y = int(input())
somatorio = 0
if Y > X:
    A = X
    B = Y
elif X > Y:
    B = X
    A = Y
for i in range(A, B+1):
    if i%13!=0:
        somatorio = somatorio + i
print(somatorio)
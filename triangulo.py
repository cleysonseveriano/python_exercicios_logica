A,B,C = input().split(' ')
A = float(A)
B = float(B)
C = float(C)
if A >= (B+C) or B >= (A+C) or C >= (A+B):
    Area=((A+B)*C)/2
    print(f'Area = {Area:.1f}')
else:
    perimetro=A+B+C
    print(f'Perimetro = {perimetro:.1f}')

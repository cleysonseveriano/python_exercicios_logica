A,B,C=input().split(' ')
A=float(A)
B=float(B)
C=float(C)
if B>=A and B>=C:
    A=A+B
    B=A-B
    A=A-B
elif C>=A and C>=B:
    A=A+C
    C=A-C
    A=A-C
if A>=(B+C) or C>=(B+A) or B>=(A+C):
    print('NAO FORMA TRIANGULO')
else:
    if (A**2)==((B**2)+(C**2)):
        print('TRIANGULO RETANGULO')
    if (A**2)>((B**2)+(C**2)):
        print('TRIANGULO OBTUSANGULO')
    if (A**2)<((B**2)+(C**2)):
        print('TRIANGULO ACUTANGULO')
    if A==B and B==C:
        print('TRIANGULO EQUILATERO')
    if (A==B or B==C or C==A)and(A!=B or B!=C or C!=A):
        print('TRIANGULO ISOSCELES')

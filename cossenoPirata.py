import math
def potencia(X,Y):
    pot = 1
    for i in range(Y):
        pot = pot * X
    return pot

def fatorial(N):
    fat = 1
    while N > 1:
        fat = fat * N
        N = N - 1
    return fat

def deg2rad(a):
    return (a*math.pi/180)+math.pi/2

X = float(input('Digite o valor em graus: '))
N = int(input('Digite a quantidade de termos: '))
X = deg2rad(X)
S = 0
t = X
i = 1
while(N>0):
    S = S + t
    i = i + 2
    t = t*((X*X)/(i*(i-1)))*-1
    N = N - 1
print(f"Cosseno calculado: {S}")
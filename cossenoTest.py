import math

def cosseno():
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
        return a*math.pi/180

    X = float(input('Digite o valor em graus: '))
    N = int(input('Digite a quantidade de termos: '))
    X = deg2rad(X)

    S = 0
    t = 1
    i = 0

    while(N>0):
        S = S + t
        i = i + 2
        t = (t*((X*X)/(fatorial()))*-1)
        N = N - 1

    print(f"Cosseno calculado: {S}")

cosseno()
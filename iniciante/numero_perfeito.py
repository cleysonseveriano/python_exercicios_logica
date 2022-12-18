N = int(input())
while N > 0:
    valor = int(input())
    soma = 0
    for i in range(1,valor):
        if valor%i==0:
            soma = soma + i
    if soma==valor:
        print(f'{valor} eh perfeito')
    else:
        print(f'{valor} nao eh perfeito')
    N = N - 1
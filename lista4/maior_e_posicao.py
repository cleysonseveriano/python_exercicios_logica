i = 0
while i < 100:
    i = i + 1
    n = int(input())
    if i == 1:
        maior = n
        menor = n
    if n < menor:
        menor = n
    if n > maior:
        maior = n
        entrada = i
print(maior)
print(entrada)
        
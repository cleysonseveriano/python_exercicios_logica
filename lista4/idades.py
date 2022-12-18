somatorio = 0
i = 0
valor = 0
while valor >= 0:
    valor = int(input())
    if valor >=0:
        somatorio+=valor
        i+=1
media = somatorio/i
print(f'{media:.2f}')
somatorio = 0
for i in range(5):
    valores = float(input())
    if valores%2==0:
        somatorio+=1
print(f'{somatorio} valores pares')
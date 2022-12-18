somatorio = 0
for i in range(6):
    valores = float(input())
    if valores > 0:
        somatorio+=1
print(f'{somatorio} valores positivos')
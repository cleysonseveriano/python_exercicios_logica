somatorio = 0
total = 0
for i in range(6):
    valores = float(input())
    if valores > 0:
        somatorio+=1
        total+=valores

valores = total/somatorio
print(f'{somatorio} valores positivos')
print(f'{valores:.1f}')
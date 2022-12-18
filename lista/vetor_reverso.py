V = [7,2,-9,32,61,79,-10]
print(f'Vetor original: {V}')
print('Imprimindo o vetor reverso')
i = len(V)-1
while i > -1:
    print(V[i], end=' ')
    i-=1
print()
for i in range(len(V)-1, -1, -1):
    print(V[i], end=' ')
print()

Vrev = [None]*len(V)
#Atribuição do reverso do vetor V a um novo vetor
for i in range(len(Vrev)):
    print(f'Vrev[{i}]   V[{len(V)-1-i}]')
    Vrev[i] = V[len(V) -1 -i]
print(Vrev)
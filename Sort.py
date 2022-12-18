lista = []
n1, n2, n3 = input().split(' ')
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
lista.append(n1)
lista.append(n2)
lista.append(n3)
if n3 in lista:
    lista.sort()
    for i in lista:
        print(i)
for i in lista:
    lista.remove(i)
lista.append(n1)
lista.append(n2)
lista.append(n3)
print()
for i in lista:
    print(i)

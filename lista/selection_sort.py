def selection_sort(V):
    for i in range(len(V)):
        menor = V[i]
        pos = i
        j = i + 1
        while j < len(V):
            if V[j] < menor:
                menor = V[j]
                pos = j
            j+=1
        V[pos] = V[i]
        V[i] = menor
    print(V)

vetor = [0,32,6]
selection_sort(vetor)
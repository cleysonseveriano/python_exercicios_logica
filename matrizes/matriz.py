import random 

L = 5
C = 5

M =[None]*L
for i in range(len(M)):
    M[i] = [None]*C
#CADASTRAR A MATRIZ
for i in range(len(M)):
    for j in range(len(M[i])):
        M[i][j] = int(random.random()*10)

#IMPRIMIR
print('Matriz original')
for i in range(len(M)):
    for j in range(len(M[i])):
        print(M[i][j], end='  ')
    print()

print('Matriz transposta')
for i in range(len(M)):
    for j in range(len(M[i])):
        print(M[j][i], end='  ')
    print()

print("Diagonal Principal")
for i in range(len(M)):
    for j in range(len(M[i])):
        if i==j:
            print(M[i][j],end='  ')
        else:
            print(end='   ')
    print()

print('Diagonal Secundária')
for i in range(len(M)):
    for j in range(len(M[i])):
        if (i+j)==len(M)-1:
            print(M[i][j],end='  ')
        else:
            print(end='   ')
    print()

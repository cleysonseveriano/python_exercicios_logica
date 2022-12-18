s_pares = 0
s_impares = 0
s_positivo = 0
s_negativo = 0
for i in range(5):
    valores = int(input())
    if valores%2==0:
        s_pares+=1
    if valores%2!=0:
        s_impares+=1
    if valores > 0:
        s_positivo+=1
    if valores < 0:
        s_negativo+=1
print(f'{s_pares} valor(es) par(es)')
print(f'{s_impares} valor(es) impar(es)')
print(f'{s_positivo} valor(es) positivo(s)')
print(f'{s_negativo} valor(es) negativo(s)')
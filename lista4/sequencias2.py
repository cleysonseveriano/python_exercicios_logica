S = 0
j = 2
n = 0
for i in range (1,40,2):
    S = S + (i/(j**n))
    n+=1
print(f'{S:.2f}')
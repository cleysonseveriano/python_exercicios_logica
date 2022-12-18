N = int(input())
coelhos = 0
ratos = 0
sapos = 0
tot_cobaias = 0
for i in range(N):
    Quantia, especie = input().split(' ')
    Quantia = int(Quantia)
    if especie == 'C':
        coelhos = coelhos + Quantia
    elif especie == 'S':
        sapos = sapos + Quantia
    elif especie == 'R':
        ratos = ratos + Quantia
    tot_cobaias = tot_cobaias + Quantia
    
print(f'Total: {tot_cobaias} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {coelhos/tot_cobaias*100:.2f} %')
print(f'Percentual de ratos: {ratos/tot_cobaias*100:.2f} %')
print(f'Percentual de sapos: {sapos/tot_cobaias*100:.2f} %')
gols_i, gols_g = input().split(' ')
gols_g = int(gols_g)
gols_i = int(gols_i)
i = 0
resposta = 0
Gremio = 0
Inter = 0
Empate = 0
while resposta!=2:
    i = i + 1
    if gols_g > gols_i:
        Gremio+=1
    if gols_i > gols_g:
        Inter+=1
    if gols_g == gols_i:
        Empate+=1
    print('Novo grenal (1-sim 2-nao)')
    resposta = int(input())
    if resposta == 1:
        gols_i, gols_g = input().split(' ')
        gols_g = int(gols_g)
        gols_i = int(gols_i)
print(f'{i} grenais')
print(f'Inter:{Inter}')
print(f'Gremio:{Gremio}')
print(f'Empates:{Empate}')
if Inter > Gremio:
    print('Inter venceu mais')
if Gremio > Inter:
    print('Gremio venceu mais')
if Gremio == Inter or (Empate==i):
    print('Não houve vencedor')
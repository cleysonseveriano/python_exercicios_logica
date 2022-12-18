Hi,Hf = input().split(' ')
Hi = int(Hi)
Hf = int(Hf)
if Hi>=Hf:
    duracao = (Hf+24)-Hi
    print(f'O JOGO DUROU {duracao} HORA(S)')
else:
    duracao = Hf-Hi
    print(f'O JOGO DUROU {duracao} HORA(S)')

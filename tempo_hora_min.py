Hi,Mi,Hf,Mf=input().split(' ')
Hi=int(Hi)
Mi=int(Mi)
Hf=int(Hf)
Mf=int(Mf)
MTi = Mi+ (60*Hi)
MTf = Mf + (60*Hf)
if MTf>MTi:
    D = MTf-MTi
else:
    D = (24*60)-MTi+MTf
Dh = D//60
Dm = D%60
print(f'O JOGO DUROU {Dh} HORA(S) E {Dm} MINUTO(S)')

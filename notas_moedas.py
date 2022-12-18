valor=float(input())
if 0<=valor<=1000000:
    notas100=valor//100
    valor=valor%100
    notas50=valor//50
    valor=valor%50
    notas20=valor//20
    valor=valor%20
    notas10=valor//10
    valor=valor%10
    notas5=valor//5
    valor=valor%5
    notas2=valor//2
    valor=valor%2
    moedas100=valor//1
    valor=valor%1
    moedas50=valor//0.5
    valor=valor%0.5
    moedas25=valor//0.25
    valor=valor%0.25
    moedas10=valor//0.1
    valor=valor%0.1
    moedas5=valor//0.05
    valor=valor%0.05
    moedas1=valor//0.01
    print('NOTAS:')
    print(f'{notas100:.0f} nota(s) de R$ 100.00')
    print(f'{notas50:.0f} nota(s) de R$ 50.00')
    print(f'{notas20:.0f} nota(s) de R$ 20.00')
    print(f'{notas10:.0f} nota(s) de R$ 10.00')
    print(f'{notas5:.0f} nota(s) de R$ 5.00')
    print(f'{notas2:.0f} nota(s) de R$ 2.00')
    print('MOEDAS:')
    print(f'{moedas100:.0f} moeda(s) de R$ 1.00')
    print(f'{moedas50:.0f} moeda(s) de R$ 0.50')
    print(f'{moedas25:.0f} moeda(s) de R$ 0.25')
    print(f'{moedas10:.0f} moeda(s) de R$ 0.10')
    print(f'{moedas5:.0f} moeda(s) de R$ 0.05')
    print(f'{moedas1:.0f} moeda(s) de R$ 0.01') 
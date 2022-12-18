i = 0
total = 0
while i < 2:
    i+=1
    nota = float(input())
    if nota < 0 or nota > 10:
        print('nota invalida')
        i-=1
    else:
        total = total + nota
    if i == 2:
        print(f'media = {(total/2):.2f}')
        seg = float(input('novo calculo (1-sim 2-nao)'))
        while seg != 1 and seg != 2:
            seg = float(input('novo calculo (1-sim 2-nao)'))
        if seg == 1:
            i = 0
            total = 0
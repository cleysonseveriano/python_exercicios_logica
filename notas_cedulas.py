print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor  = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 100
totalCed = 0
while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        print(f'Total de {totalCed} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totalCed = 0
        if total == 0:
            break

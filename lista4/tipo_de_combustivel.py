combustivel = 0
Alcool = 0
Diesel = 0
Gasolina = 0
while combustivel != 4:
    combustivel = int(input())
    while combustivel < 1 and combustivel > 4:
        combustivel = int(input())
    if  combustivel == 1:
        Alcool+=1
    if combustivel == 2:
        Gasolina+=1
    if combustivel == 3:
        Diesel+=1
print('MUITO OBRIGADO')
print(f'Alcool: {Alcool}')
print(f'Gasolina: {Gasolina}')
print(f'Diesel: {Diesel}')
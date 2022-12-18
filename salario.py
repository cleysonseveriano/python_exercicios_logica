salario = float(input())
if salario >= 0 and salario <= 400:
    reajuste = salario*0.15
    new_salario = salario + reajuste
    print(f'Novo salario: {new_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 15%')
elif salario >= 400.01 and salario <= 800:
    reajuste = salario*0.12
    new_salario = salario + reajuste
    print(f'Novo salario: {new_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 12%')
elif salario >= 800.01 and salario <= 1200:
    reajuste = salario*0.1
    new_salario = salario + reajuste
    print(f'Novo salario: {new_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 10%')
elif salario >= 1200.01 and salario <= 2000:
    reajuste = salario*0.07
    new_salario = salario + reajuste
    print(f'Novo salario: {new_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 7%')
elif salario > 2000:
    reajuste = salario*0.04
    new_salario = salario + reajuste
    print(f'Novo salario: {new_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: 4%')

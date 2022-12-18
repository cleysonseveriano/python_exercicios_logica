N = int(input('Digite a quantidade de notas a serem digitadas: '))

while N <= 0:
    N = int(input('Valores inválidos, por favor digite novamente. (VALORES ENTRE 1 e 10): '))

cont=0
nota=0
maior=0
menor=0
somatorio=0
q1=0
q2=0
q3=0
q4=0
q5=0
q6=0
q7=0
q8=0
q9=0
q10=0

while cont < N:
    cont+=1
    while nota>=0 and nota<=10:
        nota = float(input(f'Digite a nota {cont}: '))
        if cont==1:
            maior=nota
            menor=nota
        elif cont>1:
            if menor>nota:
                menor=nota
            elif maior<nota:
                maior=nota
        somatorio += nota
        if nota>=0 and nota<1:
            q1+=1
        elif nota>=1 and nota<2:
            q2+=1
        elif nota>=2 and nota<3:
            q3+=1
        elif nota>=3 and nota<4:
            q4+=1
        elif nota>=4 and nota<5:
            q5+=1
        elif nota>=5 and nota<6:
            q6+=1
        elif nota>=6 and nota<7:
            q7+=1
        elif nota>=7 and nota<8:
            q8+=1
        elif nota>=8 and nota<9:
            q9+=1
        elif nota>=9 and nota<=10:
            q10+=1
        break

media=somatorio/cont
print('ITEM A')
print(f'O menor número é {menor} e o maior número é {maior}.')
print('ITEM B')
print(f'A média dos números digitados é {media:.2f}')
print('ITEM C')
print('HISTOGRAMA')
j = 0
for notas in [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]:
    print(f'Temos {notas} no intervalo [{j},{j+1}[')
    j+=1
codigo,qtnd=input().split(' ')
codigo = int(codigo)
qtnd=int(qtnd)
if codigo==1:
    preco = qtnd*4.00
    print(f'Total: R$ {preco:.2f}')
elif codigo==2:
    preco = qtnd*4.50
    print(f'Total: R$ {preco:.2f}')
elif codigo==3:
    preco = qtnd*5.00
    print(f'Total: R$ {preco:.2f}')
elif codigo==4:
    preco = qtnd*2.00
    print(f'Total: R$ {preco:.2f}')
elif codigo==5:
    preco = qtnd*1.50
    print(f'Total: R$ {preco:.2f}')
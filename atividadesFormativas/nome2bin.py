def my_name(Name):
    num = 0
    for i in Name:
        n = ord(i)
        if (n < 32 or n > 32) and (n < 65 or n > 90) and (n < 97 or n > 122):
            raise ValueError ('ERRO')
        num = n
    return num

def dec2bin(N):
    zeros_aux = 1
    bin_rev = 0
    controle = True
    while N > 0:
        r = N%2
        if controle==True:
            if r==0:
                zeros_aux = zeros_aux * 10
            else:
                controle = False
        bin_rev = bin_rev * 10 + r
        N = int(N/2)
    binario = 0
    while bin_rev > 0:
        r = bin_rev%10
        binario = binario * 10 + r
        bin_rev = int(bin_rev/10)
    print(f'0{binario*zeros_aux}', end=' ')

def converting():
    print('POR FAVOR, NÃO UTILIZE CARACTERES, NEM LETRAS ACENTUADAS')
    name = input('Digite seu nome: ')
    for i in name:
        dec2bin(my_name(i))

converting()
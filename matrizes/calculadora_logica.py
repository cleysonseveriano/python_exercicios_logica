lista = []
operacao = []
char = ''
print("-"*15, 'Calculadora lógica', "-"*15)
print('VARIÁVEIS [p] [q] [r]')
print('OPERAÇÕES [^] [v] [>] [<>]')
for i in range(10):
    char = input()
    if char != ('p'or'q'or'r'or'>'or'v'or'^'or'<>'):
        i=10
    else:
        operacao.append(char)

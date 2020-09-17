numero = int(input('Informe um numero para descobrir se é PAR ou IMPAR: '))
resultado = numero % 2
if resultado == 0:
    print('O numero {} é PAR'.format(numero))
else:
    print('O numero {} é IMPAR'.format(numero))

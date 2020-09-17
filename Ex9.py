def List(t1, t2):
    list = []
    while(t2 <= t1):
        print()
        nro = int(input(f'Informando número {t2} de {t1} : '))
        list.append(nro)
        t2 += 1
    return list

t1 = int(input('Deseja informar quantos números? : '))
t2 = 1
list = List(t2, t1)

for nro in list:
    print(f'O QUADRADO do número {nro} é {nro ** 2}')
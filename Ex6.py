qtde_seq = input("Informe quantas sequências você quer querido:")
qtde_seq = int(qtde_seq)
t1 = 0
t2 = 1
cont = 3
print(f"Começo {t1}  - {t2}", end = '')
while cont <= qtde_seq:
    t3 = t1 + t2
    print(f" - {t3} ", end = '')
    t1 = t2
    t2 = t3
    cont += 1
print("Final")
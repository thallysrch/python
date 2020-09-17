
nome_time = input("Informe o nome do time:")
nome_time = str(nome_time)
nrovit =input("Informe Quantas vitórias que o time teve:")
nrovit =int(nrovit)
nroemp =input("Informe quantos empates o time teve:")
nroemp =int(nroemp)
nroderro =input("Informe quantas derrotas o time teve:")
nroderro =int(nroderro)

pvit = nrovit * 3
ptotal = pvit + nroemp

print(f"Pontos do Time {nome_time}: = {ptotal} pontos")






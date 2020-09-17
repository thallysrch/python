list1 =  ['Douglas', 'Anderson', 'Libório', 'Maicon', 'Prefeito Géri']
list2 = ['Douglas', 'Maicon', 'Libório']

lista_final = list(set(list1) - set(list2))

print(f'Os nomes que estão faltando na segunda lista são: {lista_final}')
def List(p1, p2):
    list = []
    while(p1 <= p2):
        print(f'Palavra {p1} de {p2}')
        string = (input('Informe uma palavra para adicionar à sua lista: \n'))
        list.append(string)
        p1 += 1
    return list

p2 = int(input('Quantas palavras gostaria de inserir? : '))
p1 = 1
list = List(p2, p1)

foundMaxWord = max(list, key=len)
import pdb
pdb.set_trace()
lista_listas = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]

lista = [max(i) for i in lista_listas]
print(lista)


lista_2 = [3, 4, 8, 5, 5, 22, 13]


def es_primo(n):
    primo = True
    for i in range(2, n):
        if(n % i == 0):
            primo = False
    return primo


resultado = list(filter(es_primo, lista_2))
print(resultado)

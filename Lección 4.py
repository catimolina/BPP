# import pdb
# pdb.set_trace()


def max_listas(list):
    resultado = [max(row) for row in list]
    return resultado


def es_primo(n):
    primo = True
    for i in range(2, n):
        if(n%i == 0):
            primo = False
    return primo

def primos_lista(list):
    resultado = [i for i in list if es_primo(i)]
    return resultado


if __name__ == '__main__':
    print(max_listas([[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]))
    print(primos_lista([3, 4, 8, 5, 5, 22, 13]))

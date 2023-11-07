

def adyacentes_in_matrix (horizontal,vertical, matriz):
    """
    Funcion que coge parametro horizontal y parametro vertical y lista
    y devuelve los adyacentes arriba izquiera derecha y abajo
    """
    #creamos la lista en la que vamos a meter los adyacentes
    nueva_lista=[]
    #meto los valores horizontales en la lista
    nueva_lista= nueva_lista + adyacentes_in_list(horizontal,crear_lista_horizontal(horizontal,matriz))
    #creamos una lista vertical y la metermos con la horizontal
    nueva_lista = nueva_lista + adyacentes_in_list(vertical,crear_lista_vertical(vertical,matriz))

    return nueva_lista
    

def adyacentes_in_list(posicion,lista):
    """
    funcion que encuentra los adayacentes de una lista
    """
    #creamos una lista en la que vamos a meter los adyacentes
    nueva_lista=[]
    #cogemos el anterior y el posterior comprobando los limites(a mejorar)
    if posicion==0:
        nueva_lista.append(None)
    else:

        nueva_lista.append(lista[posicion-1])
    if posicion==(len(lista)-1):
        nueva_lista.append(None)
    else:
        nueva_lista.append(lista[posicion+1])

    return nueva_lista

def crear_lista_vertical(posicion, matrix):
    nueva_lista=[]
    for item in matrix:
        nueva_lista.append(item[posicion])
    return nueva_lista

def crear_lista_horizontal(posicion, matrix):
    nueva_lista=[]
    nueva_lista= matrix[posicion]
    return nueva_lista
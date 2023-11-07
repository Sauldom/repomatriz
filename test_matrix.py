import pytest
from matrix_boot import *

""""lista=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]"""


def test_adyacentes_in_list():
    lista = [1,2,3,4]

    assert adyacentes_in_list(2,lista) == [2,4]
    assert adyacentes_in_list(0,lista) == [None,2]
    assert adyacentes_in_list(3,lista) ==[3,None]

def test_crear_lista_vertical():
    lista=[     [1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]]
    assert crear_lista_vertical(2,lista)==[3,7,11,15]

def test_crear_lista_horizontal():

        lista=[     [1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]]
        assert crear_lista_horizontal(2,lista)==[9,10,11,12]



def test_adyacentes_in_matrix():
    lista=[     [1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]]
    assert adyacentes_in_matrix(2,2,lista) == [10,12,7,15]
    assert adyacentes_in_matrix(0,0,lista) == [None,2, None, 5]


    

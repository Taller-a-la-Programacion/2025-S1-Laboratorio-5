import Laboratorio5;
import pytest;

###########################################################################################                       
matriz5 = [ [1,0,0,0,0], [1,1,1,1,1], [0,1,0,1,0]]
matriz6 = [ ['A',1,0], [0,'B',0], ['F','F',1], ['A','B',5], [2,'C',9]]

def test_convertirHexADec_1():
    assert Laboratorio5.convertirHexADec(matriz5) == [65536, 69905, 4112]
                       
def test_convertirHexADec_2():
    assert Laboratorio5.convertirHexADec(matriz6) == [2576, 176, 4081, 2741, 713]                       

###########################################################################################   

def test_matriz_1():
    assert Laboratorio5.matrizDiagonalInversa( [[0,0,1,0], [0,0,1,0], [0,0,1,0], [0,0,1,0]]) == [0, 0, 1, 0]
    
def test_matriz_2():
    assert Laboratorio5.matrizDiagonalInversa( [[0,0,1], [0,1,0], [0,0,0]]) == [0, 1, 1]

########################################################################################### 

m = [[1,5,3,7],[2,43,6,8],[11,23,3,4],[7,8,9,10]]
n = [[1,5,7],[2,43,6,8],[11,23,3,4],[7,8,9,10]]

#Pruebas para encontrarNumerosDivisibles
def test_encontrarNumerosDivisibles_1():
    assert isinstance(Laboratorio5.encontrarNumerosDivisibles(n, 2), str) == isinstance("Error: existen vectores de diferente tamaño", str)

def test_encontrarNumerosDivisibles_2():
    assert Laboratorio5.encontrarNumerosDivisibles(m, 2) == [[0,0,0,0],[2,0,6,8],[0,0,0,4],[0,8,0,10]]

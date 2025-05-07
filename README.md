Laboratorio 5

## Instrucciones Generales
- El archivo **debe** llamarse **Laboratorio5.py**
- Debe programar haciendo uso funciones y tecnicas aplicadas en clase

## convertirHexADec(matriz)
- La función debe recibir un parámetro matriz y este debe estar compuesto desde 0 hasta 9 y desde 'A' hasta 'F'. El programa debe retornar una lista con la conversión de hexadecimal a decimal de cada uno de sus vectores.
- Crear las funciones respectivas de conversión numérica según visto en clases
- Recorrer la matriz por sus indices

```python
matriz = [ [1,0,0,0,0], [1,1,1,1,1], [0,1,0,1,0]]
matriz2 = [ ['A',1,0], [0,'B',0], ['F','F',1], ['A','B',5], [2,'C',9]]

>>>convertirHexADec(matriz)
[65536, 69905, 4112]
>>>convertirHexADec(matriz2)
[2576, 176, 4081, 2741, 713]
```

## matrizDiagonalInversa(matriz).
Escriba una función llamada matrizDiagonalInversa que reciba como parámetro de entrada una matriz cuadrada y que retorne como vector la diagonal inversa de la matriz. Evitar funciones built-in.

```python
>>> matrizDiagonalInversa( [[0,0,1,0], [0,0,1,0], [0,0,1,0], [0,0,1,0]])
[0, 0, 1, 0]
>>> matrizDiagonalInversa( [[0,0,1], [0,1,0], [0,0,0]])
[0, 1, 0]
```

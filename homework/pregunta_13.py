"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

# Cargar los archivos
tbl0 = pd.read_csv('files/input/tbl0.tsv', sep='	')
tbl2 = pd.read_csv('files/input/tbl2.tsv', sep='	')

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    df = pd.merge(tbl0, tbl2, how='inner', on='c0')

    resultado = df.groupby('c1')['c5b'].sum()

    return resultado

print(pregunta_13())